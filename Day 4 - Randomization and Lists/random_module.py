# import the module that you want to use
import random
import my_module


random_integer = random.randint(1, 100)

print(random_integer)
# moduarisation
print(f"the value of py is {my_module.pi}")


# random floating point numbers between 1 and 100 but not including 100
random_float = random.random() * 100
print(f"random floating point number: {random_float}")


#  random love_score
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")