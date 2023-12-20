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

    total_low = 0
    total_high = 0
    i = 0
    while i < 1000:
        messages = [objects['broadcaster'].send()]
        total_low += 1
        while messages:
            next_nodes, message, sender = messages[0]
            if message:
                total_high += len(next_nodes)
            else:
                total_low += len(next_nodes)
            del(messages[0])
            for next_node in next_nodes:
                response = next_node.catch(message, sender)
                if response is not None:
                    messages.append(response)
        i += 1
    print(total_low * total_high)


if __name__ == '__main__':
    main()
