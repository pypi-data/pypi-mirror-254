from os import PathLike
from pathlib import Path
from typing import Tuple

# from types import override

import cv2
import numpy as np
from typing_extensions import override
from ..capture import Capture


class VideoCapture(Capture):
    def __init__(self, src: int | str = 0, ):
        """
        VideoCapture from a video stream (file or webcam)
        :param src: source file or webcam which src = 0
        """
        self.cap = cv2.VideoCapture(src)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    @override
    def get_frame(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return frame
            else:
                raise StopIteration
        else:
            raise ValueError("Stream is not opened")

    def __del__(self):
        self.cap.release()


class VideoWriter:
    def __init__(self, path: PathLike | Path | str, fps: int, frame_size: Tuple[int, int]):
        """
        VideoWriter wraps for cv2.VideoWriter
        :param path: path to output video file
        :param fps: fps of the output video
        :param frame_size: (width, height) format of the output video
        """
        path = Path(path)
        type_ = path.suffix
        if type_ == ".avi":
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
        elif type_ == ".mp4":
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        elif type_ == ".flv":
            fourcc = cv2.VideoWriter_fourcc(*'FLV1')
        elif type_ == ".webm":
            fourcc = cv2.VideoWriter_fourcc(*'VP80')
        else:
            raise ValueError("Format not supported!")

        self.writer = cv2.VideoWriter(str(path), fourcc, fps, frame_size)

    def write(self, frame: np.ndarray):
        return self.writer.write(frame)

    def release(self):
        self.writer.release()

    def __del__(self):
        pass
        # self.release()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.release()
        pass


def split_video(video_path, output_path, fmt='.png'):
    video_path = Path(video_path)
    output_path = Path(output_path)
    output_path.mkdir(exist_ok=True)
    cap = VideoCapture(str(video_path))
    for i, frame in enumerate(cap):
        cv2.imwrite(str(output_path / f'{video_path.name}_{i:06}{fmt}'), frame)


def merge_video(input_path, video_path, glob='*.png'):
    input_path = Path(input_path)
    video_path = Path(video_path)
    images = tuple(input_path.glob(glob))
    example = cv2.imread(str(images[0]))
    print(example.shape[:2])
    with VideoWriter(str(video_path), fps=24, frame_size=(example.shape[1], example.shape[0])) as writer:
        for image in images:
            writer.write(cv2.imread(str(image)))


if __name__ == '__main__':
    # split_video('./1.mp4', output_path='output')
    merge_video('output', './2.avi')
