age = int(input())
day = input().lower().strip()
student = input().lower().strip()


if age<0 or age>120:
    print("Invalid age")
else:
    if age<3:
        price=0
    elif age<13:
        price=50
    elif age<60:
        price=120
    else:
        price=70
    if day in ["saturday","sunday"]:
        price*=1.2
    
    if student == "yes" and 13<=age<=25:
        price*=0.75
    
    print(f"Price: {price:.2f}")


    
