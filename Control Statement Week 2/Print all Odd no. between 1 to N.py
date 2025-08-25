# Write a program to print all odd numbers from 1 to N, where you have to take N as input
# from user

N = int(input("Enter N: "))
i = 1
while i <= N:
    print(i, end=" ")
    i += 2
print()