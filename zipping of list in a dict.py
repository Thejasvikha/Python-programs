def school():
    t=int(input("range:"))
    import random
    r=random.randint(0,t)
    print(str(r))
    for i in range(1,t+1):
        z={}
        a=input("enter the name:")
        b=int(input("enter the age:"))
        l=[]
        l.append(a)
        l.append(b)
        z.update({i:l})
        print(z)
    print(z.get(r))
school()
