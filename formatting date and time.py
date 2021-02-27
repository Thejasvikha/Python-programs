def dt():
    from datetime import datetime
    d=datetime.now()
    print(datetime.strftime(d,"%I:%M"))
    print(datetime.strftime(d,"%d-%m-%y"))
dt()
