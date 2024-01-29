#example 1
print(bool("Hello"))
print(bool(15))




#example 2
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# True 3




#example 3
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# False





#example 4
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))





#example 5
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")