from functools import lru_cache

import cv2
import numpy as np


def plot_box(image: np.ndarray, box: list, label=None, color=(128, 128, 128), line_width=2):
    line_width = line_width if line_width else max(round(sum(image.shape) / 2 * 0.003), 2)
    p1, p2 = (int(box[0]), int(box[1])), (int(box[2]), int(box[3]))
    cv2.rectangle(image, p1, p2, color, thickness=line_width, lineType=cv2.LINE_AA)

    if label is None:
        return

    cv2.putText(
        img=image,
        text=label,
        org=(p1[0], p1[1] - 2 * line_width),
        fontFace=3,
        fontScale=0.95,
        color=color,
        thickness=1,
        lineType=cv2.LINE_AA
    )


def plot_dot(image: np.ndarray, points: np.ndarray, *, color=(0, 255, 50), radius=3):
    for point in points:
        cv2.circle(image, (point[0], point[1]), radius, color, -1)

    return image


class Plot(object):

    def __init__(self):
        self.palette = [
            (44, 153, 168), (0, 194, 255), (52, 69, 147), (100, 115, 255), (0, 24, 236),
            (132, 56, 255), (82, 0, 133), (203, 56, 255), (255, 149, 200), (255, 55, 199),
            (64, 125, 255), (255, 112, 31), (255, 178, 29), (207, 210, 49), (214, 112, 218),
            (72, 249, 10), (146, 204, 23), (61, 219, 134), (26, 147, 52), (0, 212, 187)
        ]

    @lru_cache(maxsize=128)
    def choose_color(self, index: int):

        return self.palette[index % len(self.palette)]

    def plot_detect(self, image: np.ndarray, pred: list, names: dict):
        """绘制检测框

        Parameters
        ----------
        image : np.ndarray
            原始图像
        pred : list
            检测结果,shape:[n,6],n代表目标个数,6代表坐标、置信度、目标种类
        names : dict
            标签名称

        Returns
        ------
        tuple[np.ndarray,dict[str,int]]
            返回绘制后的原始图像和目标个数统计结果
        """

        num: dict[str, int] = {name: 0 for name in names.values()}
        line_width = max(round(sum(image.shape) / 2 * 0.003), 2)
        for *box, conf, cls in pred:
            label = names[int(cls)]  # TODO label抽离出一个函数
            color = self.choose_color(int(cls))
            plot_box(image, box, label=label, color=color, line_width=line_width)
            num[label] += 1

        return image, num

    def plot_track(self, image: np.ndarray, tracks: np.ndarray, names: dict):

        line_width = max(round(sum(image.shape) / 2 * 0.003), 2)
        for *box, id_, conf, cls, inds in tracks:
            label = names[int(cls)] + '-' + str(int(id_))
            color = self.choose_color(int(cls))
            plot_box(image, box, label=label, color=color, line_width=line_width)

        return image

    def plot_speed(self, image: np.ndarray, speeds: list, names: dict):

        line_width = max(round(sum(image.shape) / 2 * 0.003), 2)
        for box, id_, conf, cls, speed in speeds:
            # label = names[int(cls)] + '-' + str(int(id_)) + f',{speed:.2f}m/s'
            label = f'{speed * 3.6:.1f}km/h'
            color = self.choose_color(int(cls))
            plot_box(image, box, label=label, color=color, line_width=line_width)

        return image

    @staticmethod
    def plot_dot(image: np.ndarray, points: np.ndarray, *,  color=(0, 255, 50), radius=3):
        return plot_dot(image, points, color=color, radius=radius)


PLOT = Plot()
choose_color = PLOT.choose_color
