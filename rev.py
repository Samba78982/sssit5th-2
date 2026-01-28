'''write a program to  reverse number '''

n=int(input("enter a number:"))

rev=0

while n!=0:
    r=n%10
    r=(rev*10)+r
    n=n//10
    print(r,end='')   
