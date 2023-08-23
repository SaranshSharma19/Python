class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    # Inserting at front
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    
    # Inserting after a given node
    def insertafter(self,prev_node,new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    
    # Inserting at the end
    def append(self,new_data):
        new_node=Node(new_data)

        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last = last.next
        
        last.next = new_node
        
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
    
if __name__ == '__main__':
    llist=LinkedList()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    llist.head.next=second
    second.next=third

    llist.push(0)
    # llist.printlist()

    llist.insertafter(llist.head.next, 8)
    # llist.printlist()

    llist.append(4)
    # llist.printlist()
