food=["briyani","parotta","naan","idli","dosai","noodles","fried rice","puri","chappathi","sambar vadai"]
cost=[120,10,20,10,15,40,140,30,25,35]
i=input("Enter the food you want:")
q=int(input("Enter the quantity of food you want:"))
if i in food:
    print(i)
    t=food.index(i)
    d=int(cost[t])
    a=q*d
    print("cost of the food is:",a)
