def is_leap_year(year):
    """Takes in a year, check of ot is a leap year and returns True if it is or False if it is not"""
    if year % 4 == 0 and year % 400 == 0:
        return True
    else:
        return False




year_check = int(input('Enter the year you want to check:'))
print(is_leap_year(year_check))