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

ceiling_number = 15
iterate_list = lambda n: [i for i in range(1, n+1)]
num_list = iterate_list(ceiling_number)

player_sum = 0
tax_collector_sum = 0
Is_continue_game = True
back_track_index = -1

# game loop here
while Is_continue_game == True:
    choosen_number = num_list[len(num_list)+back_track_index]

    Is_tax_collector_happy = forecast_tax_collector(num_list, choosen_number)
    while Is_tax_collector_happy == False:
        back_track_index -= 1
        choosen_number = num_list[len(num_list)+back_track_index]
        Is_tax_collector_happy = forecast_tax_collector(num_list, choosen_number)


if tax_collector_sum >= player_sum:
    print("You have lost against the tax collector")
else:
    print("You have won against the tax collector")
print("Tax collector's sum is ", tax_collector_sum)
print("Your sum is ", player_sum)