def factorial(n):
    print("Factorial is a n = ", n)
    if n == 1:
        print("Factorial is: ")
        return 1
    else:
        result = n * factorial(n-1)
        print("Factorial is a n = ", n, ": ", result)
        return result
print(factorial(5))