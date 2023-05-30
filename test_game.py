def forecast_tax_collector(remaining_number_list: list, number_pick: int):
    current_number = 0
    index = 0
    while remaining_number_list[index] != number_pick:
        current_number = remaining_number_list[index]
        if number_pick % current_number == 0:
            return True
        index += 1
    return False

def player_turn(remaining_number_list: list):
    number_pick = int(input("Pick your number: "))
    print("You choose ", number_pick)

    while number_pick not in remaining_number_list:
        number_pick = int(input("The number does not exist. Re-enter a new number: "))
    
    Is_tax_collector_happy = forecast_tax_collector(remaining_number_list, number_pick)
    while Is_tax_collector_happy == False:
        number_pick = int(input("The tax collector can not collect anything. Re-enter a new number: "))
        Is_tax_collector_happy = forecast_tax_collector(remaining_number_list, number_pick)
    
    return number_pick

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

ceiling_number = 15
iterate_list = lambda n: [i for i in range(1, n+1)]
num_list = iterate_list(ceiling_number)

player_sum = 0
tax_collector_sum = 0
Is_continue_game = True

while Is_continue_game == True:
    print("The current number list: ",num_list)
    num_player_pick = player_turn(num_list)
    player_sum += num_player_pick
    total_collect_this_round = tax_collector_turn(num_list, num_player_pick)
    tax_collector_sum += total_collect_this_round
    Quit_game = input("Do you want to quit now? Press 'q' to quit the game: ")
    if Quit_game.lower() == 'q':
        Is_continue_game = False
    

if tax_collector_sum >= player_sum:
    print("You have lost against the tax collector")
else:
    print("You have won against the tax collector")
print("Tax collector's sum is ", tax_collector_sum)
print("Your sum is ", player_sum)