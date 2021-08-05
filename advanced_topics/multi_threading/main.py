#   thread = a flow of execution. Separate order of instructions.
#            However, each thread takes a turn running to achieve concurrency
#            GIL = (global interpreter lock),
#            allows only one thread to hold control of the Python interpreter at any (one) given time (by default, the main thread is the first one that always runs).

#   cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#               For such tasks, multi-processing should be used.

#   io bound = program/task spends most of it's time waiting for external events (user input, web scrapping)
#              Use multithreading.

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


# # sequential execution, ETA to end: 12s
# eat_breakfast()
# drink_coffee()
# study()

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# # concurrent execution, ETA to end: ca. 5s

x.join()
y.join()
z.join()
# thread synchronization, the main thread will wait until the other threads finish
# # synchronized execution, ETA to end: ca. 5.1s

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
