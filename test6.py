# SuperFastPython.com
# example of a thread executing a custom function
import time
from threading import Thread
 
# custom task function
def task():
    # execute a task in a loop
    for i in range(5):
        # block for a moment
        time.sleep(1)
        # report a message
        print('Worker thread running...')
    print('Worker closing down')
 
# create and configure a new thread
thread = Thread(target=task)
# start the new thread




thread.start()

# counter1 = 0
# currentTime1 = time.time()
# while(True):
#     if (time.time() - currentTime1 >= 1):
#         currentTime1 = time.time()
#         counter1 += 1
#         print("Thread 1:", counter1)
#         if counter1 == 10:
#             break

print("guo")
# wait for the new thread to finish
thread.join()

print("wong")