"""处理工具模块"""

from functools import lru_cache

import cv2
import numpy as np
import torch
import torchvision


class Ops(object):

    @staticmethod
    def adjust_scale(img: np.ndarray, new_shape: tuple = (640, 640)):
        shape = img.shape[:2]

        # 根据原图的高宽比计算新的高宽
        r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
        new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))

        # 缩放原图至新的高宽
        if shape[::-1] != new_unpad:
            img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_LINEAR)

        # 计算边缘的宽和高
        dw = (new_shape[1] - new_unpad[0]) / 2
        dh = (new_shape[0] - new_unpad[1]) / 2

        # 拓展边缘
        top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
        left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
        img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=(114, 114, 114))

        return img

    @staticmethod
    def restore_scale(img1_shape: torch.Size, boxes: torch.Tensor, img0_shape: tuple):
        """将检测框从推理的输入图中映射到原始图像中

        Parameters
        ----------
        img1_shape : torch.Size
            推理的输入图的性状(hw)
        boxes : torch.Tensor
            nms过后的检测框(xyxy)
        img0_shape : tuple
            原始图的性状(hw)

        Returns
        -------
        _type_
            _description_
        """
        gain = min(img1_shape[0] / img0_shape[0], img1_shape[1] / img0_shape[1])
        pad = round((img1_shape[1] - img0_shape[1] * gain) / 2 - 0.1), round(
            (img1_shape[0] - img0_shape[0] * gain) / 2 - 0.1)
        boxes[..., [0, 2]] -= pad[0]
        boxes[..., [1, 3]] -= pad[1]
        boxes[..., :4] /= gain

        boxes[..., 0].clamp_(0, img0_shape[1])  # x1
        boxes[..., 1].clamp_(0, img0_shape[0])  # y1
        boxes[..., 2].clamp_(0, img0_shape[1])  # x2
        boxes[..., 3].clamp_(0, img0_shape[0])  # y2

        return boxes

    @staticmethod
    def nms(pred: torch.Tensor, nms_arg: dict[int, float] | None = None, iou_thres=0.45, max_det=1500):
        """对单个pred进行nms

        Parameters
        ----------
        pred : torch.Tensor
            检测器推理后的结果,shape为[4+num_classes, num_boxes]
        nms_arg : dict
            每个类别的置信度,例如{0:0.3,2:0.4}
        """

        # 获取nms参数
        class_num = pred.shape[0] - 4  # 类别数量
        nms_arg = {i: 0.25 for i in range(class_num)} if nms_arg is None else nms_arg
        class_list = list(nms_arg.keys())
        conf_list = list(nms_arg.values())

        # 初始化条件
        condition = torch.zeros(pred.shape[1], dtype=torch.bool, device=pred.device)
        for classes, conf in zip(class_list, conf_list):
            condition = torch.logical_or(condition, pred[4 + classes, :] >= conf)
        pred = pred[:, condition]

        # 如果没有检测框，则返回空
        if not pred.shape[1]:
            return torch.zeros((0, 6), device=pred.device)

        # 将x,y,w,h转换为xyxy
        pred = pred.transpose(1, 0)
        pred[..., :4] = Ops.xywh2xyxy(pred[..., :4])

        # 将每个类别的检测框和置信度拼接成一个数组
        box, cls = pred.split((4, class_num), 1)
        conf, j = cls.max(1, keepdim=True)
        pred = torch.cat((box, conf, j.float()), 1)

        # 筛选需要检测的类别
        if len(class_list) != class_num:
            pred = pred[(pred[:, 5:6] == torch.tensor(class_list, device=pred.device)).any(1)]

        # 如果没有检测框，则返回空
        if not pred.shape[0]:
            return torch.zeros((0, 6), device=pred.device)

        # 进行nms计算
        c = pred[:, 5:6] * 7680
        boxes, scores = pred[:, :4] + c, pred[:, 4]
        index = torchvision.ops.nms(boxes, scores, iou_thres)
        index = index[:max_det]

        return pred[index]

    @staticmethod
    def xywh2xyxy(x: torch.Tensor):
        y = torch.empty_like(x)
        dw = x[..., 2] / 2  # half-width
        dh = x[..., 3] / 2  # half-height
        y[..., 0] = x[..., 0] - dw  # top left x
        y[..., 1] = x[..., 1] - dh  # top left y
        y[..., 2] = x[..., 0] + dw  # bottom right x
        y[..., 3] = x[..., 1] + dh  # bottom right y
        return y
