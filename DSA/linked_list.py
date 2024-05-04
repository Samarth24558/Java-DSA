#python programme to create linked list 

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class LL:
    def __init__(self):
        self.head=None
    
    def insert_at_end(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            cur=self.head
            
            while(cur.next is not None):
                cur=cur.next
            cur.next=new_node
    
    def insert_at_begin(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            prev=self.head
            new_node.next=prev
            self.head=new_node
            
                        
                
    def insert_node_at_position(self,value,position):
        new_node=Node(value)
        cur=self.head
        pos=1
        while cur.next is not None:
            if(pos==position-1):
                break
            cur=cur.next
            pos+=1
        
        t=cur.next
        cur.next=new_node
        new_node.next=t
            
    def remove_head(self):
        self.head=self.head.next
    
    def remove_tail(self):
        cur=self.head
        
        while cur.next:
            prev=cur
            cur=cur.next
        prev.next=None
    
    def remove_at_index(self,index):
        cur=self.head
        i=1
        while cur.next:
            if(i==index):
                break
            i+=1
            prev=cur
            cur=cur.next
        prev.next=cur.next    
    
    def update_head(self,value):
        self.head.value=value
        
    def update_tail(self,value):
        cur=self.head
        
        while cur.next:
            cur=cur.next
        cur.value=value
    
    def update_at_position(self,value,index):
        cur=self.head
        pos=1
        
        while cur:
            if(pos==index):
                break
            cur=cur.next
            pos+=1
        cur.value=value
    
    def size(self):
       cur=self.head
       size=0
       while cur is not None:
            size+=1
            cur=cur.next
       print("Size of linked list is:",size)
            
    def printll(self):
        cur=self.head
        
        while(cur is not None):
            print(cur.value,end="->")
            cur=cur.next
        print("None")
    

if __name__=="__main__":                
    ll=LL()
    ll.insert_at_end(100)
    ll.insert_at_end(90)
    ll.insert_at_end(40)
    ll.insert_at_end(500)
    ll.size()
    ll.printll()    