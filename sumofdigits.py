def sum_of_digits(n):
    total=0
    while(n>0):
        digit=n%10
        total=total+digit
        n=n//10
    return total

x=int(input("number:"))
c=sum_of_digits(x)
print("sum of digits=",c)
