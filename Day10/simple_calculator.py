from calculator_logo import logo


def multiply(num1, num2):
    return float(num1 * num2)


def divide(num1, num2):
    return float(num1 / num2)


def plus(num1, num2):
    return float(num1 + num2)


def minus(num1, num2):
    return float(num1 - num2)


def choose_operator_function(operator_chosen, first_num, next_num):
    if operator_chosen == '*':
        answer = multiply(first_num, next_num)
        return answer
    elif chosen_operator == '/':
        answer = divide(first_num, next_num)
        return answer
    elif chosen_operator == '+':
        answer = plus(first_num, next_num)
        return answer
    elif chosen_operator == '-':
        answer = minus(first_num, next_num)
        return answer
    else:
        print("You did not type a valid operator")

should_continue = True

operators = ['*', '/', '+', '-']
print(logo)
first_number = int(input("What's the first number?:"))

# print the operators to the console
for op in operators:
    print(op)


while should_continue:
    chosen_operator = input("Pick an operation:")

    next_number = int(input("What's the next number?:"))
    final_value = choose_operator_function(chosen_operator, first_number, next_number)

    num1_float = float(first_number)
    num2_float = float(next_number)

    print(f"{num1_float} {chosen_operator} {num2_float} = {final_value}")
    keep_going = input(f"Type 'y' to continue calculating with {final_value}, or type 'n' to start a new calculation:")

    if keep_going.lower() == 'n':
        should_continue = False
    else:
        first_number = final_value
