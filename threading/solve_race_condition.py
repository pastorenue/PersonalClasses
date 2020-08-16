import threading
import logging
import time
import concurrent.futures

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
    
    def locked_update(self, value):
        logging.info("thread %s: starting update", value)
        logging.debug("Thread %s about to lock", value)
        with self._lock:
            logging.debug("Thread %s has lock", value)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", value)
        logging.debug("Thread %s after release", value)
        logging.info("Thread %s: finishing update", value)
    
    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)


# creating a threading target function
if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.getLogger().setLevel(logging.DEBUG)
    
    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.info("Testing update. Ending value is %d.", database.value)