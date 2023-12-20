from functools import reduce
from copy import deepcopy


def chinese_remainder(m, a):
    total_sum = 0
    prod = reduce(lambda acc, b: acc * b, m)
    for n_i, a_i in zip(m, a):
        p = prod // n_i
        total_sum += a_i * mul_inv(p, n_i) * p
    return total_sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


class Broadcaster:

    def __init__(self):
        self.name = 'broadcaster'
        self.receivers = []
        self.signal = False

    def add_receivers(self, receivers):
        self.receivers.append(receivers)

    def send(self):
        return self.receivers, self.signal, self.name

    def get_receivers(self):
        return self.receivers

    def get_name(self):
        return self.name


class Flipflop:

    def __init__(self, name):
        self.name = name
        self.receivers = []
        self.signal = False

    def add_receivers(self, receivers):
        self.receivers.append(receivers)

    def catch(self, message, sender):
        if not message:
            self.signal = not self.signal
            return self.send(self.signal)
        else:
            return None

    def send(self, message):
        return self.receivers, message, self.name

    def get_receivers(self):
        return self.receivers

    def get_name(self):
        return self.name


class Conjunction:

    def __init__(self, name):
        self.name = name
        self.receivers = []
        self.inputs = []
        self.dict_inputs = dict()

    def add_receivers(self, receivers):
        self.receivers.append(receivers)

    def add_inputs(self, inputs):
        self.inputs.append(inputs)
        self.dict_inputs[inputs] = False

    def catch(self, message, sender):
        self.dict_inputs[sender] = message
        return self.send(message)

    def send(self, message):
        message = not all(self.dict_inputs.values())
        return self.receivers, message, self.name

    def get_receivers(self):
        return self.receivers

    def get_inputs(self):
        return self.inputs

    def get_name(self):
        return self.name


class Output:

    def __init__(self):
        self.signal = False
        self.name = 'output'

    def catch(self, message, sender):
        self.signal = message

    def get_signal(self):
        return self.signal

    def get_name(self):
        return self.name


def get_cycle_offset(objects, end):
    i = 0
    seen = False
    running = True
    while running:
        messages = [objects['broadcaster'].send()]
        while messages:
            next_nodes, message, sender = messages[0]
            del (messages[0])
            for next_node in next_nodes:
                if next_node == objects['qb'] and message and sender == end and seen:
                    running = False
                elif next_node == objects['qb'] and message and sender == end:
                    seen = True
                    offset = i
                response = next_node.catch(message, sender)
                if response is not None:
                    messages.append(response)
        i += 1
    cycle = i - offset - 1
    return cycle, offset


def main():
    data = dict()
    with open('day20_input.txt') as file:
        for line in file:
            key, values = line.strip().split(' -> ')
            data[key] = [value.strip() for value in values.split(',')]

    objects = dict()
    objects['rx'] = Output()
    for el in data:
        if el == 'broadcaster':
            objects['broadcaster'] = Broadcaster()
        elif el[0] == '%':
            objects[el[1:]] = Flipflop(el[1:])
        elif el[0] == '&':
            objects[el[1:]] = Conjunction(el[1:])

    for el in data:
        if el == 'broadcaster':
            for receiver in data[el]:
                objects[el].add_receivers(objects[receiver])
        else:
            for receiver in data[el]:
                objects[el[1:]].add_receivers(objects[receiver])

    for el in data:
        if el[0] == '&':
            for el2 in data:
                if el[1:] in data[el2]:
                    objects[el[1:]].add_inputs(el2[1:])

    kv = get_cycle_offset(deepcopy(objects), 'kv')
    jg = get_cycle_offset(deepcopy(objects), 'jg')
    rz = get_cycle_offset(deepcopy(objects), 'rz')
    mr = get_cycle_offset(deepcopy(objects), 'mr')

    multipliers = [kv[0], jg[0], rz[0], mr[0]]
    offsets = [kv[1], jg[1], rz[1], mr[1]]
    print(chinese_remainder(multipliers, offsets) + 1)


if __name__ == '__main__':
    main()
    print('temp')
