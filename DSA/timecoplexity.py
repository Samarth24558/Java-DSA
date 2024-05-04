#python programme to calculate time complixity of a programme with a graph
import matplotlib.pyplot as plt
from datetime import datetime


def search(data,val):
    for i in range(len(data)):
        if(data[i]==val):
            ind=1
            index=i
            break
    
    
    if(ind==0):
        print("Element not found")
    else:
        print(f"Element found at index {index} ")

arr1=[]
arr2=[]
arr3=[]

for i in range(1000):
    arr1.append(i)

for i in range(2000):
    arr2.append(i)
    
for i in range(3000):
    arr3.append(i)

start_time=datetime.now()
search(arr1,900)
end_time=datetime.now()
tm1=(end_time-start_time).total_seconds()


start_time=datetime.now()
search(arr2,1000)
end_time=datetime.now()
tm2=(end_time-start_time).total_seconds()

start_time=datetime.now()
search(arr3,2900)
end_time=datetime.now()
tm3=(end_time-start_time).total_seconds()


x=["1000(900)","2000(1000)","3000(2900)"]
y=[tm1,tm2,tm3]

plt.bar(x,y)
plt.show()