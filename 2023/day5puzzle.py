def parse_mappings(file_content):
    # parse the input to list of seeds and maps of the other things
    lines = file_content.strip().split('\n')
    seeds = list(map(int, lines[0].split(': ')[1].split()))
    mappings = []
    current_mapping = []

    for line in lines[2:]:
        if ':' in line:
            if current_mapping:
                mappings.append([t for t in current_mapping if len(t) == 3])
                current_mapping = []
        else:
            if line.strip():  # Check if the line is not empty
                current_mapping.append(tuple(map(int, line.split())))

    if current_mapping:
        mappings.append([t for t in current_mapping if len(t) == 3])

    return seeds, mappings

def map_value(value, map_list):
    # Maps a value using the provided map list.
    for dest_start, src_start, length in map_list:
        if src_start <= value < src_start + length:
            offset = value - src_start
            # Return the corresponding value in the destination range
            return dest_start + offset
    # If the value is not in any range, it maps to itself
    return value

def process_seeds(seeds, mappings):
    # Process each seed through the sequence of mappings
    final_values = []
    for seed in seeds:
        value = seed
        for map_list in mappings:
            value = map_value(value, map_list)
        final_values.append(value)
    return final_values

if __name__ == "__main__":
    with open("2023/day5input.txt") as f:
        input = f.read()
        seeds, mappings = parse_mappings(input)
        final_locations = process_seeds(seeds, mappings)
        lowest_location = min(final_locations)
        print(lowest_location)
