"""
Goal: automatically return the highest score to win against the tax collector 
using greedy algorithm. 
For every round, pick the largest number in the given list that meets the two 
requirements of the game. And deducted by one, every time the requirements are
not met.
"""
def forecast_tax_collector(remaining_number_list: list, number_pick: int):
    current_number = 0
    index = 0
    current_number = remaining_number_list[index]

    while current_number != number_pick:
        if number_pick % current_number == 0:
            return True
        current_number = remaining_number_list[index]
        index += 1
    return False

def tax_collector_turn(remaining_number_list: list, player_number: int):
    total_collect = 0
    index = 0

    while index < len(remaining_number_list):
        remaining_number = remaining_number_list[index]
        if player_number % remaining_number == 0:
            if player_number > remaining_number:
                total_collect += remaining_number
                index -= 1
            remaining_number_list.remove(remaining_number)
        index += 1

    return total_collect

ceiling_number = 100
iterate_list = lambda n: [i for i in range(1, n+1)]
num_list = iterate_list(ceiling_number)

player_sum = 0
tax_collector_sum = 0
Is_continue_game = True
back_track_index = 1

# game loop here
while Is_continue_game == True:
    if len(num_list) < 2:
        Is_continue_game = False
        break

    choosen_number = num_list[len(num_list) - back_track_index]

    Is_tax_collector_happy = forecast_tax_collector(num_list, choosen_number)
    while Is_tax_collector_happy == False:
        if back_track_index >= len(num_list) - 1:
            Is_continue_game = False
            break
        back_track_index += 1
        choosen_number = num_list[len(num_list) - back_track_index]
        Is_tax_collector_happy = forecast_tax_collector(num_list, choosen_number)

    player_sum += choosen_number
    total_collect_this_round = tax_collector_turn(num_list, choosen_number)
    tax_collector_sum += total_collect_this_round


if tax_collector_sum >= player_sum:
    print("You have lost against the tax collector")
else:
    print("You have won against the tax collector")
print("Tax collector's sum is ", tax_collector_sum)
print("Your sum is ", player_sum)