# 10. WAP to accept a number from 1 to 7 and display the name of the day, like 1 for Sunday, 2 for Monday, etc.
name= int(input("Enter the Number(1-7) to display the Day: "))
if name==1:
    print("Sunday")
elif name==2:
    print("Monday")
elif name==3:
    print("Tuesday")
elif name==4:
    print("Wednesday")
elif name==5:
    print("Thursday")
elif name==6:
    print("Friday")
elif name==7:
    print("Saturday")
else:
    print("Enter a valid number")