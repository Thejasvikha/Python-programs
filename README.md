# Python-programs
class bank:
    def __init__(self):
        name=input("enter your name:")
        branch=input("enter the branch:")
        date=input("enter the date:[date.month.year]")
        ac=int(input("enter your account number"))
        pan=input("enter your pan number")
        c=input("you are going to deposit or withdraw")
        self.name=name
        self.branch=branch
        self.date=date
        self.ac=ac
        self.pan=pan
        self.c=c
        if(c=="deposit"):
            self.deposit()
        elif(c=="withdraw"):
            self.withdraw()
    def withdraw(self):
        rs=int(input("enter rupees in digits"))
        rsw=input("enter rupees in words")
        self.rs=rs
        self.rsw=rsw
        print("Thank you for transaction",self.name)
    def deposit(self):
        d=input("enter whether ur deposit is through cash or cheque or dd")
        if(d=="cash"):
          self.denomination()
        elif(d=="cheque"):
            bname=input("enter the bank name")
            bbranch=input("enter the branch:")
            bdate=input("enter the date:[date.month.year]")
            cno=int(input("enter the cheque number"))
            rs=int(input("enter rupees in digits"))
            rsw=input("enter rupees in words")
            self.bname=bname
            self.bbranch=bbranch
            self.bdate=bdate
            self.cno=cno
            self.rs=rs
            self.rsw=rsw
            print("Thanks for ur transaction")
        elif(d=="dd"):
            bname=input("enter the bank name")
            bbranch=input("enter the branch:")
            bdate=input("enter the date:[date.month.year]")
            dno=int(input("enter the dd number"))
            ab=input("enter in favour of what the dd is taken")
            rs=int(input("enter rupees in digits"))
            rsw=input("enter rupees in words")
            self.bname=bname
            self.bbranch=bbranch
            self.bdate=bdate
            self.dno=dno
            self.ab=ab
            self.rs=rs
            self.rsw=rsw
            print("Thanks for ur transaction")
    def denomination(self):
            rs=int(input("enter rupees in digits"))
            rsw=input("enter rupees in words")
            ds=int(input("enter zero"))
            self.rs=rs
            self.rsw=rsw
            self.ds=ds
            print("enter your denomination")
            th=int(input("enter zero"))
            self.th=th
            self.l=[]
            while(not(self.rs==self.ds)):
                i=int(input("enter the amount"))
                t=int(input("enter no.of times it should be multiplied"))
                self.i=i
                self.t=t
                self.th=(self.i*self.t)
                self.l.append(self.th)
                self.ds=sum(self.l)
            print("thanks for your transaction")

b=bank()
                
