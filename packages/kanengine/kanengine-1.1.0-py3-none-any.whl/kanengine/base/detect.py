"""
    基础检测器
"""

from typing import TypeAlias

import numpy as np
import torch

from kanengine.abc import EngineABC
from kanengine.utils.ops import Ops

ConfArg: TypeAlias = dict[int, float]
ConfArgs: TypeAlias = list[ConfArg]
OrigImg: TypeAlias = np.ndarray
OrigImgs: TypeAlias = list[OrigImg]


class BaseDetector(EngineABC):

    def __init__(self, weight_path: str, device: str, fp16: bool, names=None) -> None:
        device = torch.device(device)
        model = torch.jit.load(weight_path, map_location=device)
        model.half() if fp16 else model.float()
        model.eval()
        self.model = model
        self.fp16 = fp16
        self.device = device
        self.names = names if isinstance(names, dict) else dict()
        self._pre_inference()

    def _pre_inference(self):
        """预热"""
        for _ in range(100):
            arr = torch.randn((1, 3, 640, 640), device=self.device)
            arr = arr.half() if self.fp16 else arr.float()
            self.model(arr)

    def __call__(self, orig_im: OrigImgs | OrigImg, conf_arg: ConfArgs | ConfArg | None = None):
        """检测,流程为:前处理 --> 推理 --> 后处理

        Parameters
        ----------
        orig_im : OrigImgs | OrigImg
            原始图像列表
        conf_arg: ConfArgs | ConfArg | None
            nms的相关参数(类别、置信度)列表,例如[{0:0.2,1:0.3,2:0.5},{1:0.4,2:0.25}]

        Returns
        -------
        list[np.ndarray] | np.ndarray
            返回每张图像的检测结果,如[[[200,100,300,200,0.7,1],[100,200,150,300,0.8,0]],
            [[1000,1500,1200,2000,0.65,1],[100,1300,120,1400,0.4,3]]]
        """

        is_one = not isinstance(orig_im, list)  # 判断是否为单张图像检测
        orig_im = [orig_im] if is_one else orig_im
        tensor_im = self._preprocess(orig_im)
        preds = self._infer(tensor_im)
        args = tensor_im, orig_im, conf_arg
        processed_pred = self._postprocess(preds, *args)
        processed_pred = processed_pred[0] if is_one and processed_pred else processed_pred

        return processed_pred

    def _infer(self, im: torch.Tensor) -> torch.Tensor:
        """推理"""
        return self.model(im)

    def _preprocess(self, ims: list[np.ndarray]):
        """前处理

        Parameters
        ----------
        ims : list[np.ndarray]
            原始图像列表

        Returns
        -------
        torch.Tensor
            返回预处理结果
        """

        ims = [Ops.adjust_scale(im) for im in ims]  # 原始图像尺寸 --> 模型推理的输入图像尺寸
        ims = np.stack(ims, 0)
        ims = ims[..., ::-1].transpose(0, 3, 1, 2)  # BHWC --> BCHW
        ims = np.ascontiguousarray(ims)

        # np.ndarray 转换成 torch.tensor
        tensor_ims = torch.from_numpy(ims).to(self.device)
        tensor_ims = tensor_ims.half() if self.fp16 else tensor_ims.float()
        tensor_ims /= 255.0

        return tensor_ims

    def _postprocess(self, preds: torch.Tensor, *args):
        """后处理一批图像的推理结果

        Parameters
        ----------
        preds : torch.Tensor
            模型推理的结果
        args : tuple
            后处理的其他参数
        """

        tensor_ims, orig_ims, nms_args = args
        nms_args = nms_args if nms_args else [None] * len(orig_ims)
        processed_preds = []

        for pred, tensor_im, orig_im, nms_arg in zip(preds, tensor_ims, orig_ims, nms_args):
            # 非极大值抑制nms处理
            processed_pred = Ops.nms(pred, nms_arg)

            # boxes坐标恢复到原始图像
            processed_pred[..., :4] = Ops.restore_scale(
                img1_shape=tensor_im.shape[-2:],
                boxes=processed_pred[..., :4],
                img0_shape=orig_im.shape[:2]
            )
            processed_preds.append(processed_pred.to('cpu').numpy())

        return processed_preds
