import datetime as dt

first_date = dt.datetime(year = 2024, month = 1, day = 22, hour =  14, second = 31) 

second_date = dt.datetime(year = 2024, month = 1, day = 22, hour =  14, second = 15)

print(abs(second_date - first_date))