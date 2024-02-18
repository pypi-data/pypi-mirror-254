import numpy as np
import cv2


class VisualWindow:
    def __init__(self, name="Camera"):
        self.name = name
        cv2.namedWindow(name, cv2.WINDOW_NORMAL)

    def write(self, frame):
        cv2.imshow(self.name, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return False
        return True

    def show(self, frame):
        cv2.imshow(self.name, frame)
        cv2.waitKey(0)
        # while True:
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break


def read_rgb_image(path, size=(2560, 1440, 4)):
    img = np.fromfile(open(path, 'rb'), np.uint8).reshape(size)
    return img


def rgb2gbr(img: np.ndarray) -> np.ndarray:
    """
    使用numpy完成图像RGB与BGR之间的转换
    :param img: numpy数组格式的图片
    :return: 转换后的图片
    """
    return img[:, :, ::-1]
