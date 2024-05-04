#python programme to search element using linear search. BigO(n)
    
def search(len_arr):
    data=[]
    for i in range(len_arr):
        value=int(input(f"Enter the element{i+1}: "))
        data.append(value)            
    print(data)
    ind=0
    val=int(input("Enter the search element: "))
 
    for i in range(len(data)):
        if(data[i]==val):
            ind=1
            index=i
            break
    
    
    if(ind==0):
        print("Element not found")
    else:
        print(f"Element found at index {index} ")


l=int(input("Enter the length of array:"))
search(l)
