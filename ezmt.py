from queue import Queue
import threading
import time

# Set up some global variables.
num_threads = 10
q = Queue()

# A real app wouldn't use hard-coded data.
items = ['123', '456', '789',
         '012', '345', '678',
         '901', '234', '567',
         '890', '123', '456',
         '789', '012', '345',
         '678', '901', '234',
         '567', '890', '123',
         '123', '456', '789',
         '012', '345', '678',
         '901', '234', '567',
         '890', '123', '456',
         '789', '012', '345',
         '678', '901', '234',
         '567', '890', '123',
         '123', '456', '789',
         '012', '345', '678',
         '901', '234', '567',
         '890', '123', '456',
         '789', '012', '345',
         '678', '901', '234',
         '567', '890', '123',
         '123', '456', '789',
         '012', '345', '678',
         '901', '234', '567',
         '890', '123', '456',
         '789', '012', '345',
         '678', '901', '234',
         '567', '890', '123',
         '123', '456', '789',
         '012', '345', '678',
         '901', '234', '567',
         '890', '123', '456',
         '789', '012', '345',
         '678', '901', '234',
         '567', '890', '123',
         '123', '456', '789',
         '012', '345', '678',
         '901', '234', '567',
         '890', '123', '456',
         '789', '012', '345',
         '678', '901', '234',
         '567', '890', '123',]
         
def message(s):
    print('{}: {}'.format(threading.current_thread().name, s))

#The function worker_process() runs in the worker thread and processes the data
def worker_process(q):
    """This is the worker thread function.
    It processes items in the queue one after
    another. These daemon threads go into an
    infinite loop, and exit only when
    the main thread ends.
    """
    while True:
        #message('looking for the next enclosure')
        item = q.get()
        print(item)
        time.sleep(1) #a little sleep to simulate delay
        q.task_done()
#Once the target function for the threads is defined, the worker threads can be started. When worker_process() processes the statement url = q.get(), it blocks and waits until the queue has something to return. That means it is safe to start the threads before there is anything in the queue.

# Set up some threads to fetch the data.
for i in range(num_threads):
    worker = threading.Thread(
        target=worker_process,
        args=(q,),
        name='worker-{}'.format(i),
    )
    worker.setDaemon(True)
    worker.start()
#The next step is to retrieve the feed contents using the feedparser module and enqueue the URLs of the enclosures. As soon as the first URL is added to the queue, one of the worker threads picks it up and starts downloading it. The loop continues to add items until the feed is exhausted, and the worker threads take turns dequeuing URLs to download them.

# Download the feed(s) and put the enclosure URLs into
# the queue.
for item in items:
    q.put(item)
#The only thing left to do is wait for the queue to empty out again, using join().

# Now wait for the queue to be empty, indicating that we have
# processed all of the downloads.
message('*** main thread waiting')
q.join()
message('*** done')
