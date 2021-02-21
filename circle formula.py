r=int(input("Enter the radius:"))
ch=input("1.area of the circle 2.circumference of the circle 3.Diameter of circle. Enter your choice:")
if(ch=="1"):
    a=3.14*(r**2)
    print("Area of the circle is:",a)
if(ch=="2"):
    c=2*3.14*r
    print("Circumference of circle is:",c)
if(ch=="3"):
    d=2*r
    print("Diameter of circle is:",d)
