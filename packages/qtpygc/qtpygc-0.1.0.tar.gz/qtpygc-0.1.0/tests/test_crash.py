import gc
import multiprocessing
import threading
import time
import sys

import pytest

from qtpygc import GarbageCollector
from qtpy import QtCore, QtWidgets


class CyclicChildWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self._parent = parent
        self._timer = t = QtCore.QTimer()
        t.setInterval(2)
        t.timeout.connect(lambda: time.sleep(0.03))
        t.start()


class CyclicWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        CyclicChildWidget(self)


def main(use_qtpygc: bool):
    gc.set_threshold(*(x // 10 + 1 for x in gc.get_threshold()))

    app = QtWidgets.QApplication(sys.argv)

    # alive = lambda: sum(isinstance(o, CyclicWidget) for o in gc.get_objects())

    should_stop = False
    cell = [None]

    def create_other_garbage_outside_qt_thread():
        while not should_stop:
            time.sleep(24e-3)
            cell[0] = None
            lst = [[] for x in range(1000)]  # noqa
            del lst
            # import gc
            # print("before", alive())
            # gc.collect()
            # print(alive())

    def create_garbage_in_qt_thread():
        if cell[0] is None:
            cell[0] = CyclicWidget()

    t = threading.Thread(target=create_other_garbage_outside_qt_thread)
    t.start()

    try:
        timer = QtCore.QTimer()
        timer.setInterval(23)
        timer.timeout.connect(create_garbage_in_qt_thread)
        timer.start()

        kill_timer = QtCore.QTimer()
        kill_timer.setInterval(15000)
        kill_timer.timeout.connect(app.exit)
        kill_timer.start()

        if use_qtpygc:
            g = GarbageCollector()
            with g.qt_loop():
                app.exec_()
        else:
            app.exec_()

        print("all good")
    finally:
        should_stop = True
        t.join()


if __name__ == "__main__":
    main(bool(int(sys.argv[-1])))


@pytest.mark.parametrize("use_qtpygc", (False, True))
def test_crash(use_qtpygc):
    import subprocess

    ret = subprocess.run([sys.executable, __file__, str(int(use_qtpygc))], stdout=subprocess.PIPE)

    ok = b"all good" in ret.stdout and ret.returncode == 0
    assert ok == use_qtpygc, "crash should occur iff use_qtpygc is not used"
