user = int(input("Enter a number to check it is Prime Number: "))
for i in range(2,user):
    if not user % i :
        print("not prime number")
        break
    
else:
     print("prime number")



