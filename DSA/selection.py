#python programme to perform selection sort

a=[5,4,3,2,1]

for i in range(len(a)):
    min=i
    for j in range(i+1,len(a)):
        if(a[min]>a[j]):
            min=j
    a[i],a[min]=a[min],a[i]

print(a)