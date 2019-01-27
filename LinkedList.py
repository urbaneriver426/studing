class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        arr = []
        while node is not None:
            if node.value == val:
                arr.append(node)
                node = node.next
            else:
                node = node.next
        return arr

    def delete(self, val, all=False):
        current = self.head
        previous = None
        if all==False:
            while current is not None:
                if current.value == val:
                    if previous is not None:
                        previous.next = current.next
                    else:
                        self.head = current.next
                        return True
                else:
                    previous = current
                    current = current.next
            return False
        else:
            while current is not None:
                if current.value == val:
                    if previous is not None:
                        previous.next = current.next
                        current = current.next
                    else:
                        self.head = current.next
                        current = current.next
                else:
                    previous = current
                    current = current.next
            return True


    def clean(self):
        node = self.head
        node.value = None
        node.next = None


    def len(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def insert(self, afterNode, newNode):
        newNode.next = afterNode.next
        afterNode.next = newNode
