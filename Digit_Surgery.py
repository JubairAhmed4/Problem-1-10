Number = (int(input()))
n=abs(Number)
digit=0
total_sum=0
reversed=0
d=0
if Number==0:
    digit=1
else:
    while n>0:
        d= n % 10
        digit+=1
        total_sum+=d
        reversed=reversed*10+d
        n = n // 10
if Number<0:
    reversed = -reversed

if Number == reversed:
    plaindrome = "Yes"
else:
    plaindrome = "No"

print(f"Digits: {digit}\nSum: {total_sum}\nReversed: {reversed}\nPlandrome: {plaindrome}")

        

    

