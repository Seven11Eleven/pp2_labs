import os
path = r"C:\Users\Alina\PPPP2"
print(f"Test for existence: {os.access(path, os.F_OK)}\nTest for readability: {os.access(path, os.R_OK)}")
print(f"Test for writability: {os.access(path, os.W_OK)}\nTest for executability: {os.access(path, os.X_OK)}")


path1 = r"C:\Users\Alina\somewrongnonsense"
print(f"Test for existence: {os.access(path1, os.F_OK)}\nTest for readability: {os.access(path1, os.R_OK)}")
print(f"Test for writability: {os.access(path1, os.W_OK)}\nTest for executability: {os.access(path1, os.X_OK)}")
