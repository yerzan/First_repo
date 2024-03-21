num  = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')
else:
    print('Decline',num)

pool = 1000
quantity = int(input("Enter the number of mailings: "))
try:
    chunk = pool / quantity
    print (int(chunk))
except ValueError:
    print('Divide by zero completed!')
except ZeroDivisionError:
    print('Cant divide to zero')
