import re

symbols = ["+", "/", "*", "#", "%", "-", "&", "=", "@", "$"]

def puzzle1(line_list):
    end_sum = 0
    pattern = r'\b\d+\b'
    prev_line = "............................................................................................................................................"
    i = 0 
    while i < len(line_list):
        line = line_list[i]
        if i < len(line_list)-1:
            next_line = line_list[i+1]
        else:
            next_line = "............................................................................................................................................"

        for match in re.finditer(pattern, line):
            number = match.group()
            start = match.start()
            end = match.end()
            matched = False
            
            # this feels so hacky, to avoid out of bounds
            if start == 0:
                start = 1
            if end == 140:
                end = 139

            # check current line 
            if line[start-1] in symbols or line[end] in symbols:
                end_sum += int(number)
                matched = True
            # check previous line 
            elif any(symbol in prev_line[start-1:end+1] for symbol in symbols) and not matched:
                end_sum += int(number)
                matched = True
            # check next line
            elif any(symbol in next_line[start-1:end+1] for symbol in symbols) and not matched:
                end_sum += int(number)
                matched = True

        prev_line = line
        i += 1
    print(end_sum)

def puzzle2(line_list):
    end_sum = 0
    pattern = r'\b\d+\b'
    pattern2 = r'\*'
    prev_line = "............................................................................................................................................"
    i = 0 
    while i < len(line_list):
        line = line_list[i]
        if i < len(line_list)-1:
            next_line = line_list[i+1]
        else:
            next_line = "............................................................................................................................................"

        for match in re.finditer(pattern2, line):
            pos = match.start()
            numbers = []
            
            # this feels so hacky, to avoid out of bounds
            if pos == 0:
                pos = 1
            elif pos == 140:
                pos = 139

            for match in re.finditer(pattern, line):
                if pos in range(match.start()-1, match.end()+1):
                    numbers.append(match.group())
            for match in re.finditer(pattern, prev_line):
                if pos in range(match.start()-1, match.end()+1):
                    numbers.append(match.group())
            for match in re.finditer(pattern, next_line):
                if pos in range(match.start()-1, match.end()+1):
                    numbers.append(match.group())
            if len(numbers) == 2:
                end_sum = end_sum + (int(numbers[0])*int(numbers[1]))

        prev_line = line
        i += 1
    print(end_sum)
   

if __name__ == "__main__":
    with open("day3Input.txt") as f:
        line_list = f.readlines()
        #puzzle1(line_list)
        puzzle2(line_list)