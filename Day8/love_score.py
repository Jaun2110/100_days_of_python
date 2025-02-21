def calculate_love_score(name1, name2):
    complete_string = (name1 + name2).upper()
    true_count = 0
    love_count = 0

    true_count = (complete_string.count('T') + complete_string.count('R') + complete_string.count('U')
                  + complete_string.count('E'))
    love_count = (complete_string.count('L') + complete_string.count('O') +
                  complete_string.count('V')+ complete_string.count('E'))

    final_count = str(true_count) + str(love_count)
    return final_count


love_rating = calculate_love_score("angela yu", "jack bauer")

print(f"Love Score ={love_rating}")
