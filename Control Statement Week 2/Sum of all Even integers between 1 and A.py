# You are given an integer A, you need to find and return the sum of all the even numbers
# between 1 and A. Even numbers are those numbers that are divisible by 2.

A = int(input("Enter A: "))
i = 2
total = 0
while i <= A:
    total += i
    i += 2
print("Sum of even numbers =", total)