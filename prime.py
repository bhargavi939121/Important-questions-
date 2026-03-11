def find(num):
    if num == 2:
        print("prime")
    if num < 1:
        print("not prime")
    flag=False
    for i in range(2,num):
        if num % i==0:
            flag=True
            break
    if flag:
        return f"{num} is not prime"
    else:
        return f"{num} is prime"
res=find(int(input("enter number")))
print(res)