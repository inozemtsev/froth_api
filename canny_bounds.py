import cv2
import numpy as np
import os

from argparse import ArgumentParser
from os.path import join


def get_canny_bounds(frame,
                    color=[36,255,12]):
    """
    
    Возвращает изображение с границами Кённи
    
    :param frame: путь к изображению
    :param color: цвет границ
    
    :return: массив с изображением и границами
    
    """
    frame = cv2.imread(frame)
    frame_canny = cv2.Canny(frame, 50, 150)
    out_frame = []
    for num1, i in enumerate(frame_canny):
        row = []
        for num2, j in enumerate(i):
            if j == 255:
                row.append(color)
            else:
                row.append(list(frame[num1, num2]))
        out_frame.append(row)
    return np.array(out_frame) / 255.


parser = ArgumentParser()
parser.add_argument("--video_name",
                   default="F5_1_2_1.ts",
                   required=False)
parser.add_argument("--frames_dir",
                   default="/Users/artemsenin/nornickel_hack/all_frames",
                   required=False)


if __name__ == "__main__":
    args = parser.parse_args()
    all_frames = os.listdir(args.frames_dir)
    video_frames = [frame for frame in all_frames
                   if args.video_name in frame]
    n_frames = len(video_frames)
    for i in range(n_frames):
        frame_path = join(args.frames_dir, f"{args.video_name}_f_{i}.jpg")
        canny_bounds = get_canny_bounds(frame_path)
        cv2.imshow('canny_bounds', canny_bounds)
        cv2.waitKey(1)
    