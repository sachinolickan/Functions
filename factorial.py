def factorial(a):
    result=1
    for a in range(a,1,-1):
        result=result*a
    return result

num=int(input("number:"))
c=factorial(num)

print("factorial=",c)
