# datatypes do not matter

# each item has an order in the list

states_in_US =["Delaware", "Pennsylvania"]
print(states_in_US[0])
# last item in the list:

print(states_in_US[-1])

# update an item
states_in_US[1] = "Pennywise"
print(states_in_US)
#  add item to list
states_in_US.append(("JaunLand"))
print(states_in_US)

# extend the list:
states_in_US.extend(["jaun","dean"])
print(states_in_US)