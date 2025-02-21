programming_dictionary = {
    "Bug": "A glitch in a computer program",
    "Loop": "Process of doing something over and over again",
    "Function": "A block of code that can be executed over and over again",
}

# #retreive an item
# print(programming_dictionary['Bug'])
#
#
# #loop through
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if 90 < student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif 80 < student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 70 < student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
