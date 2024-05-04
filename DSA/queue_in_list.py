# python program to implement queue in list

class Queue:
    def __init__(self) -> None:
        self.queue:list[int]=[]
    
    def enqueue(self,value:int)->None:
        self.queue.append(value)
    
    def dequeue(self)->None:
        del self.queue[0]
    
    def print_queue(self)->None:
        print(self.queue)

if __name__=="__main__":
    queue=Queue()
    while True:
        print("1.Insert value\n2.Remove value\n3.Display queue\n4.Exit")
        choice=int(input("Enter your choice: "))
        if(choice<1 or choice>4):
            print()
            print("---Invalid input---")
            print()
        else:
            match choice:
                case 1:
                    value=int(input("Enter the value: "))
                    queue.enqueue(value)
                case 2:
                    queue.dequeue()
                case 3:
                    queue.print_queue()
                case 4:
                    break
        
    
        