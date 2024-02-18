import cv2
import numpy as np

from kanengine.base import BasePeopleFlowDetect
from kanengine.utils.plot import PLOT
from kanengine.register import ENGINES


@ENGINES.register()
class PeopleFlowDetect(BasePeopleFlowDetect):

    def __call__(self, orig_im: np.ndarray, threshold=0.3, option_area: dict | None = None):
        h, w = orig_im.shape[:2]
        _orig_im = orig_im

        if option_area:
            pts = np.array([option_area["x"], option_area["y"]]).T

            # 若点数不等于4或长宽不等于原始图像,则去ROI区域
            if len(pts) != 4 or np.sum(np.abs(pts[0] - pts[2]) + np.abs(pts[1] - pts[3])) != 4:
                pts[:, 0] = pts[:, 0] * w
                pts[:, 1] = pts[:, 1] * h
                pts = pts.astype(np.int32)
                mask = np.zeros_like(orig_im, dtype=np.uint8)
                cv2.fillPoly(mask, [pts], color=(255, 255, 255))
                _orig_im = cv2.bitwise_and(orig_im, mask)

        pred_pts = super().__call__(_orig_im, threshold)
        pred_pts = pred_pts.astype(np.int32)
        plotted_im = PLOT.plot_dot(orig_im.copy(), pred_pts)
        if len(pred_pts):
            res_pts = {'x': (pred_pts[:, 0] / w).tolist(), 'y': (pred_pts[:, 1] / h).tolist()}
        else:
            res_pts = {'x': [], 'y': []}

        return plotted_im, res_pts
