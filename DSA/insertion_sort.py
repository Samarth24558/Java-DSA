#python programme to sort an array using insertion sort

arr=[3,2,1,4,5,90,0]
f=0
for i in range(1,len(arr)):
    t=arr[i]
    for j in range(i,0,-1):
        if(t<arr[j-1]):
            f=1
            arr[j]=arr[j-1]
        
            
    if(f!=0):
        arr[j-1]=t
        f=0

print(arr)