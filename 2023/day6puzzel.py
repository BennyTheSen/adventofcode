# most shitty code this year but it gets the job done with brute force
times = [40, 82, 84, 92]
distances = [233, 1011, 1110, 1487]
i = 0
sol = 1
while i<len(times):
    time = times[i]
    distance = 0
    wins = 0
    speed = 5 # no need to start lower with those numbers
    while speed < time:
        distance = speed * (time - speed)
        if distance > distances[i]:
            wins += 1
        speed += 1
    sol = sol * wins
    i += 1
print(f"Puzzle 1 solution: {sol}")
    
time = 40828492
record = 233101111101487
wins = 0
speed = 5 # no need to start lower with those numbers
while speed < time:
    distance = speed * (time - speed)
    if distance > record:
        wins += 1
    speed += 1
print(f"Puzzle 2 solution: {wins}")