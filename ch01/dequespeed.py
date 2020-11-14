from collections import deque
from functools import partial
from timeit import Timer

dq = deque(range(10000))

_list = list(range(10000))


def rotate_deque(dq):
    for i in range(10000):
        dq.rotate()


def rotate_list(_list):
    for i in range(10000):
        _list = _list[-i:] + _list[:-i]


deque_timer = Timer(partial(rotate_deque, dq))
list_timer = Timer(partial(rotate_list, _list))

print(f'deque {deque_timer.timeit(10) * 1000} ms')
print(f'list {list_timer.timeit(10) * 1000} ms')