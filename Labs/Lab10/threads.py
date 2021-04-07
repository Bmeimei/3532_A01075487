# Author:            Honghai Mei (Luke)
# Student Number:    A01075487
# Created time:      2021/4/6 21:29
# File Name:         threads.py
from time import sleep
from threading import Thread
from city_processor import ISSDataRequest, CityDatabase

from producer_consumer import CityOverheadTimeQueue


class ProducerThread(Thread):

    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self._cities = cities
        self._queue = queue

    def run(self) -> None:
        super().run()
        times = 0
        for city in self._cities:
            self._queue.access_queue_lock.acquire()
            self._queue.put(ISSDataRequest.get_overhead_pass(city))
            times += 1
            if times % 5 == 0:
                sleep(1)
            self._queue.access_queue_lock.release()


class ConsumerThread(Thread):

    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self._queue = queue
        self.data_incoming = True

    def run(self) -> None:
        super().run()
        while self.data_incoming or len(self._queue) > 0:
            self._queue.access_queue_lock.acquire()
            if len(self._queue) == 0:
                sleep(0.75)
            else:
                item = self._queue.get()
                print(item)
                sleep(0.5)
            self._queue.access_queue_lock.release()


def main():
    """
    Test the Producer and Consumer Threads.
    """
    print("Start Testing the threads, it might costs a while at the beginning, please wait patiently~")
    queue = CityOverheadTimeQueue()
    database = CityDatabase("city_locations.xlsx").city_db

    cities = []
    first_part = []
    second_part = []
    third_part = []
    cities.extend(database)

    # Divide cities into 3 parts
    first_part.extend(cities[0: len(cities) // 3])
    second_part.extend(cities[len(cities) // 3: len(cities) // 3 * 2])
    third_part.extend(cities[len(cities) // 3 * 2::])

    first_producer = ProducerThread(first_part, queue)
    second_producer = ProducerThread(second_part, queue)
    third_producer = ProducerThread(third_part, queue)
    consumer = ConsumerThread(queue)

    first_producer.start()
    second_producer.start()
    third_producer.start()
    consumer.start()

    first_producer.join()
    second_producer.join()
    third_producer.join()
    consumer.data_incoming = False


if __name__ == '__main__':
    main()
