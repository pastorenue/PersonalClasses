import threading
import logging
import time

# creating a threading target function
def target_function(name):
    logging.info("Threading %s starting", name)
    time.sleep(2)
    logging.info("Thread %s: finished", name)
    

if __name__ == "__main__":
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    threads = list()
    for index in range(3):
        logging.info("Main   : create and start thread %d.", index)
        x = threading.Thread(target=target_function, args=(index,)) 
        threads.append(x)
        x.start() 
    
    for index, thread in enumerate(threads):
        logging.info("Main   :before joining thread %d.", index)
        thread.join()
        logging.info("Main   : thread %d done", index)