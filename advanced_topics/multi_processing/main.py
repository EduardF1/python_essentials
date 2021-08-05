# ******************************************
# multiprocessing
# ******************************************

# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL (used for threading)
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for I/O bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())  # 12 additional processes possible

    a = Process(target=counter, args=(83333333,))
    b = Process(target=counter, args=(83333333,))
    c = Process(target=counter, args=(83333333,))
    d = Process(target=counter, args=(83333333,))
    e = Process(target=counter, args=(83333333,))
    f = Process(target=counter, args=(83333333,))
    g = Process(target=counter, args=(83333333,))
    h = Process(target=counter, args=(83333333,))
    i = Process(target=counter, args=(83333334,))
    j = Process(target=counter, args=(83333334,))
    k = Process(target=counter, args=(83333334,))
    l = Process(target=counter, args=(83333334,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    i.start()
    j.start()
    k.start()
    l.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    i.join()
    j.join()
    k.join()
    l.join()

    print("finished in:", time.perf_counter(), "seconds")


if __name__ == '__main__':
    main()

# initial result (1 process): ca. 46s
# second result (2 processes): ca. 24.5s
# third result (4 processes): ca. 14.6s
# fourth result (12 processes): ca. 9.4s
