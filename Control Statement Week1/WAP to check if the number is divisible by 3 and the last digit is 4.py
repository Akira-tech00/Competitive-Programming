#3. WAP to check if the number is divisible by 3 and the last digit is 4.
user_input = int(input("Enter a Number: "))
if user_input % 3 ==0 and user_input % 10== 4:
    print("The Number is divisible by 3 and having 4 at its end")
else :
    print("The Number is not divisible by 3 and not having 4 at its end")