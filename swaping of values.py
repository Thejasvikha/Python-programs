x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
s=x+y      
a=x-y
m=x//y
d=x*y
print("printing values of a:",a,"s:",s,"m:",m,"d:",d,"before swapping")
s,a,m,d=a,s,d,m
print("printing values of a:",a,"s:",s,"m:",m,"d:",d, " after swapping")


