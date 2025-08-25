#Read N, Print the sum of digits in N
N=int(input("Enter a number: "))
sum=0 
while(N>0):
    digit= N % 10
    N= N//10
    sum += digit
print(sum)