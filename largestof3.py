a = int(input("enter no a:"))
b = int(input("enter no b:"))
c = int(input("enter no c:"))
if(a >= b and b >= c):
    print("a is the largest number.")
elif(b >= c):
    print("b is the largest number.")
else:
    print("c is the largest number.")
