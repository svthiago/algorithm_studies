class Node():
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.lenght = 0

    def insert(self, value, index=0):
        if (index < 0) or (index > self.lenght):
            raise Exception("Index out of range")

        itr = self.head
        pos = 0
        while True:
            if index == 0:
                aux = self.head
                self.head = Node(value)
                self.head.next = aux
                self.lenght += 1
                break
            if pos == (index - 1):
                aux = itr.next
                itr.next = Node(value)
                itr.next.next = aux
                self.lenght += 1
                break

            itr = itr.next
            pos += 1


    def delete(self, index=0):
        if (index < 0) or (index > self.lenght):
            raise Exception("Index out of range")


        itr = self.head
        pos = 0
        while True:
            if index == 0:
                self.head = self.head.next
                self.length -= 1
                break
            
            if pos == (index - 1):
                itr.next = itr.next.next
                break         

            itr = itr.next
            pos += 1

    def print_elements(self):
        iter = self.head
        s = ""

        while iter:
            s += f"{iter.data}-->"
            iter = iter.next

        print(s)
