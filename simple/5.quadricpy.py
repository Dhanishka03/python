import math
a=int(input("Enter co eff of a :"))
b=int(input("Enter co eff of b :"))
c=int(input("Enter co eff of c :"))
if a==0:
    print("Given input is not an quadratic equation ")
else:
    discriminant=b**2-4*a*c
    if discriminant>0:
        root1=(-b+math.sqrt(discriminant))/(2*a)
        root2=(-b-math.sqrt(discriminant))/(2*a)
        print("Two distinct real roots:%2f"%(root1,root2))
    elif discriminant==0:
        root=-b/(2*a)
        print("One real root :%2f"%root)
    else :
        real_part=-b/(2*a)
        imaginary_part=math.sqrt(-discriminant)/(2*a)
        print("Two complex roots:%.2f + %.2fi and %.2f - %.2fi" %(real_part,imaginary_part,real_part,imaginary_part))
