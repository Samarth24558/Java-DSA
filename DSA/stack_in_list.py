#python programme to perform stack datastructure using list

class Stack:
    def __init__(self,size):
        self.stack=[]
        self.stack_pointer=-1
        self.size=size
    
    def push(self,value):
        if self.stack_pointer==self.size-1:
            print("Stack is full")
        else:
            self.stack.append(value)
            self.stack_pointer+=1
    
    def print_stack(self):
        for i in range(len(self.stack)-1,-1,-1):
            print("[",end=" ")
            print(self.stack[i],end=" ")
            print("]")
        print(f"Used size: {self.stack_pointer+1}/{self.size} ")
    
    def delete(self):
        if self.stack_pointer==-1:
            print("Stack is empty")
        else:
            self.stack.pop()
            self.stack_pointer-=1
    
    def peek(self):
        if self.stack_pointer==-1:
            print("Stack is empty")
        else:
            print(self.stack[-1])
        
            
            
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
                stack.delete()
            case 3:
                stack.print_stack()
            case  4:
                stack.peek()
            case 5:
                break
        print()