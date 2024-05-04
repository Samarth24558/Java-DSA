#python programme to stack data structure using linked list

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,size):
        self.head=None
        self.size=size
        self.stack_pointer=0
    
    def push(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
            self.stack_pointer+=1
        elif self.stack_pointer<self.size:
            new_node.next=self.head
            self.head=new_node
            self.stack_pointer+=1
        else:
            print("Stack size exeeded")
    
    def pop(self):
        if self.head==None:
            print("Stack is empty")
        else:
            self.head=self.head.next
            self.stack_pointer-=1
    
    def peek(self):
        if self.head==None:
            print("Stack is empty")
        else:
            print(self.head.value)
    
    def print_stack(self):
        if self.head==None:
            print("Stack is empty")
        else:
            cur=self.head
            while cur:
                print("[ ",cur.value," ]")
                cur=cur.next


if __name__=="__main__":
    stack_size=int(input("Enter the stack size: "))
    stack=Stack(stack_size)
    while True:
        print("1.Push\n2.Pop\n3.Dispaly stack\n4.Peek\n5.Exit")
        choice=int(input("Enter your choice:"))
        if choice<1 or choice>5:
            print("Invalid input")
        match choice:
            case 1:
                value=int(input("Enter the value: "))
                stack.push(value)
            case 2:
                stack.pop()
            case 3:
                stack.print_stack()
            case  4:
                stack.peek()
            case 5:
                break
        print()