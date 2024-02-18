"""通用目标检测"""

from typing import TypeAlias
from collections.abc import Generator

import numpy as np

from kanengine.utils.plot import PLOT, choose_color
from kanengine.register import ENGINES
from kanengine.base import BaseDetector

YieldType: TypeAlias = tuple[np.ndarray, list]
SendType: TypeAlias = tuple[np.ndarray, dict]
DetectGenerator: TypeAlias = Generator[YieldType, SendType, None]


@ENGINES.register()
class CommonDetector(BaseDetector):

    def __init__(self, weight_path: str, names: dict[int, str], device='cuda:0', fp16=True, interval=1) -> None:
        super().__init__(weight_path, device, fp16)
        self.names = names
        self.interval = interval

    def __call__(self, orig_img: np.ndarray, conf_args: dict[int, float] | None = None) -> DetectGenerator:

        # 执行推理
        pred: np.ndarray = super().__call__([orig_img], [conf_args])[0]
        result = None

        while True:
            item = yield result
            orig_img, conf_arg = item
            mask = np.isin(pred[:, -1], list(conf_arg.keys()))
            _preds: list = pred[mask].tolist()
            labels = []
            for *box, conf, cls in pred:
                box = [int(b) for b in box]
                label = {
                    'wide': box[2] - box[0],
                    'high': box[3] - box[1],
                    'abscissa': box[0],
                    'ordinate': box[1],
                    'labelName': self.names[cls],
                    'color': choose_color(int(cls))
                }
                labels.append(label)

            plot_img = orig_img.copy() if len(labels) else orig_img
            plotted_img, _ = PLOT.plot_detect(plot_img, _preds, self.names)

            result = plotted_img, labels
