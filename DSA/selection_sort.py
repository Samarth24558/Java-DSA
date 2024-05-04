a=[]
l=int(input("Enter the length of array: "))

for i in range(l):
    value=int(input("Enter the element:"))
    a.append(value)

print(a)

f=0
l=len(a)-1
for j in range(len(a)):
    for i in range(l):
        if(a[i]>a[i+1]):
            f=1
            k=i+1
    if(f==1):
        a[j],a[k]=a[k],a[j]
        l=l-1
        f=0
print(a)