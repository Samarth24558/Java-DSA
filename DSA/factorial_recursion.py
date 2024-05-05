#python program find factorial of number using recursion

def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)


num=int(input("Enter the number: "))
res=factorial(num)
print(res)