def get_next(part, rules):
    for rule in rules[:-1]:
        base, end = rule.split(':')
        if base[1] == '<':
            if part[base[0]] < int(base[2:]):
                return end
        elif rule[1] == '>':
            if part[base[0]] > int(base[2:]):
                return end
        else:
            if part[base[0]] == int(base[2:]):
                return end
    return rules[-1]


def get_accepted(parts, workflow):
    total = 0
    for part in parts:
        flow = 'in'
        while flow not in 'AR':
            flow = get_next(part, workflow[flow])
        if flow == 'A':
            total += sum(part.values())
    return total


def main():
    with open('day19_input.txt') as file:
        data = file.read()

    rules, parts = data.strip().split('\n\n')
    workflow = dict()
    for rule in rules.split():
        key, values = rule.split('{')
        values = values[:-1].split(',')
        workflow[key] = values

    processed_parts = []
    for part in parts.split():
        current_part = dict()
        for variable in part[1:-1].split(','):
            key, value = variable.split('=')
            current_part[key] = int(value)
        processed_parts.append(current_part)

    print(get_accepted(processed_parts, workflow))


if __name__ == '__main__':
    main()
