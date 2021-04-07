# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/4/6 20:39
# File Name:         producer_consumer.py
from city_processor import CityOverheadTimes, CityDatabase, ISSDataRequest
from threading import Lock


class CityOverheadTimeQueue:

    def __init__(self) -> None:
        """
        Constructs a Queue.
        """
        self._size = 0
        self._data_queue = []
        self.access_queue_lock = Lock()

    def put(self, overhead_time: CityOverheadTimes) -> None:
        """
        This method is responsible for adding to the queue.
        """
        self._data_queue.append(overhead_time)
        self._size += 1

    def get(self) -> CityOverheadTimes:
        """
        This method is responsible for removing an element from a Queue.
        """
        if self._size == 0:
            raise IndexError("The Queue is Empty!")
        result = self._data_queue[0]
        del self._data_queue[0]
        self._size -= 1
        return result

    def __len__(self) -> int:
        """
        Returns the size of Queue.
        """
        return self._size


def main():
    """
    Test the Queue.
    """
    queue = CityOverheadTimeQueue()
    database = CityDatabase("city_locations.xlsx").city_db
    for i in range(0, 5):
        city = database[i]
        queue.put(ISSDataRequest.get_overhead_pass(city))

    while len(queue) != 0:
        print(queue.get())


if __name__ == '__main__':
    main()
