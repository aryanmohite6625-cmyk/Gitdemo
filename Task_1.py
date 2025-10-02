a = (int(input("Enter any number: ")))
def factorial(n):
    if n ==0 or n ==1 :
        return 1
    else:
        return n*factorial(n-1)
print("factorial of",a,"is",factorial(a))