# 7. Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle).
a= int(input("Enter the Fisrt Angle: "))
b= int(input("Enter the Second Angle: "))
c= int(input("Enter the Third Angle: "))
if a+b+c==180:
    print("The Sum of all angles is 180, hence")
    if a==90 or b==90 or c==90:
        print("This is a Right Triangle")
    elif a>90 or b>90 or c>90:
        print("This is a Obtuse Triangle")
    else:
        print("This is a Acute Triangle")
else:
    print("Entered Invalid Angles ")
