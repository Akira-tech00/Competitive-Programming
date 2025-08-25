#12. You are given 3 integer angles(in degrees), A, B, and C, of a triangle. You have to tell
# whether the triangle is valid or not. A triangle is valid if the sum of its angles equals 180.
a= int(input("Enter the Fisrt Angle: "))
b= int(input("Enter the Second Angle: "))
c= int(input("Enter the Third Angle: "))
if a+b+c==180:
    print("The sum of angles is 180, hence Valid Triangle")
else:
    print("Entered Invalid angles, not a Valid Triangle")