#3
class Node():
    def __init__(self, value):
        self.value = value
        self.next: Node = None
    
class LinkedList():
    def __init__(self):
        self.head: Node = None
    
    def append_patient(self, value):
        if not self.head:
            self.head = Node(value)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)

#custom task
    def insert(self, idx, value):
        pass

    def remove_patient(self, value):
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
        
        current = self.head
        while current.next.value != value and current.next:
            current = current.next

        if not current.next:
            return

        nn = current.next.next
        del current.next
        current.next = nn
#4
    def reverse_playlist(self):
        current = self.head
        prev = None

        while current:
            next = current.next
            current.next = prev

            prev = current
            current = next
        self.head = prev