from itertools import pairwise

def parse_input(input, puzzle2=False):
    sequences = []
    for line in input:
        if puzzle2:
            sequence = [eval(i) for i in line.strip().split()]
            sequence.reverse()
            sequences.append(sequence)
        else:    
            sequences.append([eval(i) for i in line.strip().split()])
    return sequences

def puzzle1(sequences):
    sol = 0
    
    for sequence in sequences:
        steps = [sequence]
        prev_step = steps[-1]
        # doing the steps until each diff is 0
        while not all(v==0 for v in prev_step):
            steps.append([y-x for (x, y) in pairwise(prev_step)])
            prev_step = steps[-1]
        steps.reverse()
        i = 1
        while i < len(steps):
            steps[i].append(steps[i-1][-1]+steps[i][-1])
            i += 1
        sol += steps[-1][-1]
    return sol

if __name__ == "__main__":
    with open("2023/day9input.txt") as f:
        input = f.readlines()
        sequences = parse_input(input)
        sequences2 = parse_input(input, True)
        print(f"Puzzle 1 solution: {puzzle1(sequences)}")
        print(f"Puzzle 2 solution: {puzzle1(sequences2)}")