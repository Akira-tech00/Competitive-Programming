#5. Take an integer A as input. You have to tell whether A is divisible by both 5 and 11 or not.
user_input=int(input("Enter a Number: "))
if user_input % 5==0 and user_input % 11==0:
    print("This number is Divisible by 5 and 11")
else:
     print("This number is not Divisible by 5 and 11")
