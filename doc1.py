# 1.Write a program to calculate sum of the digits of a number using functions.
def Sum(n):
    sum=0
    while (n!=0):
        sum = sum+int(n%10)
        n = int(n/10)
    return sum
n=int(input("Enter the numbers:-"))
print(Sum(n))



