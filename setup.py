from src import *

class ListPool(BasePool[TSegment]):
    __buffer: list

    def __init__(self):
        super().__init__()

    def __init__(self):
        super().__init__()
        self.__buffer = list()

    def enqueue_segment(self, datas: TSegment) -> None:
        self.__buffer.append(datas)

    def retrieve_segment(self) -> TSegment:
        return self.__buffer.pop()

    def is_empty(self) -> bool:
        return len(self.__buffer) == 0

    def clear_buffer(self) -> None:
        self.__buffer = list()

    def process_segment(self, segment: int) -> None:
        print(segment)

with ListPool() as pool:
    pool.pause()
    for i in range(10):
        pool.enqueue_segment(i)
    pool.start()