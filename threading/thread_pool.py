import threading
import logging
import time
import concurrent.futures

class FakeDatabase:
    def __init__(self):
        self.value = 0
    
    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)

# creating a threading target function
def target_function(name):
    logging.info("Threading %s starting", name)
    time.sleep(2)
    logging.info("Thread %s: finished", name)
    

if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(target_function, range(3))