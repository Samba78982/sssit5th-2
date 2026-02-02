def adamcheck(n):
    if n <= 0:
        return -1

    power = 0
    while n > 1:
        if n % 2 != 0:
            return -1
        n = n // 2
        power += 1

    return power


# calling the function
num = int(input("Enter a number: "))

result = adamcheck(num)

if result != -1:
    print(f"{num} = 2^{result}")
else:
    print(f"{num} is NOT a power of 2")
