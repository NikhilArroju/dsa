class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


linked_list = LinkedList()

linked_list.head = Node(1)

second = Node(2)
third = Node(3)

linked_list.head.next = second
second.next = third

while linked_list.head != None:
    print(linked_list.head.item, end=" ")
    linked_list.head = linked_list.head.next
