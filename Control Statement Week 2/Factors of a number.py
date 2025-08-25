# Print all the Factors/Divisors of a given +ve number.
no=int(input("Enter a Number: "))
i=1
while(i<=no):
    if(no % i ==0):
        print(i)
    i+=1