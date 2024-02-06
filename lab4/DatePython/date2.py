import datetime as dt


yesterday = dt.datetime.today() - dt.timedelta(days = 1)

today = dt.datetime.today()

tomorrow = dt.datetime.today() + dt.timedelta(days = 1)

print(yesterday,"\n",today,"\n",tomorrow)