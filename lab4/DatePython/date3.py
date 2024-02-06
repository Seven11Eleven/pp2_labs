import datetime as dt

datetime_now = dt.datetime.now()

datetime_without_microsec = datetime_now.replace(microsecond=0)

print(datetime_without_microsec)