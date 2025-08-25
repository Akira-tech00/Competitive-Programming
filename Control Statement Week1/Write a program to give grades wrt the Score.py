#15. Accept the percentage from the user and display the grade according to the following criteria.
# ● Below 25 – D
# ● 25 to 45 – C
# ● 45 to 65 – B
# ● 65 to 85 – A
# ● Above 85 – A+
percentage= int(input("Enter your Percentage: "))
if percentage<25:
    print("You get D")
elif 25<percentage<45:
    print("You get C")
elif 45<percentage<65:
    print("You get B")
elif 65<percentage<85:
    print("You get A")
else:
    print("You get A+")
