def puzzle1(game_list):
    game_dict = build_game_dict(game_list)
    id_sum = 0
    for id, game in game_dict.items():
        set_doable = []
        for set in game.values():
            # This could be done way more beautiful
            red = False
            green = False
            blue = False
            if set.get("red"):
                if int(set["red"]) <= 12:
                    red = True
            else:
                red = True    

            if set.get("green"):
                if int(set["green"]) <= 13:
                    green = True
            else:
                green = True 

            if set.get("blue"):
                if int(set["blue"]) <= 14:
                    blue = True
            else:
                blue = True 

            if red and green and blue:
                set_doable.append(True)
            else:
                set_doable.append(False)
        if all(set_doable):
            id_sum += id
    print(f"Puzzle 1 solution: {id_sum}")

def puzzle2(game_list):
    game_dict = build_game_dict(game_list)
    cube_sum = 0
    for id, game in game_dict.items():
        max_values = {}
        for key, inner_dict in game.items():
            for inner_key, value in inner_dict.items():
                if inner_key not in max_values or int(value) > max_values[inner_key]:
                    max_values[inner_key] = int(value)
        cube_sum += max_values['red'] * max_values['green'] * max_values['blue']
    print(f"Puzzle 2 solution: {cube_sum}")
            

def build_game_dict(game_list):
    game_dict = {}
    i = 1
    for game in game_list:
        set_dict = {}
        game_dict[i] = {}
        game = game.split(":")[1]
        set_list = game.split(";")
        j = 1
        for set in set_list:
            set_dict[j] = {}
            colors = set.split(",")
            for color in colors:
                color = color.strip()
                split = color.split(" ")
                number = {split[1]: split[0]}
                set_dict[j].update(number)
            j += 1
        game_dict[i].update(set_dict)
        i += 1
    return game_dict

if __name__ == "__main__":
    with open("day2Input.txt") as f:
        game_list = f.readlines()
        puzzle1(game_list)
        puzzle2(game_list)
