triangle =input().split()
sides =[int(triangle[0]),int(triangle[1]),int(triangle[2])]
sides.sort()

if sides[0]<=0 or sides[0]+sides[1]<=sides[2]:
    print("Invalid")
else:
    if sides[0]==sides[1]==sides[2]:
        sides_type="Equilateral"
    elif sides[0]==sides[1] or sides[1]==sides[2]:
        sides_type="Isosceles"
    else:
        sides_type="Scalene"

    if sides[0]*sides[0]+sides[1]*sides[1]==sides[2]*sides[2]:
        sides_angle="Right"
    elif sides[0]*sides[0]+sides[1]*sides[1]>sides[2]*sides[2]:
        sides_angle="Acute"
    else:
        sides_angle="Obtuse"

    print(f"{sides_type} {sides_angle}")



sides=sorted(map(int,input().split()))
x,y,z=sides

if x<=0 or x+y <= z:
    print("Invalid")
else:
    if x==y==z:
        sides_type="Equilateral"
    elif x==y or y==z:
        sides_type="Isosceles"
    else:
        sides_type="Scalene"

    if x**2+y**2==z**2:
        sides_angle="Right"
    elif x**2 + y**2>z**2:
        sides_angle="Acute"
    else:
        sides_angle="Obtuse"

    print(f"{sides_type} {sides_angle}")

