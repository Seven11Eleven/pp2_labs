some_string = "MYnameISyernur"
upper = sum(map(lambda x : x.isupper(), some_string))
lower = sum(map(lambda x : x.islower(), some_string))

print(upper, lower)