#python programme to perform bubble sort

a=[5,4,3,4,-1,0,2,1]

for i in range(len(a)):
    for j in  range(len(a)-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]

print(a)