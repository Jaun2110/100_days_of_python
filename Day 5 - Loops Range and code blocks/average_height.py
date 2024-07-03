student_heights = input("enter the heights of your students:\n").split()
# print(student_heights)
# convert the list from string to int
student_heights_int_list = []
# create a new list with integer values
for student in student_heights:
    student_heights_int_list.append(int(student))
total_heights = 0
student_count = 0
for height in student_heights_int_list:
    total_heights += height
    student_count += 1

average_height = total_heights/student_count


print(f"total height = {total_heights}\n"
      f"number of students = {student_count}\n"
      f"average height = {average_height}")