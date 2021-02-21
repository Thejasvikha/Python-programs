Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> def loop():
	str=input("enter a string ")
	ind=-1
	for i in str:
		print(str[:ind+1])
		ind-=1
	for j in str:
		print(str[:ind+1])
		ind+=1

		
>>> 