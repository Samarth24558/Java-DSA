# python program to perform priority queue in list
class Priority_Queue:
    def __init__(self):        
        self.queue=[]
        self.priority=[]
        self.size=-1
        
    def enqueue(self,value,priority):
        self.queue.append(value)
        self.priority.append(priority)
        
    def dequeue(self):
        if self.queue==[]:
            print("Queue is empty")
        else:
            self.queue.pop(0)
            self.priority.pop(0)
    
    def peek(self):
        for i in range(len(self.queue)):
            for j in range(len(self.queue)-1):
                if self.priority[j]<self.priority[j+1]:
                    self.queue[j],self.queue[j+1]=self.queue[j+1],self.queue[j]
                    self.priority[j],self.priority[j+1]=self.priority[j+1],self.priority[j]

        print("["+self.queue[0]+"]")

    def print_queue(self):
        for i in range(len(self.queue)):
            for j in range(len(self.queue)-1):
                if self.priority[j]<self.priority[j+1]:
                    self.queue[j],self.queue[j+1]=self.queue[j+1],self.queue[j]
                    self.priority[j],self.priority[j+1]=self.priority[j+1],self.priority[j]
        print(self.queue)
        
        
if __name__=="__main__":
    queue=Priority_Queue()
    print("1.Enqueue \n2.Dequeue \n3.Print queue \n4.Peek \n5.Exit")
    while True:
        choice=int(input("Enter your choice: "))
        if choice<1 or choice>5:
            print("Invalid input")
        else:
            match choice:
                case 1:
                    value=int(input("Entre the value"))
                    priority=int(input("Enter the priority: "))
                    queue.enqueue(value,priority)
                case 2:
                    queue.dequeue()
                case 3:
                    queue.print_queue()
                case 4:
                    queue.peek()
                case 5:
                    break                  
    
    

        

    