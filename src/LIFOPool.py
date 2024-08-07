from collections import deque

from .abstraction.basePool import BasePool
from .genericity.t_segment import TSegment


class LIFOPool(BasePool[TSegment]):
    """
    Base class for async operation based on a Last In First Out collection
    """
    __buffer: deque

    def __init__(self):
        super().__init__()
        self.__buffer = deque()

    def enqueue_segment(self, datas: TSegment) -> None:
        self.__buffer.append(datas)

    def retrieve_segment(self) -> TSegment:
        return self.__buffer.pop()

    def is_empty(self) -> bool:
        return len(self.__buffer) == 0

    def clear_buffer(self) -> None:
        self.__buffer = deque()