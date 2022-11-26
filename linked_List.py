class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            while self.head:
                print(self.head.data)
                self.head = self.head.next

    def begin(self, new_element):
        new_element = Node(new_element)
        new_element.next = self.head
        self.head = new_element

    def end(self, data):
        new_element = Node(data)
        if not self.head:
            self.head = new_element
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_element

    def after_pos(self, data1, position):
        n = self.head
        while n is not None:
            if n.data == data1:
                break
            n = n.next
        if n is None:
            print("item is not present in the list")
        else:
            node = Node(data1)
            node.next = n.next
            n.next = node

    def bef_pos(self, data, position):
        node = Node(data)
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == data:
            node.next = self.head
            self.head = node
            return
        n = self.head
        while n.next is not None:
            if n.next.data == data:
                break
            n = n.next
            if n.next is None:
                print("position not found")
            else:
                node.next = n.next
                n.next = node

    def del_begin(self):
        if self.head is None:
            print("No items to delete from list")
        else:
            self.head = self.head.next

    def del_end(self):
        if self.head is None:
            print("No items to delete from list")
        else:
            n = self.head
            while n.next.next:
                n = n.next
            n.next = None

    def del_Middle(self, del_val):
        if self.head is None:
            print("Linked List is empty You can't perform any deletion task")
        else:
            n = self.head
            if n.data == del_val:
                self.head = self.head.next
            else:
                while n.next:
                    if n.next.data == del_val:
                        break
                    n = n.next
                n.next = n.next.next


l = LL()

l.begin(40)
l.del_end()

l.print_LL()
