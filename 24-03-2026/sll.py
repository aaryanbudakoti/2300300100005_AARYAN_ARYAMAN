#  singly linked list
class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next

class SLL:
    def __init__(self, head = None):
        self.head=head

    def insert_at_end(self, info):
        temp = Node(info) # create a new node with the given info
        if self.head != None:
            t1 = self.head
            while t1.next != None:
                t1 = t1.next # traverse the list until the end is reached
            t1.next = temp # if the list is not empty, then the new node is added at the end of the list
        else:
            self.head = temp # if the list is empty, then the new node becomes the head

    def printLL(self):
        if self.head != None:
            t1=self.head
            while t1 != None:
                print(t1.data, end=' ')
                t1 = t1.next
            
            
    def insert_at_beginning(self, info):
        temp = Node(info) # create a new node with the given info
        if self.head != None:
            temp.next = self.head # if the list is not empty, then the new node is added at the beginning of the list
            self.head = temp
        else:
            self.head = temp # if the list is empty, then the new node becomes the head


    def insertInMiddle(self, info, loc):
        temp = Node(info) # create a new node with the given info
        if self.head != None:
            t1 = self.head
            count = 1
            while count < loc and t1.next != None:
                t1 = t1.next # traverse the list until the specified location is reached
                count += 1
            temp.next = t1.next # insert the new node at the specified location
            t1.next = temp
        else:
            self.head = temp # if the list is empty, then the new node becomes the head


            
s1 = SLL() # create an empty singly linked list
s1.insert_at_end(10) # insert 10 at the end of the list
s1.insert_at_end(120) 
s1.insert_at_end(30) 
s1.insert_at_beginning(5) # insert 5 at the beginning of the list
s1.printLL() # print the linked list