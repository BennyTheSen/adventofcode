from collections import defaultdict, Counter

def puzzle(hand_map, puzzle2=False):

    lists_by_frequency = defaultdict(list)

    for item in hand_map:
        freq = character_frequency(item[0], puzzle2)
        lists_by_frequency[freq].append(item)
    # Sorting each list by the custom order
    for freq, items in lists_by_frequency.items():
        lists_by_frequency[freq] = sorted(items, reverse=True, key=lambda item:custom_sort_key(item, puzzle2=puzzle2))

    # split up for full house
    full_house_list = []
    three_of_a_kind_list = []
    for item in lists_by_frequency[3]:
        if is_full_house(item[0]):
            full_house_list.append(item)
        else:
            three_of_a_kind_list.append(item)

    # split up for two pair
    two_pairs_list = []
    one_pair_list = []
    for item in lists_by_frequency[2]:
        if is_two_pairs(item[0]):
            two_pairs_list.append(item)
        else:
            one_pair_list.append(item)

    # reordering
    lists_by_frequency[7] = lists_by_frequency[5] #5
    lists_by_frequency[6] = lists_by_frequency[4] #4
    lists_by_frequency[5] = full_house_list 
    lists_by_frequency[4] = three_of_a_kind_list
    lists_by_frequency[3] = two_pairs_list
    lists_by_frequency[2] = one_pair_list

    index = 1
    i = 1
    sol = 0 
    while i <= len(lists_by_frequency):
        hand_list = lists_by_frequency[i]
        i += 1
        for hand in hand_list:
            sol = sol + (index * int(hand[1]))
            index += 1
    return sol


def parse_input(hand_list):
    hand_mapping = []
    for hand in hand_list:
        tmp_split = hand.split()
        hand_mapping.append(tuple((tmp_split[0], tmp_split[1])))
    return hand_mapping 

# sorting helper for frequency
def character_frequency(hand, puzzle2=False):
    max_chars = 0
    for char in set(hand):
        max_char = hand.count(char)
        if not puzzle2 and max_char > max_chars:
            max_chars = max_char
        if puzzle2 and max_char > max_chars and char != 'J':
            max_chars = max_char
    if puzzle2 and hand != 'JJJJJ':
        max_chars += hand.count('J')
    elif puzzle2:
        max_chars = 5
    return max_chars 

# sorting helper for value
def custom_sort_key(hand, puzzle2=False):
    if puzzle2:
        order = {'A': 0, 'K': 1, 'Q': 2, 'T': 3, '9': 4, '8': 5, '7': 6, '6': 7, '5': 8, '4': 9, '3': 10, '2': 11, 'j': 12}
    else: 
        order = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}
    return [order.get(char, 13) for char in hand[0]]

def is_full_house(s):
    freqs = Counter(s)
    return sorted(freqs.values()) == [2, 3]

def is_two_pairs(s):
    freqs = Counter(s)
    return len(freqs) == 3 and sorted(freqs.values()) == [1, 2, 2]

def is_one_pair(s):
    freqs = Counter(s)
    return len(freqs) == 4

if __name__ == "__main__":
    with open("2023/day7input.txt") as f:
        hand_list = f.readlines()
        hand_map = parse_input(hand_list)
        print(f"Puzzle 1 solution: {puzzle(hand_map)}")
        print(f"Puzzle 2 solution: {puzzle(hand_map, True)}")