
"""
age=int(input())

day=input().strip().upper()


student=input().strip().upper()

if age<0 or age>120:
    print("Invalid age")

else:
    if age < 3:
        price = 0
    elif 3<=age<13:
        price = 50
    elif 13<=age<60:
        price = 120
    else:
        price = 70

    if day in ["SATURDAY","SUNDAY"]:
        price*=1.2

    if student == "YES" and 13<=age<26:
        price*=0.75

    print(f"Price: {price:.2f}")

    
"""


"""
sides = [int(x) for x in input().split()]

sorted_sides = sorted(sides)


sides = [int(x) for x in input().split()]
sorted_sides=sorted(sides)


sides =sorted(map(int,input().split()))
x,y,z=sides

sides=sorted(map(int,input()))
x,y,z =sides


sides = input().split()
x=[int(sides[0],int(sides[1]),int(sides[2]))]
x.sort()


sides=input().split()
x=[int(sides[0]),int(sides[1]),int(sides[2])]
x.sort()

"""
"""

sides=sorted(map(int,input().split()))
x,y,z=sides

if x<=0 or x+y<=z :
    print("Invalid")

else:
    if x==y==z:
        show ="Equilateral"
    elif x==y or y==z:
        show ="Isosceles"
    else:
        show ="Scalene"

    if x**2 + y**2 == z**2:
        angle="Right"
    elif x**2 + y**2 > z**2:
        angle="Acute"
    else:
        angle="Obtuse"

    print(f"{show} {angle}")

"""


"""
a = 7
b = 2
# print(a / b, a // b, a % b, -a // b, -a % b)

# print(2 + 3 * 4 ** 2 // 5 % 3)

# print(type(a / b), type(a // b), type(True + 1), type(3 * "ab"))

# print("5" + "5", "5" * 3, int("5") + 5)

# print(bool(0), bool("0"), bool([]), bool(" "), bool(None))

# print(10 > 5 > 2, 1 < 2 < 2, not 1 == 2 or 3)

x = "Py"
y = x
x += "thon"
print(x, y)


"""



"""
number=int(input())

x=abs(number)

digit=0
summ=0
rev=0
y=0



if number == 0:
    digit = 1
else:
    while x>0:
        y=x % 10
        digit +=1
        summ += y
        rev = rev*10 + y
        x = x // 10

if number<0:
    rev = -rev

if rev == number:
    plaindrome ="yes"
else:
    plaindrome="no"

print(f"Digit:{digit:}\nSum:{summ:}\nReversed:{rev:}\nPlaindrome:{plaindrome:}")


"""

bill =float(input())
tip_per=float(input())
people=int(input())

if bill<0 or tip_per<0 or people<1:
    print("Invalid Input")

else:
    tip_per = bill * tip_per / 100
    total = bill + tip_per
    each_pays=total/people
    if each_pays>int(each_pays):
        each_pays=int(each_pays)+1

    collected =each_pays*people
    surplus = collected - total

    print(f"Total with tip:{total:.2f}\nEach pays:{each_pays:.2f}\nCollected:  {collected:.2f}\nSurplus:{surplus:.2f}")


















