def extract_mappings(mapping):
    mapping_lines = mapping.split('\n')[1:]
    mapping_lines = [line.strip().split() for line in mapping_lines]
    mappings = []
    for line in mapping_lines:
        current_line = [int(number) for number in line]
        mappings.append(current_line)
    return mappings


def calculate_overlap(origin, element):
    min_origin, len_origin = origin
    min_element, len_element = element
    min_overlap = max(min_origin, min_element)
    max_overlap = min(min_origin + len_origin - 1, min_element + len_element - 1)
    result = []
    if min_overlap < max_overlap:
        if min_origin < min_overlap:
            result.append(((min_origin, min_overlap - min_origin), False))
        overlap = (min_overlap, max_overlap - min_overlap + 1)
        result.append((overlap, True))
        if min_origin + len_origin - 1 > max_overlap:
            result.append(((max_overlap + 1, min_origin + len_origin - 1 - max_overlap), False))
    else:
        result.append((origin, False))
    return result


def destination(origins, conversionmap):
    endpoints = []
    unmapped = [origins]
    for element in conversionmap:
        new_unmapped = []
        for origin in unmapped:
            overlap_data = calculate_overlap(origin, (element[1], element[2]))
            for overlap_datapoint in overlap_data:
                ranges, overlap_present = overlap_datapoint
                if overlap_present:
                    endpoints.append((ranges[0] - element[1] + element[0], ranges[1]))
                else:
                    new_unmapped.append(ranges)
        unmapped = new_unmapped
    endpoints.extend(unmapped)
    return endpoints


def get_destination(ranges, conversionmap):
    destinations = []
    for element in ranges:
        destinations.extend(destination(element, conversionmap))
    return destinations


def get_final_destinations(ranges, mapping):
    destinations = ranges
    for conversionmap in mapping:
        destinations = get_destination(destinations, conversionmap)
    return destinations


def main():
    with open('day5_input.txt') as file:
        content = file.read()
    split_contents = content.split('\n\n')
    seeds = split_contents[0].split(':')[1].strip().split()
    seeds = [int(seed) for seed in seeds]

    mapping = []
    for i in range(1, len(split_contents)):
        mapping.append(extract_mappings(split_contents[i]))

    seed_ranges = []
    for i, seed in enumerate(seeds[::2]):
        seed_ranges.append((seed, seeds[2*i+1]))
    location_ranges = get_final_destinations(seed_ranges, mapping)

    print(min([location[0] for location in location_ranges]))


if __name__ == '__main__':
    main()
