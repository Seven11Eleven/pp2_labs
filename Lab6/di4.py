import os

with open('C:/Users/Alina/PPPP2/lecture/Lab6/meowmeow/meow.txt', 'r') as text:
    x = sum(1 for line in text)
print(x)