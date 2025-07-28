def factorial(n):
    if n<0:
        return "Factorial cannot be negative"
    if n==0 or n==1:
        return 1
    else:
        return factorial(n-1)*n

num = int(input("Enter a number: "))
print("Factorial of "+str(num)+" is :",factorial(num))