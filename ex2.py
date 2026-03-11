# Check if a number is an Armstrong number or not
def find(n):
    power=len(str(n))
    sum1=0
    num=n
    while num > 0:
        rem=num % 10
        sum1=sum1 + rem **power
        num=num // 10
    return n==sum1
if find(int(input("enter number"))):
    print("Armstrong number:")
else:
    print("Not an armstrong number")