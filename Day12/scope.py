#prime number checker
def is_prime(num):
    if num > 1:
        if num > 5 and num % 3 == 0:
            return False
        elif num % 2 == 0 and num != 2:
            return False
        else:
            return True
    else:
        return False


is_prime(75)