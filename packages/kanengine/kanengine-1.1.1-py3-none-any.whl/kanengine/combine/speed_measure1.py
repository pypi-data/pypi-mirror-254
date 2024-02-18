from collections import defaultdict

import numpy as np

from kanengine.base.detect import BaseDetector
from kanengine.base.boxmot import BYTETracker
from ..utils.plot import PLOT


class SpeedMeasure(object):

    def __init__(self, detector: BaseDetector = None, **kwargs):
        if detector is None:
            detector = BaseDetector(**kwargs)
        self._names = detector.names
        self._detector = detector
        self._tracker = BYTETracker()
        self._time_interval = 0  # 前后两帧的时间差
        self._base_speed = 0  # 基准速度
        self._rate = 0  # 图像中每一个像素对应现实中多少米
        self._objects = defaultdict(tuple)

    def _measure(self, tracks: np.ndarray):
        measure_results = []
        for *box, id_, conf, cls, ind in tracks:
            x1, y1 = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2

            if id_ not in self._objects:
                self._objects[id_] = x1, y1
                continue

            x2, y2 = self._objects[id_]
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            virtual_speed = distance / self._time_interval
            sign = -1 if y1 - y2 > 0 else 1
            real_speed = sign * virtual_speed * self._rate + self._base_speed
            print(
                f'id:{int(id_)},v-v:{virtual_speed:.2f},r-v:{real_speed:.2f},s:{distance:.2f},sign:{sign}')
            self._objects[id_] = x1, y1
            measure_results.append((box, id_, conf, cls, real_speed))

        return measure_results

    def __call__(self, img: np.ndarray, base_speed: float, time_interval: float, rate: float):
        self._rate = rate
        self._base_speed = base_speed
        self._time_interval = time_interval
        dets = self._detector(img)
        tracks = self._tracker.update(dets, None)
        measure_results = self._measure(tracks)
        plotted_img = PLOT.plot_speed(img, measure_results, self._names)

        return plotted_img
