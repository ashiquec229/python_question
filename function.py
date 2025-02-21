
# sum of digit of a number using return function?

n=int(input("enter the number"))
def even(b):
    x = 0
    for i in range (2,b+1,2):
        x=x+i
    return x
obj=even(n)
print(obj)


# create list and find the largest element from the list(using function)

# def large(a):
#     largest=a[0]
#     i=1
#     while i<len(a):
#         if a[i]>largest:
#             largest=a[i]
#         i+=1
#     return largest
#
# b = [1, 2, 3, 40, 5]
# obj=large(b)
# print(obj)

# write a program to find  smallest number in a list
#
# def small(a):
#     smallest=a[0]
#     i=1
#     while i<len(a):
#         if a[i]<smallest:
#              smallest=a[i]
#         i+=1
#     return smallest
# b = [11, 2, 3, 40, 5]
# obj=small(b)
# print(obj)

# factorial of a number in python using return function

# def fact1(a):
#     fact=1
#     for i in range(1,a+1):
#         fact=fact*i
#     return fact
# num=int(input("enter a number:"))
# obj=fact1(num)
# print(obj)



