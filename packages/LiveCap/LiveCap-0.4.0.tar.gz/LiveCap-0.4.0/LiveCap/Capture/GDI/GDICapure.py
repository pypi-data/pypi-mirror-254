from ctypes import *
from ctypes.wintypes import HWND
from pathlib import Path

import numpy as np

from ...capture import Capture


class GDICapture(Capture):
    dll = WinDLL(str(Path(__file__).parent / 'GDICapture.dll'))
    dll.init.restype = c_void_p
    dll.get_frame_sync.argtypes = [c_void_p, np.ctypeslib.ndpointer(dtype=np.int32,
                                                                    ndim=1,
                                                                    flags='C_CONTIGUOUS')]
    dll.get_frame_sync.restype = POINTER(c_ubyte)
    dll.desturct.argtypes = [c_void_p]

    def __init__(self, hwnd: HWND, scale: float):
        """
        Capture Screenshot with GDI Capture Api
        :param hwnd: window handle
        :param scale: scaling factor
        """
        self.hwnd = hwnd
        self.gdi: c_void_p = self.dll.init(hwnd, c_float(scale))

    def __del__(self):
        self.dll.desturct(self.gdi)

    def get_frame_sync(self):
        size = np.array([0, 0], dtype=np.int32)
        res = self.dll.get_frame_sync(self.gdi, size)
        img = np.ctypeslib.as_array(res, shape=(size[0], size[1], 4)).copy()
        return img

    def get_frame(self):
        return self.gdi.get_frame_sync()


if __name__ == '__main__':
    import time
    import cv2

    wgc = GDICapture(windll.user32.FindWindowW(None, "YoloTest"), 1)
    while True:
        t = time.perf_counter()
        img = wgc.get_frame_sync()
        print(f'time: {time.perf_counter() - t:.6f}s')
        cv2.imshow('1', img)
        cv2.waitKey(0)
        break
