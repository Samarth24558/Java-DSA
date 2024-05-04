# python programme to perform queue data struture using linked list
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self,size):
        self.head=None
        self.tail=None
        self.size=size
        self.currrent_size=0
    
    def enqueue(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.tail=self.head
            self.currrent_size+=1
        elif(self.currrent_size<self.size):
            self.tail.next=new_node
            self.tail=new_node
            self.currrent_size+=1
        else:
            print("Queue is full")
    
    def dequeue(self):
        if self.head==None:
            print("Queue is empty")        
        else:
            self.head=self.head.next
            self.currrent_size=-1
    
    def peek(self):
        print(self.tail.value)
    
    
    def print_queue(self):
        if self.head==None:
            print("Queue is empty")
        else:
            cur=self.head
            
            while cur:
                print("[",cur.value,"]",end='')
                cur=cur.next
    

if __name__ == "__main__":
   size=int(input("Enter the queue size: "))
   queue=Queue(size)
   while True:
        print("1.Enqueue\n2.Dequeue\n3.Dispaly queue\n4.Peek\n5.Exit")
        choice=int(input("Enter your choice:"))
        if choice<1 or choice>5:
            print("Invalid input")
        match choice:
            case 1:
                value=int(input("Enter the value: "))
                queue.enqueue(value)
            case 2:
                queue.dequeue()
            case 3:
                queue.print_queue()
            case  4:
                queue.peek()
            case 5:
                break
        print()
            
        
        

        