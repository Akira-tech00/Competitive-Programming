# Read N, print No of digits of N.
N=int(input("Enter the value of N: "))
digit=0
while (N>0):
    N=N//10
    digit =digit+1
print(digit)