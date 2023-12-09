from math import lcm

def parse_input(input):
    directions = input[0].strip() 
    mappings = input[2:]
    mapping_dict = {}
    for mapping in mappings:
        tmp_split = mapping.split(" = ")
        map_split = tmp_split[1].strip().split(", ")
        map_split[0] = map_split[0].replace("(", "")
        map_split[1] = map_split[1].replace(")", "")
        mapping_dict[tmp_split[0]] = tuple(map_split)
    return directions, mapping_dict

def puzzle1(directions, mappings):
    cur_location = 'AAA'
    steps = 0
    i = 0 
    while cur_location != 'ZZZ':
        if directions[i] == 'L':
            direction = 0
        elif directions[i] == 'R':
            direction = 1
        cur_location = mappings[cur_location][direction]
        
        if i == len(directions) - 1:
            i = 0
        else:
            i += 1
        steps += 1
    print(f"Puzzle 1 solution: {steps}")

def puzzle2(directions, mappings):
    steps = []
    starting_locations = []

    for location in mappings.keys():
        if location[2] == 'A':
            starting_locations.append(location)

    # calculate the steps of each gost path
    for location in starting_locations:
        location__steps = 0
        i = 0 
        cur_location = location
        while cur_location[2] != 'Z':
            if directions[i] == 'L':
                direction = 0
            elif directions[i] == 'R':
                direction = 1
            cur_location = mappings[cur_location][direction]
 
            if i == len(directions) - 1:
                i = 0
            else:
                i += 1
            location__steps += 1
        # the least common multiplier of all individual paths is the solution
        steps.append(location__steps)

    print(f"Puzzle 2 solution: {lcm(*steps)}")

if __name__ == "__main__":
    with open("2023/day8input.txt") as f:
        input = f.readlines()
        directions, mappings = parse_input(input)
        puzzle1(directions, mappings)
        puzzle2(directions, mappings)