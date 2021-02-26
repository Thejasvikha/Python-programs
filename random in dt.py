def dt():
	import random
	i=random.randint(0,20)
	print("The random number is:",i)
	import datetime
	for i in range(1,i+1):
	        d=datetime.datetime.now()+datetime.timedelta(days=i)
	        print(d)
	        i-=1
dt()
