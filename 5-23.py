num = int(input("enter a number "))
num1 = int(input("enter a numer "))
small = 0
g = 0
if num > num1:
    small = num1
else:
    small = num
for x in range(1, num+1):
    if (num % x == 0) and (num1 % x ==0):
       g = x
print((g*(num/g))*(num1/g))
  
   