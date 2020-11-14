from _collections import deque
from time import sleep
from threading import Thread

que = deque()


def fun1(que: deque):
    for p in range(10, 110, 10):
        sleep(1)
        que.append(str(p) + '%')


def fun2(que: deque):
    for p in range(10, 110, 10):
        sleep(1)
        if que:
            print(que.popleft())


if __name__ == '__main__':
    p1 = Thread(target=fun1, args=(que,))
    p2 = Thread(target=fun2, args=(que,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
