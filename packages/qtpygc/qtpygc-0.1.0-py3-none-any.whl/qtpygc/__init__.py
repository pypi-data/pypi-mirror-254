"""
Example code::


    from qtpygc import GarbageCollector

    g = GarbageCollector()
    with g.qt_loop():
        qtpy.QCoreApplication.exec_()


In other threads you can do::


    g.maybe_collect_threadsafe()


Inspired by Kovid Goyal's post on:
https://riverbankcomputing.com/pipermail/pyqt/2011-August/030378.html
"""

from contextlib import contextmanager
import gc
from threading import RLock

from heapdict import heapdict
from qtpy.QtCore import QCoreApplication, QEvent, QObject, QTimer, Signal, Slot


_TypeUser = QEvent.Type.User


class GarbageCollector:
    """
    Manual garbage collector. Use :meth:`qt_loop` to wrap the main Qt loop and periodically run
    manual garbage collection in the GUI thread.
    """
    def __init__(self, default_gc_interval: float = 1.0, auto_disable_runtime_gc: bool = True):
        self.qobject = None
        self._gc_interval = None
        self._gc_interval_heapdict = heapdict()
        self.lock = RLock()
        self.default_gc_interval = default_gc_interval

        if auto_disable_runtime_gc:
            gc.disable()

    @property
    def default_gc_interval(self):
        return self._default_gc_interval

    @default_gc_interval.setter
    def default_gc_interval(self, value):
        with self.lock:
            self._default_gc_interval = value
            self._gc_interval_heapdict[None] = value
            self._update_interval_maybe()

    @property
    def gc_interval(self):
        """
        Current GC interval in seconds. Read-only attribute.

        To modify, set :attr:`default_gc_interval` or use :meth:`gc_interval_threadsafe`.
        """
        return self._gc_interval

    def _update_interval_maybe(self):
        """
        You must acquire :attr:`lock` before calling this.
        """
        old = self._gc_interval
        new = self._gc_interval_heapdict.peekitem()[1]
        if old != new:
            self._gc_interval = new
            self._gc_interval_qt_msec = max(round(new * 1000), 1)
            self._notify_qt()

    def maybe_collect_threadsafe(self):
        """
        Check whether a garbage collection should be performed. If yes, then notify the event
        loop on the main Qt thread so that a garbage collection is performed from the main
        Qt thread.

        Call this method periodically from any thread when you think too much garbage has
        accumulated.
        """
        # do not wake up the Qt main loop unless a collection should actually occur
        if self._real_collect(True):
            with self.lock:
                qo = self.qobject
                if qo is not None:
                    self._notify_qt()
                else:
                    self._real_collect()

    @contextmanager
    def qt_loop(self):
        """
        Only call this from the main (Qt) thread!!

        Convenient context manager.
        """
        self.start_qt()
        try:
            yield self
        finally:
            self.stop_qt()

    @contextmanager
    def gc_interval_threadsafe(self, interval: float):
        """
        Temporarily set the minimum garbage collection interval. You can nest this context manager
        or call it from multiple threads at the same time and it will work.
        """
        h = self._gc_interval_heapdict
        h_key = object()
        with self.lock:
            h[h_key] = interval
            self._update_interval_maybe()

        try:
            yield self
        finally:
            del h[h_key]
            self._update_interval_maybe()

    def _real_collect(self, dry_run: bool = False) -> bool:
        _gc = gc
        thresholds = _gc.get_threshold()
        counts = _gc.get_count()
        for i in (2, 1, 0):
            if counts[i] > thresholds[i]:
                if not dry_run:
                    _gc.collect(i)
                return True

        return False

    def _notify_qt(self):
        """
        Notify the QObject so that it runs a GC and/or changes the interval.

        You must have acquired :attr:`lock` before calling this.
        """
        qo = self.qobject
        if qo is not None:
            qo._notify_me_threadsafe()

    def start_qt(self) -> None:
        """
        Only call this from the main (Qt) thread!

        You should probably use :meth:`qt_loop` instead.
        """
        if gc.isenabled():
            raise AssertionError("automatic garbage collection should be disabled")

        with self.lock:
            obj = _QtGarbageCollector()
            obj.init(self)
            self.qobject = obj

    def stop_qt(self) -> None:
        """
        Only call this from the main (Qt) thread, preferably after you have ended your
        event loop.
        """
        with self.lock:
            if self.qobject is not None:
                # ensure that the object is deleted
                self.qobject.deleteLater()
                destroy = True
            else:
                destroy = False

        if destroy:
            QCoreApplication.instance().processEvents()

    def _qobject_deleted(self) -> None:
        with self.lock:
            if self.qobject is not None:
                self.qobject = None


class _QtGarbageCollector(QObject):
    garbage_collector: "GarbageCollector" = None
    gc_timer: QTimer = None
    gc_interval_msec: int = -1
    gc_notification_signal = Signal()

    def init(self, garbage_collector) -> None:
        self.garbage_collector = garbage_collector
        self.gc_timer = timer = QTimer(self)
        self.gc_interval_msec = msec = garbage_collector._gc_interval_qt_msec
        timer.setInterval(msec)
        timer.timeout.connect(self._handle_notified)
        timer.start()
        self.gc_notification_signal.connect(self._handle_notified)
        self.destroyed.connect(garbage_collector._qobject_deleted)

    def _notify_me_threadsafe(self) -> None:
        """
        Trigger a garbage collection in the main thread from a different thread.

        This is the only thread-safe method of this class, and you must still ensure that this
        object isn't destroyed while you are calling it by using a lock or something.
        """

        QCoreApplication.postEvent(self, QEvent(_TypeUser))

    @Slot()
    def _handle_notified(self) -> None:
        g = self.garbage_collector
        if g is not None:
            new_msec = g._gc_interval_qt_msec
            if new_msec != self.gc_interval_msec:
                timer = self.gc_timer
                timer.stop()
                timer.setInterval(new_msec)
                timer.start()
                self.gc_interval_msec = new_msec
            g._real_collect()

    def event(self, event):
        if event.type() == _TypeUser:
            self.gc_notification_signal.emit()
        return super().event(event)
