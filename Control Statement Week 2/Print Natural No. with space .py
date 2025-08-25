# Write a program that takes a positive integer N as input from the user and prints all natural numbers
# numbers from 1 to N, with each number followed by a space.
N = int(input("Enter N: "))
i = 1
while i <= N:
    print(i, end=" ")
    i += 1
print()