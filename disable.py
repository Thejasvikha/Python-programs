Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def dt():
	import time
	from datetime import datetime
	from datetime import timedelta
	l=["10","20","30","40","Thejas","appu"]
	print(l)
	while(True):
		d=datetime.now()
		dt=datetime.now()+timedelta(seconds=60)
		print("current time:",datetime.strftime(d,"%M"))
		dt=datetime.strftime(dt,"%M")
		print("time after 1 minute",dt)
		while(True):
			ch=int(input("1.add\n2.insert\n3.remove\nenter your choice:"))
			if(ch==1):
				print("Adding a number:")
				n=input("Enter the value you need to add:")
				l.append(n)
			elif(ch==2):
				print("Inserting a number:")
				n=input("Enter the value you need to insert:")
				le=len(l)
				print("insert a number between",le)
				i=int(input("enter the index position in which you need to insert:"))
				l.insert(i,n)
			elif(ch==3):
				print("Removing a number:")
				n=input("Enter the value you need to remove:")
				l.remove(n)
			else:
				print("invalid choice")
			t=time.localtime().tm_min
			t=str(t)
			print("time after 1 minute",dt)
			if(dt==t):
				print("its disabled for 1 minute")
				time.sleep(60)
				break
