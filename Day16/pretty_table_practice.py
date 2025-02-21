from prettytable import PrettyTable

# new table object
my_first_table = PrettyTable()
# add fieldnames
# my_first_table.field_names = ["Family Member Name", "Age", "Martial Status", "Occupation"]
# # add all rows at once
# my_first_table.add_rows([
#         #list represents each row
#         ["Jano", 29, "Married", "Estate Agent"],
#         ["Patricia", 58, "Divorced", "Pensioner"],
#         ["Jaun", 28, "Single for Life", "Software Dev"],
#     ]
# )

#add data one column at a time
my_first_table.add_column("Member Name", ['Jano', 'Patricia', 'Anke'])
my_first_table.add_column("Age", [29, 58, 5])
my_first_table.add_column("Martial Status", ['Married', 'Divorced', 'Too Young'])
my_first_table.add_column("Occupation", ['Estate Agent', 'Pensioner', 'Minor'])

# change the table alignment by updating the align attribute
my_first_table.align = "r"
# display the table
print(my_first_table)
