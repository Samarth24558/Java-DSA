#python programme search element in an array using binary search. BigO(log(n))

def binary_search(arr,s):
    low=0
    high=len(arr)-1
    mid=(low+high)//2
    
    f=0
    
    for i in range(len(arr)):
        if(arr[mid]==s):
            f=1
            break
            
        elif(arr[mid]<s):
            low=mid+1
            mid=(low+high)//2

        else:
            high=mid-1
            mid=(low+high)//2
            
    if f==0:
        print("Element not found")
    else:
        print("Element found at index:",mid)

arr=[2,4,8,16,32,64,128,256]
binary_search(arr,128)
        
        