from sys import stdin


class Node:
    def __init__(self, key=None):
        if key is not None and not (0 <= key <= 1234566890):
            return None
        self.key = key
        self.next = None
        self.prev = None


class LinkedList:
    sentinel: Node

    def __init__(self):
        self.sentinel = Node()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def insert(self, key):
        x = Node(key)
        x.next = self.sentinel.next
        self.sentinel.next.prev: Node = x
        self.sentinel.next = x
        x.prev = self.sentinel

    def list_search(self, key):
        cur = self.sentinel.next
        while cur is not None and cur != self.sentinel and cur.key != key:
            cur = cur.next
        return cur

    def delete_node(self, t):
        if t == self.sentinel:
            return
        t.prev.next = t.next
        t.next.prev = t.prev

    def delete_first(self):
        self.delete_node(self.sentinel.next)

    def delete_last(self):
        self.delete_node(self.sentinel.prev)

    def delete_key(self, key):
        self.delete_node(self.list_search(key))

    def print_list(self):
        cur = self.sentinel.next
        output = []
        while cur is not None and cur != self.sentinel:
            output.append(str(cur.key))
            cur = cur.next
        print(" ".join(output))


def main():
    n = int(stdin.readline())
    nodes = LinkedList()
    input_line = stdin.read().splitlines()
    if len(input_line) != n:
        raise ValueError("invalid input")
    for line in input_line:
        input = line.split()
        func = input[0]
        if func == "insert":
            nodes.insert(int(input[1]))
        elif func == "delete":
            nodes.delete_key(int(input[1]))
        elif func == "deleteFirst":
            nodes.delete_first()
        elif func == "deleteLast":
            nodes.delete_last()
        else:
            raise ValueError("invalid input")
    nodes.print_list()


if __name__ == "__main__":
    main()
