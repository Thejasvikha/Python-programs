Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def school():
	i=int(input("enter the number of students:"))
	for t in range(0,i):
		name=input("enter student name:")
		std=int(input("enter the standard:"))
		if (std<=12 and std>9):
			print(name,"is public exam student")
		elif(std<=9 and std>5):
			print(name,"is in higher class")
		elif(std<=5 and std>=1):
			print(name,"is in primary")
		else:
			print(name,"is in pre-school")

			
>>> 