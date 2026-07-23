n =list(map( int,input("Enter a number:").split()))
maximum = n[0]
for i in n:
 if i > maximum:
   maximum = i
print(maximum)
