# python programme to create circular linked list in python

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class CLL:
    def __init__(self):
        self.head=None
        
    def insert_at_end(self,value):
        new_node=Node(value)
        
        if self.head==None:
            self.head=new_node
            self.head.next=self.head
        else:
            cur=self.head
            while cur.next is not self.head:
                cur=cur.next
            cur.next=new_node
            new_node.next=self.head
    
    def insert_at_begin(self,value):
        new_node=Node(value)
        
        if self.head is None:
            self.head=new_node
            self.head.next=self.head
        
        else:
            cur=self.head
            while cur.next is not self.head:
                cur=cur.next
            new_node.next=self.head
            self.head=new_node
            cur.next=self.head
    
    def insert_at_position(self,value,index):
        new_node=Node(value)
        cur=self.head
        pos=1
        while True:
            if pos==index-1:
                break
            pos+=1
            cur=cur.next
        
        t=cur.next
        cur.next=new_node
        new_node.next=t
    
    def remove_head(self):
        cur=self.head
        
        while cur.next is not self.head:
            cur=cur.next
        
        self.head=self.head.next
        cur.next=self.head
    
    def remove_tail(self):
        cur=self.head
        
        while cur.next is not self.head:
            prev=cur
            cur=cur.next
        prev.next=self.head
    
    def remove_at_position(self,index):
        cur=self.head
        pos=1
        
        
        while True:
            if pos==index:
                break
            pos+=1
            prev=cur
            cur=cur.next
        
        prev.next=cur.next
    
    
    def update_head(self,value):
        self.head.value=value
    
    def update_tail(self,value):
        cur=self.head
        
        while cur.next is not self.head:
            cur=cur.next
        
        cur.value=value
    
    def update_at_position(self,index,value):
        cur=self.head
        pos=1
        
        while True:
            if pos==index:
                break
            pos+=1
            cur=cur.next
            
        cur.value=value
 
        
    def printll(self):
        cur=self.head
        
        while True:
            print(cur.value,end="->")
            if cur.next is self.head:
                break
            cur=cur.next
    
        print("Head")

if __name__=="__main__": 
    ll=CLL()
    ll.insert_at_end(10)
    ll.insert_at_end(80)
    ll.insert_at_end(100)
    ll.insert_at_begin(300)
    ll.insert_at_position(70,3)
    ll.remove_at_position(2)
    ll.update_at_position(2,103)
    ll.printll()
