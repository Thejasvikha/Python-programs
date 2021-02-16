Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def hotel():
	name=input("enter your name:")
	i=int(input("number of products u gonna order:"))
	tot=[]
	for i in range(0,i):
		print("Menu:briyani,parotta,chicken,mutton")
		food=input("Enter the food you want:")
		print(food)
		if(food=="briyani"):
			cost=100
			print("cost=",cost)
			tot.append(cost)
		elif(food=="parotta"):
			cost=10
			print("cost=",cost)
			tot.append(cost)
		elif(food=="chicken"):
			cost=80
			print("cost=",cost)
			tot.append(cost)
		elif(food=="mutton"):
			cost=120
			print("cost=",cost)
			tot.append(cost)
		else:
			print(food,"is not available in our hotel")
	totalcost=sum(tot)
	print(totalcost)
	urcost=int(input("your total cash amount is ?"))
	fcost=urcost-totalcost
	print("your balance amount is",fcost)
	print(name,"enjoy the food.thank you visit again")

	
>>> 