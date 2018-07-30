
l=[]
def factors(a):
        for i in range(1,a+1):
               if(a%i==0):
                   l.append(i)
        return l
               
num=int(input("number:"))                 
c=factors(num)

print("factors:",c)
