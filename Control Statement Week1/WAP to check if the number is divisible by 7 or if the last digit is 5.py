#4. WAP to check if the number is divisible by 7 or if the last digit is 5.
user_input = int(input("Enter a Number: "))
if user_input % 7 ==0 or user_input % 10== 5:
    print("The Number is divisible by 7 and having 5 at its end")
else :
    print("The Number is not divisible by 7 and not having 5 at its end")