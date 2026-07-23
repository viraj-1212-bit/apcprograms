a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))
if(a <= b and b <= c):
    print("a is smallest",a)
elif(b <= c):
    print("b is the smallest")
else:
    print("c is the smallest")
