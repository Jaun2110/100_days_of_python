# find the highest value in the list:

scores = [123, 5, 800, 555, 3, 1300, 7, 13, 55, 80, 300]
highest_number = 0
for score in scores:
    if score > highest_number:
        highest_number = score

print(f"The highest score in the class is {highest_number}")