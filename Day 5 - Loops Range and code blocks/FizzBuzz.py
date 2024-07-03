# devisible by 3 then Fizz
# divisible by 5 then Buzz
# divisible by 3 and 5 FizzBuzz

for number in range(1, 100 + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)