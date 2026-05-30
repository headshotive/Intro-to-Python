a=int(input("enter an value:"))
b=int(input("enter an value 2:"))
c=int(input("enter an value 3:"))

avg=(a+b+c/3)
print("avg=",avg)

if avg>a and avg>b and avg>c:
    print("%d is higher %d,%d,%d"%(avg,a,b,c))
elif avg>a and avg>b:
    print("%d is higher %d,%d"%(avg,a and c))
elif avg>a and avg>c:
    print("%d is higher %d,%d"%(avg,a and c))
elif avg>b and avg>c:
    print("%d is higher %d,%d"%(avg,b and c))
elif avg>a:
    print("%d is just higher %d"%(avg,a))
elif avg>b:
    print("%d is just higher %d"%(avg,b))
elif avg>c:
    print("%d is just higher %d"%(avg,c))
else:
    print("Invalid Input")