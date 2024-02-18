import time
from ctypes import *
import numpy as np
import cv2
from pathlib import Path

from ...capture import Capture


class DXGICapture(Capture):
    dll_path = Path(__file__).parent / 'DXGICapture.dll'
    dll = WinDLL(str(dll_path))
    dll.get_frame.res_type = c_int

    def __init__(self):
        """
        Capture Screenshot with DXGI Api
        """
        self.dll.init()
        r = np.array([0, 0])
        r_ptr = r.ctypes.data_as(POINTER(c_int))
        self.dll.get_range(r_ptr)
        self.width, self.height = r
        self.img = np.zeros(self.height * self.width * 4, dtype=np.uint8)

    def get_frame(self) -> np.ndarray:
        self.img = np.ascontiguousarray(self.img)
        arr_ptr = cast(self.img.ctypes.data, POINTER(c_ubyte))
        res = self.dll.get_frame(arr_ptr)
        if res != self.width:
            raise RuntimeError("Capture Fail!")
        img_res = self.img.copy().reshape((self.height, self.width, 4))
        return img_res

    def __call__(self, *args, **kwargs) -> np.ndarray | None:
        try:
            return self.get_frame()
        except (RuntimeError, OSError):
            print("Capture Fail!")
            return

    def __next__(self):
        res = self()
        while res is None:
            res = self()
        # if res is None:
        #     raise StopIteration

        return res

    def __del__(self):
        self.dll.destruct()


if __name__ == '__main__':
    cap = DXGICapture()
    print(cap.height, cap.width)

    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    # count = 0
    # t = time.time()
    t = time.perf_counter()

    for img in cap:
        cv2.imshow('frame', img)
        cv2.waitKey(1)

    # cv2.imshow('frame', img)
    # cv2.waitKey(1)

    # cv2.imshow('img', img)
    # cv2.waitKey(0)
