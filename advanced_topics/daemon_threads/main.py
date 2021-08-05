#   daemon thread = a thread that runs in the background, not important for a program to run
#                   the program will not wait for daemon threads to complete before exiting.
#                   Non-daemon threads cannot normally be killed, they stay alive until their task
#                   is complete.
#
#                   ex.: background tasks, garbage collection, waiting for input, long running processes

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, "seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)
# print(x.isDaemon())  # check if a thread is daemon

answer = input("Do you wish to exit?")
