#6. Read three integers and print their maximum.
a =int(input("Enter First Number: "))
b =int(input("Enter Second Number: "))
c =int(input("Enter Third Number: 3"))
 
if a>b and a>c:
    print(a)
elif b>c:
    print(b) 
else: 
    print(c)