def fizzbuzz(num):
    if(num % 3 == 0 and num % 5 == 0):
        print('FizzBuzz')
    elif(num % 3 == 0):
        print("Fizz")
    elif(num % 5 == 0):
        print('Buzz')
    else:
        print(num)


numbers = [2, 3, 6, 19, 25, 15, 50, 33, 27, 99, 85, 100, 105, 115]

for number in numbers:
    fizzbuzz(number)
