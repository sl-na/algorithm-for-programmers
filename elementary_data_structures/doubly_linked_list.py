import sys
from collections import deque


def validate_key(key: int):
    if 0 <= key <= 10**10 - 1:
        return True
    else:
        return False


def insert(nodes: deque[int], key: int):
    if validate_key(key):
        nodes.appendleft(key)
    else:
        pass


def delete(nodes: deque[int], key: int):
    if not nodes:
        raise ValueError("nodes is empty. cannot delete key")
    for node in nodes:
        if node == key:
            nodes.remove(node)
            break
    else:
        pass


def deleteFirst(nodes: deque[int], key=None):
    if not nodes:
        raise ValueError("nodes is empty. cannot delete first node")
    else:
        nodes.popleft()


def deleteLast(nodes: deque[int], key=None):
    if not nodes:
        raise ValueError("nodes is empty. cannot delete last node")
    else:
        nodes.pop()


def print_list(nodes: deque[int]):
    for i, node in enumerate(nodes):
        if i == len(nodes) - 1:
            print(node)
        else:
            print(node, end=" ")


def main():
    n = int(sys.stdin.readline())
    if n > 2000000:
        raise ValueError("command most not exceed 2000000")
    nodes: deque[int] = deque(maxlen=n)
    input_line = sys.stdin.read().splitlines()
    if len(input_line) != n:
        raise ValueError("input data length is not equal to the first input data")
    for line in input_line:
        i = line.split()
        if len(i) == 1:
            func = i[0]
        elif len(i) == 2:
            func = i[0]
            key = int(i[1])
        else:
            raise ValueError("wrong input data")
        select_func = globals().get(func)
        if not callable(select_func):
            raise ValueError("wrong function name")
        select_func(nodes, key)
    print_list(nodes)


if __name__ == "__main__":
    main()
