import datetime as dt
current_date = dt.datetime.today()
past_date = dt.datetime.today() - dt.timedelta(days = 5)

print(past_date)