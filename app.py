def fizzbuzz(num):
    if(num % 3 == 0 and num % 5 == 0):
        print('FizzBuzz')
    elif(num % 3 == 0):
        print("Fizz")
    elif(num % 5 == 0):
        print('Buzz')
    else:
        print(num)


def second_largest(arr):
    first = second = 0
    for i in range(len(arr)):
        if(arr[i] > first):
            second = first
            first = arr[i]

        elif(arr[i] > second and arr[i] is not first):
            second = arr[i]
    print("Second largest number is: ", second)

    # for i in range(len(arr)):
    #     for k in range(len(arr)):
    #         if arr[i] < arr[k]:
    #             arr[k], arr[i] = arr[i], arr[k]
    # print(arr[-2])
    # return arr[-2]


def greater_than_ten(str):
    if(len(str) < 10):
        print("False")
        return False

    elif(len(str) > 10):
        print("True")
        return True


def avg_of_pos(arr):
    pos_num = [item for item in arr if item >= 0]
    avg = sum(pos_num) / len(pos_num)
    print(avg)


def is_sorted(arr):
    for i in range(len(arr)):
        for k in range(len(arr)):
            if arr[k] > arr[i]:
                return False
    return True


numbers = [56, 22, 2, 3, 6, 19, 25, 15, 50, 33, 27, 99, 85, 100, 105, 115, 157]
greaterthanten = "This is greater than ten!"
lessthanten = "Less"

greater_than_ten(greaterthanten)
greater_than_ten(lessthanten)

is_sorted(numbers)
second_largest(numbers)

list_of_numbers = [1, -5, 14, -10, 21, 34]

avg_of_pos(list_of_numbers)
