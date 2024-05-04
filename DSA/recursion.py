# python program to perform recursion
def sum(num):
    if num==0:
        return num
    else:
        return num+sum(num-1)

print(sum(5))