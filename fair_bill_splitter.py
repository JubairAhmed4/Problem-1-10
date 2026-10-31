bill = float(input())
tip=float(input())
people=int(input())

if bill<0 or tip<0 or people<1:
    print("Invalid input")

else:
    tip_ammount= bill*tip/100
    total = bill+tip_ammount
    each_pay =total / people
    if each_pay>int(each_pay):
        each_pay=int(each_pay)+1
    collected =each_pay*people
    surplus = collected -total

print(f"Total with tip:{total: .2f}\nEach pays:{each_pay}\nCollected:{collected: .2f}\nSurplus:{surplus: .2f}")






