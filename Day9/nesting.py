capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#nested list in dictionary

travel_log = {
    "France": {
        "times_visited": 12,
        "Cities_visited": ['Paris', 'Lille', 'Dijon']

    },
    "Germany": {
        "times_visited": 8,
        "Cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    }
}

#print stuttgart
print(travel_log["Germany"]["Cities_visited"][2])


# #print lille
# print(travel_log['France'][2])
#
# #nested lists
# nested_list = ['A', 'B', ['C', 'D']]
# print(nested_list[2][1])
