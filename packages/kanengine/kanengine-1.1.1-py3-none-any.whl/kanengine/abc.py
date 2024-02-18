"""算法抽象类"""

from abc import ABC, abstractmethod


class EngineABC(ABC):

    @abstractmethod
    def _preprocess(self, *args, **kwargs):
        pass

    @abstractmethod
    def _infer(self, *args, **kwargs):
        pass

    @abstractmethod
    def _postprocess(self, *args, **kwargs):
        pass

    def _pre_inference(self, *args, **kwargs):
        pass
