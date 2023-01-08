from threading import *
import time
counter1 = 0
class App1(Thread):
    def run(self):
        global counter1
        currentTime1 = time.time()
        while(True):
            if (time.time() - currentTime1 >= 1):
                currentTime1 = time.time()
                counter1 += 1
                print("Thread 1:", counter1)
                if counter1 == 10:
                    break


class App2(Thread):
    def run(self):
        global counter1
        while(True):
            if counter1 >= 5:
                currentTime2 = time.time()
                counter2 = 0
                if (time.time() - currentTime2 >= 0.5):
                    currentTime2 = time.time()
                    counter2 += 1
                    print("Thread 2:", counter2)
                    if counter2 == 10:
                        break


            



app1 = App1()
app2 = App2()

app1.start()
app2.start()
