def extract_mappings(mapping):
    mapping_lines = mapping.split('\n')[1:]
    mapping_lines = [line.strip().split() for line in mapping_lines]
    mappings = []
    for line in mapping_lines:
        current_line = [int(number) for number in line]
        mappings.append(current_line)
    return mappings


def mapping_function(mapping, value):
    output = -1
    for mapping_line in mapping:
        if mapping_line[1] <= value < mapping_line[1] + mapping_line[2]:
            output = mapping_line[0] + (value - mapping_line[1])
    if output == -1:
        output = value
    return output


def main():
    with open('day5_input.txt') as file:
        content = file.read()
    split_contents = content.split('\n\n')
    seeds = split_contents[0].split(':')[1].strip().split()
    seeds = [int(seed) for seed in seeds]

    maps = []
    for i in range(1, len(split_contents)):
        maps.append(extract_mappings(split_contents[i]))

    seed_to_location = dict()
    for seed in seeds:
        loc = seed
        for mapping in maps:
            loc = mapping_function(mapping, loc)
        seed_to_location[seed] = loc

    print(min(seed_to_location.values()))


if __name__ == '__main__':
    main()
