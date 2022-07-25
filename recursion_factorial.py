def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n


n = int(input('Enter numbre for count Factorial'))
f = factorial(n)
print(n,'! =',f) 
