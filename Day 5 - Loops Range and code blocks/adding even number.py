x = int(input("enter a number:"))

even_numbers = []
even_numbers_total = 0
for number in range(1, x + 1):
    if number % 2 == 0:
        even_numbers.append(number)
        even_numbers_total += number
print(f"{even_numbers_total}\n"
      f"{even_numbers}")
