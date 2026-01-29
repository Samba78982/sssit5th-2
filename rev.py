'''write a program to  reverse number '''

def reverse(num):
    rev=0
    while num>0:
        rev =rev*10+num%10
        num//=10
    return rev

def isPalidrome(num):
    return num==reverse(num)

print(reverse(1235))
print(isPalidrome(1239))
print(reverse(121))
print(isPalidrome(121))

print("samba")
