def puzzle1(game_list):
    end_sum = 0
    for game in game_list:
        tmp_split = game.split(":")[1]
        winning_numbers = list(map(int, tmp_split.split("|")[0].split()))
        your_numbers = list(map(int, tmp_split.split("|")[1].split()))
        game_sum = 0 
        for your_number in your_numbers:
            if your_number in winning_numbers:
                if game_sum == 0:
                    game_sum = 1
                else: 
                    game_sum = game_sum * 2
        end_sum += game_sum
    print(f"Puzzle 1 solution: {end_sum}")
    
def puzzle2(game_list):
    copies = {key: 1 for key in range(1, 202)}
    i = 2
    for game in game_list:
        tmp_split = game.split(":")[1]
        winning_numbers = list(map(int, tmp_split.split("|")[0].split()))
        your_numbers = list(map(int, tmp_split.split("|")[1].split()))
        copies_won = 0
        for your_number in your_numbers:
            if your_number in winning_numbers:
                copies_won += 1
        #print(f"Game {i-1}: {copies_won}")
        
        # increase copies
        for key in range(i, i + copies_won):
            j = i-1
            copies[key] += copies[j]
        i += 1
    
    print(f"Puzzle 2 solution: {sum(copies.values())}")
                

if __name__ == "__main__":
    with open("day4input.txt") as f:
        game_list = f.readlines()
        puzzle1(game_list)
        puzzle2(game_list)