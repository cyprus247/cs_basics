from node import Node


class LinkedList:
    def __init__(self):
        self.head: [Node, None] = None

    def get(self, value) -> Node:
        n = self.head
        while True:
            if n.value == value:
                return n
            else:
                if n._next is None:
                    break
                else:
                    n = n._next

    def search(self, value):
        n = self.get(value=value)
        if n is None:
            return f"node with value {value} not found"
        else:
            return n

    def get_prev(self, next_value) -> Node:
        n = self.head
        while True:
            if n._next.value == next_value:
                return n
            else:
                if n._next is None:
                    break
                else:
                    n = n._next

    def insert(self, value, value_to_follow):
        node_to_follow = self.search(value_to_follow)
        n = Node(value, node_to_follow._next)
        node_to_follow._next = n

    def delete(self, value_to_delete):
        node_to_delete = self.search(value_to_delete)
        previous_node = self.get_prev(value_to_delete)
        previous_node._next = node_to_delete._next

    def __repr__(self):
        # l = []
        # n = self.head
        # while n.next:
        #     l.append(str(n.value))
        #     n = n.next
        return ' -> '.join((str(n) for n in self))

    def __iter__(self):
        n = self.head
        while n:
            yield n.value
            n = n._next


if __name__ == "__main__":
    n1 = Node(3)
    n2 = Node(7)
    n3 = Node(2)
    n4 = Node(9)

    ll = LinkedList()
    ll.head = n1

    n1._next = n2
    n2._next = n3
    n3._next = n4

    print(ll)

    ll.insert(5, 7)
    print(ll)
    ll.delete(5)
    print(ll)

    for el in ll:
        print(el)

