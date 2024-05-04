#python programme create circular double linked list

# python programme to create dobly linked list 

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.previos=None


class CDLL:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert_at_begin(self,value):
        new_node=Node(value)
        if(self.head is None):
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.previos=new_node
            self.head=new_node
            self.tail.next=self.head
    
    def insert_at_end(self,value):
        new_node=Node(value)
        if(self.head is None):
            self.head=new_node
            self.head.next=self.head
        else:
            cur=self.head
            while(cur.next and cur.next is not self.head):
                cur=cur.next
                
            cur.next=new_node
            new_node.previos=cur
            new_node.next=self.head
            self.tail=new_node
            
    def insert_at_position(self,value,index):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            cur=self.head
            pos=1
            while True:
                if(pos==index-1):
                    break
                cur=cur.next
                pos+=1
            
            t=cur.next
            cur.next=new_node
            new_node.previos=cur
            new_node.next=t
    
    def remove_head(self):
        self.head=self.head.next
        self.tail.next=self.head
    
    def remove_tail(self):
        cur=self.head
        
        while cur.next and cur.next is not self.head:
            prev=cur
            cur=cur.next
        prev.next=None
        self.tail=prev
        self.tail.next=self.head
    
    def remove_at_position(self,index):
        cur=self.head
        pos=1
        
        while True:
            if pos==index:
                break
            prev=cur
            cur=cur.next
            pos+=1
        
        prev.next=cur.next
    
    def update_head(self,value):
        self.head.value=value
    
    def update_tail(self,value):
        self.tail.value=value
    
    def update_at_position(self,value,index):
        cur=self.head
        pos=1
        
        while True:
            if pos==index:
                break
            cur=cur.next
            pos+=1

        cur.value=value

    def printll(self):
        cur=self.head
        
        while True:
            print(cur.value,end="<->")
            if(cur.next is self.head):
                break
            cur=cur.next
        print("Head")
        
        
        

if __name__=="__main__":
    ll=CDLL()
    ll.insert_at_end(10)
    ll.insert_at_end(90)
    ll.insert_at_end(20)
    ll.insert_at_begin(89)
    ll.insert_at_begin(800)
    ll.insert_at_position(20,3)
    ll.remove_head()
    ll.remove_tail()
    ll.remove_at_position(3)
    ll.update_tail(156)
    ll.update_head(120)
    ll.update_at_position(400,2)
    ll.printll()