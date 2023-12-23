from copy import deepcopy


class Block:

    def __init__(self, name, coord1, coord2):
        self.name = name
        self.orientation = coord1[2] == coord2[2]
        if self.orientation:
            if coord1[1] == coord2[1]:
                self.location = [(i, coord1[1], coord1[2]) for i in range(coord1[0], coord2[0] + 1)]
            else:
                self.location = [(coord1[0], i, coord1[2]) for i in range(coord1[1], coord2[1] + 1)]
        else:
            self.location = [(coord1[0], coord1[1], i) for i in range(coord1[2], coord2[2] + 1)]

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_orientation(self):
        return self.orientation

    def drop_down(self):
        self.location = [(x, y, z-1) for (x, y, z) in self.location]


def drop_down(block_list):
    occupied = []
    occupied_with_id = dict()
    for block in block_list:
        if block.get_orientation():
            floor = block.get_location()
            collision = False
            while not collision:
                z = floor[0][2]
                if not any((x, y, z-1) in occupied for (x, y, z) in floor) and z-1 > 0:
                    block.drop_down()
                    floor = block.get_location()
                else:
                    collision = True
            for coords in block.get_location():
                occupied_with_id[coords] = block.get_name()
            occupied.extend(block.get_location())
        else:
            x, y, z = block.get_location()[0]
            collision = False
            while not collision:
                if (x, y, z-1) not in occupied and z-1 > 0:
                    block.drop_down()
                    x, y, z = block.get_location()[0]
                else:
                    collision = True
            occupied.append(block.get_location()[0])
            occupied.append(block.get_location()[-1])
            occupied_with_id[block.get_location()[0]] = block.get_name()
            occupied_with_id[block.get_location()[1]] = block.get_name()
    return occupied_with_id


def is_solo_support(block, supporting, supported_by):
    supported = supporting[block.get_name()]
    for block_name in supported:
        if any(bl != block.get_name() for bl in supported_by[block_name]):
            continue
        else:
            return True
    return False


def supports(blocks, occupied):
    supporting = dict()
    supported_by = dict()
    for block in blocks:
        supported_by[block.get_name()] = set()
        supporting[block.get_name()] = set()
    for block in blocks:
        if block.get_orientation():
            floor = block.get_location()
            for (x, y, z) in floor:
                if (x, y, z+1) in occupied:
                    supporting[block.get_name()].add(occupied[(x, y, z+1)])
                    supported_by[occupied[(x, y, z+1)]].add(block.get_name())
        else:
            x, y, z = block.get_location()[-1]
            if (x, y, z + 1) in occupied:
                supporting[block.get_name()].add(occupied[(x, y, z+1)])
                supported_by[occupied[(x, y, z+1)]].add(block.get_name())
    return supporting, supported_by


def calculate_destruction(block, supporting, supported_by):
    total = 0
    supported = supporting[block]
    for block_name in supported:
        if len(supported_by[block_name]) == 1:
            supported_by[block_name].remove(block)
            total += 1 + calculate_destruction(block_name, supporting, supported_by)
        else:
            supported_by[block_name].remove(block)
    return total


def main():
    with open('day22_input.txt') as file:
        data = []
        for line in file:
            data_line = line.strip().split('~')
            data_line = [[int(char) for char in row.strip().split(',')] for row in data_line]
            data.append(data_line)
    data = sorted(data, key=lambda x: x[0][2])

    block_list = []
    for i, block in enumerate(data):
        block_list.append(Block(i, block[0], block[1]))

    occupied = drop_down(block_list)
    supporting, supported_by = supports(block_list, occupied)
    print(supporting)
    print(supported_by)
    total = 0
    for block in block_list:
        temp = deepcopy(supported_by)
        print('Name:', block.get_name())
        total += calculate_destruction(block.get_name(), supporting, temp)
    print(total)


if __name__ == '__main__':
    main()
