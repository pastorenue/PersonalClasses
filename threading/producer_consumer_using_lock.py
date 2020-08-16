import random
import logging

SENTINEL = object()

def producer(pipeline):
    """Pretend we're getting a message fro mthe network"""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")
    
    # send a sentinel message to tell the consumer we're done
    pipeline.set_message(SENTINEL, "Producer")
    

def consumer(pipeline):
    """Pretending we're saving a number into the database"""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)
        