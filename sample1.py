def calculate_sum(exp):
    total=0
    for item in exp:
        total=total+item
    return total

l1=[100,200,300]
l2=[200,400,600]

l1_sum=calculate_sum(l1)
l2_sum=calculate_sum(l2)

print("first list sum=",l1_sum)
print("second list sum=",l2_sum)
    
