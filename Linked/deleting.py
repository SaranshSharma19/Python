from asyncio.windows_events import NULL
from django.forms import NullBooleanField


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
    
    # Deleting node from the begining
    def delet_begin(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head=self.head.next
    
    # Deletiing node from the end
    def delet_end(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            # temp.next=temp.next.next
            temp.next=None
    
    # Deletiing node from the middle (delet by value)
    def delet_by_value(self,x):
        if self.head is None:
            print("Linked List is Empty")
        if x==self.head.data:
            self.head=self.head.next
        temp=self.head
        while temp.next is not None:
            if x==temp.next.data:
                break
            temp=temp.next
        if temp.next is None:
            print("Node is not present in the linked list")
        else:
            temp.next=temp.next.next

if __name__=="__main__":
    llist=LinkedList()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    fourth=Node(4)
    fifth=Node(5)
    llist.head.next=second
    second.next=third
    third.next=fourth
    fourth.next=fifth
    
    llist.push(0)
    llist.printlist()
    print(end="\n")

    llist.delet_begin()
    llist.printlist()
    print(end="\n")

    llist.delet_end()
    llist.printlist()
    print(end="\n")

    llist.delet_by_value(3)
    llist.printlist()

