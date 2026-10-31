"""

1 no ques:

age = int(input())
day = input().lower().strip()
student = input().strip()

if 0>age or age>120:
    print("Invalid age")

else:
    if age<3:
        price = 0
    elif 3<=age<=12:
        price = 50
    elif 13<=age<=59:
        price = 120
    else:
        price = 70


   

    if student=="yes" and 13<=age<=25:
        price*=0.75    
            

    if day in ["saturday","sunday"]:
        price*=1.2

    print(f"Price:{price: .2f}")


"""
"""

# ques 2:

sides = sorted(map(int,input().split()))

x , y ,z =sides

if x<=0 or x+y<=z:
    print("Invalid")

else:
    if x==y==z:
        sides_l="Eqilateral"
    elif x==y or y==z:
        sides_l="Isosceles"
    else:
        sides_l ="Scalare"

    if x**2 + y**2 == z**2:
        angle ="Right"
    elif x**2 + y**2 > z**2:
        angle ="Acute"
    elif x**2 + y**2 < z**2:
        angle ="Obtuse"

    print(f"{sides_l} {angle}")

"""


# ques 4

number = int(input())
x = abs(number)

digit=0
total=0
reversed=0
y=0

if number == 0:
    digit = 1

else:
    while x > 0:
        y = x % 10
        total +=y
        reversed = reversed*10 +y
        digit +=1
        x == x // 10

if number<0:
    reversed=-reversed

if x == reversed:
    print="Palindrome"
else:
    print="No Palindrome"

print(f"{digit},{total},{reversed}")


