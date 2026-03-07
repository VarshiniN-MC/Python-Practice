#Quadratic equation roots
import math
a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
c=int(input("Enter the value of c :"))
d=(b*b)-4*a*c
sq= math.sqrt(abs(d))
if d>0 :
    print("The roots are real and distinct")
    r1=(-b+sq)/(2*a)
    r2=(-b-sq)/(2*a)
    print("root1 =",r1,"root2 =",r2)
elif d==0 :
    print("The roots are real and equal")
    r= -b/(2*a)
    print("The root = ",r)
else :
    real= -b/(2*a)
    im= d/(2*a)
    print("The roots are imaginary")
    print("root1 =",real,"+i",im)
    print("root2 =",real,"-i",im)
