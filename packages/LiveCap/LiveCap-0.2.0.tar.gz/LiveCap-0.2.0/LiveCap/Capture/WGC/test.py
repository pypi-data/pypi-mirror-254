import asyncio
import ctypes
import time

from screenshot import WindowsGraphicsCapture
import cv2


async def main():
    # cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    user32 = ctypes.windll.user32

    # https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-findwindoww
    handle = user32.FindWindowW("UnityWndClass", "崩坏：星穹铁道")
    snapshot = WindowsGraphicsCapture(handle)
    img = await snapshot.get_frame()
    cv2.imwrite("test.jpg", img)

    # while 1:
    #     await asyncio.sleep(1)
    #     t = time.time()
    #     img = await snapshot.get_frame()
    #     print(f"time: {time.time() - t:.6f}s")

    # # call async func
    # t = time.time()
    # count = 0
    # # show capture frame
    # while 1:
    #     image = await snapshot.get_frame()
    #     # print(image.shape)
    #     count += 1
    #     if count > 99:
    #         print(f'FPS: {count / (time.time() - t):.6f}s')
    #         count = 0
    #         t = time.time()
    #     cv2.imshow('image', image)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    # cv2.destroyAllWindows()
    return


if __name__ == "__main__":
    asyncio.run(main())
