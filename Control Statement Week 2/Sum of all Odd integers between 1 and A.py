# Sum of all integers between 1 and A which are divisible  by 2

A = int(input("Enter A: "))
i = 1
total = 0
while i <= A:
    total += i
    i += 2
print("Sum of odd numbers =", total)