import os

path = r"C:\Users\Alina\PPPP2\lecture\Lab6\meowmeow"

if os.path.exists(path) == True:
    print(f"Directory name:{os.path.dirname(path)}")
    print(f"Files in this Directory: {os.path.basename(path)}")
else:
    print("You have zero!")