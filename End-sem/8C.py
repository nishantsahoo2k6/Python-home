n = int(input("Enter range: "))
def digit_sum(i):
    total=0
    order = len(str(i))
    t = i
    while(t>0):
        d=t%10
        t=t-d
        total = total+(d**order)
        t=t//10
    return total

for i in range(n+1):
    if(digit_sum(i)==i):
        print(i, end=" ")
