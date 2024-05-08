class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, "-->", end=' ')
            current = current.next
        print("None")

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def insert_at_pos(self, pos, data):
        if pos <= 0:
            print("Invalid position")
            return
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        previous = None
        temp = 1
        while current and temp < pos:
            previous = current
            current = current.next
            temp += 1
        if not current:
            print("Position out of range")
            return
        previous.next = new_node
        new_node.next = current


LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.display()
LL.insert(20)
LL.insert(39)
LL.display()
LL.delete(39)
LL.display()
print("Searching for value 3:", LL.search(3))
print("Searching for value 5:", LL.search(5))
print("Searching for value 1:", LL.search(1))
LL.insert_at_pos(1, 9)
LL.insert_at_pos(2, 9)
LL.insert_at_pos(4, 19)
LL.insert_at_pos(7, 17)
LL.display()
