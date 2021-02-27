def detail():
	name=input("name:")
	age=int(input("enter your age:"))
	if(age>18):
		print(name,"you are eligible to vote as your age is",age)
	elif(age==18):
		print(name,"your age is",age,".Eligibility to vote is above 18 years.So you are not eligible to vote")
	else:
		print(name,"your age is",age,"which is below 18 so you are not eligible to vote")

detail()
