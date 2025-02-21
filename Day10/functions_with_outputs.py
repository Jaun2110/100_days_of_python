
def format_name(fName, lName):
    name_first_letter = fName[0].upper()
    remaining_first_name = fName[1: len(fName)]
    last_name_first_letter = lName[0].upper()
    remaining_last_name = lName[1: len(lName)]

    fName = name_first_letter + remaining_first_name
    lName = last_name_first_letter + remaining_last_name

    return f'{fName} {lName}'


first_name = input("enter your first name:").lower()
last_name = input('enter your last name:').lower()

print(format_name(first_name, last_name))

#can also use title() function
# print(f'{name_first_letter}, {remaining_first_name}, {last_name_first_letter}, {remaining_last_name}')



