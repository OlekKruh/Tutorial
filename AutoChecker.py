from collections import deque

MAX_LEN = 5

fifo = deque(maxlen=MAX_LEN)


def push(element):
    global fifo
    fifo.append(element)
    return fifo


def pop():
    global fifo
    res = fifo.popleft()
    return res
