import dataclasses
import sys
import threading
import time

from qtpy import QtCore, QtWidgets
from qtpygc import GarbageCollector


@dataclasses.dataclass
class Stats:
    count: int = dataclasses.field()
    secs: float = dataclasses.field(default_factory=time.perf_counter)

    def __sub__(self, other):
        return Stats(self.count - other.count, self.secs - other.secs)

    @property
    def rate(self):
        return self.count / self.secs


class XGarbageCollector(GarbageCollector):
    counter = 0

    def pytest_stats(self):
        return Stats(self.counter)

    def _real_collect(self, dry_run=False):
        self.counter += 1
        return super()._real_collect(dry_run)


def test_interval():
    """
    Check that the GC runs at the correct interval.
    """
    should_exit = False
    exc = None

    def _test():
        nonlocal exc, should_exit
        try:
            t0 = g.pytest_stats()
            time.sleep(2)
            t1 = g.pytest_stats()
            assert 1 <= (t1 - t0).count <= 3

            with g.gc_interval_threadsafe(1 / 20):
                time.sleep(1)
            t2 = g.pytest_stats()
            assert 15 <= (t2 - t1).rate <= 25

            # nesting still uses the lowest so far
            with g.gc_interval_threadsafe(1 / 20):
                with g.gc_interval_threadsafe(1 / 1000):
                    time.sleep(0.0001)

                with g.gc_interval_threadsafe(2):
                    time.sleep(2)
            t3 = g.pytest_stats()
            assert 15 <= (t3 - t2).rate <= 25

            # setting the default GC interval
            g.default_gc_interval = 1 / 40
            time.sleep(1)
            t4 = g.pytest_stats()
            assert 30 <= (t4 - t3).rate <= 50

            return None
        except Exception as e:
            exc = e
        finally:
            should_exit = True

    def _maybe_quit():
        if should_exit:
            app.quit()

    g = XGarbageCollector()
    app = QtWidgets.QApplication(sys.argv)
    tmr = QtCore.QTimer()
    tmr.setInterval(100)
    tmr.timeout.connect(_maybe_quit)
    tmr.start()

    t = threading.Thread(target=_test)
    t.start()

    with g.qt_loop():
        app.exec_()

    t.join()
    if exc:
        raise exc
