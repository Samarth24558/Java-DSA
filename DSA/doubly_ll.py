# python programme to create dobly linked list 

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.previos=None


class DLL:
    def __init__(self):
        self.head=None
    
    def insert_at_begin(self,value):
        new_node=Node(value)
        if(self.head is None):
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previos=new_node
            self.head=new_node
    
    def insert_at_end(self,value):
        new_node=Node(value)
        if(self.head is None):
            self.head=new_node
        else:
            cur=self.head
            while(cur.next):
                cur=cur.next
                
            cur.next=new_node
            new_node.previos=cur
            
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
    
    def remove_tail(self):
        cur=self.head
        
        while cur.next:
            prev=cur
            cur=cur.next
        prev.next=None
    
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
        cur=self.head
        
        while cur.next:
            cur=cur.next
        
        cur.value=value
    
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
        
        while(cur):
            print(cur.value,end="<->")
            cur=cur.next
        print("None")
        
        
        

if __name__=="__main__":
    ll=DLL()
    ll.insert_at_begin(100)
    ll.insert_at_begin(90)
    ll.insert_at_begin(200)
    ll.insert_at_position(40,3)
    ll.insert_at_end(50)
    ll.remove_at_position(3)
    ll.update_head(500)
    ll.update_tail(1000)
    ll.update_at_position(850,3)
    ll.printll()