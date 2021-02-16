def calc():
    while(True):
        ch=int(input("Enter your choice 1 to 5"))
        s=int(input("Enter a number"))
        m=int(input("Enter another number"))
        if(ch==1):
            t=s+m
            print("By adding we get",t)
        elif(ch==2):
            t=s-m
            print("By subtracting we get",t)
        elif(ch==3):
            t=s*m
            print("By multiplying we get",t)
        elif(ch==4):
            t=s//m
            print("By dividing we get",t)
        elif(ch==5):
            print("Exit")
            break
calc()
