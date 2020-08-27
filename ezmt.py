from queue import Queue
import threading
import time

# Set up some global variables.
num_threads = 10
q = Queue()

#lots of fake data
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

#message format
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
        #message('Processing next item')
        item = q.get()
        print(item)
        time.sleep(1) #a little sleep to simulate delay
        q.task_done()

#Once the target function for the threads is defined, the worker threads can be started. When worker_process() processes the statement item = q.get(), it blocks and waits until the queue has something to return. That means it is safe to start the threads before there is anything in the queue.
# Set up some threads to fetch the data.
for i in range(num_threads):
    worker = threading.Thread(
        target=worker_process,
        args=(q,),
        name='worker-{}'.format(i),
    )
    worker.setDaemon(True)
    worker.start()

#below is the code that'll fill the queue with the items to process
for item in items:
    q.put(item)

#The only thing left to do is wait for the queue to empty out again, using join().
# Now wait for the queue to be empty, indicating that we have
# processed all of the data.
message('*** main thread waiting')
q.join()
message('*** done')
