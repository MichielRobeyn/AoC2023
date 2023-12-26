from sympy import symbols, nonlinsolve


def calc_valid_intersections(data):
    x_pos, y_pos, z_pos, x_v, y_v, z_v, t1, t2, t3 = symbols('x_pos, y_pos, z_pos, x_v, y_v, z_v, t1, t2, t3', real=True)
    equations = []
    for i in range(3):
        hail_pos, hail_v = data[i]
        if i == 0:
            eqx = x_pos + x_v*t1 - (hail_pos[0] + hail_v[0]*t1)
            eqy = y_pos + y_v*t1 - (hail_pos[1] + hail_v[1]*t1)
            eqz = z_pos + z_v*t1 - (hail_pos[2] + hail_v[2]*t1)
        elif i == 1:
            eqx = x_pos + x_v * t2 - (hail_pos[0] + hail_v[0] * t2)
            eqy = y_pos + y_v * t2 - (hail_pos[1] + hail_v[1] * t2)
            eqz = z_pos + z_v * t2 - (hail_pos[2] + hail_v[2] * t2)
        else:
            eqx = x_pos + x_v * t3 - (hail_pos[0] + hail_v[0] * t3)
            eqy = y_pos + y_v * t3 - (hail_pos[1] + hail_v[1] * t3)
            eqz = z_pos + z_v * t3 - (hail_pos[2] + hail_v[2] * t3)
        equations.extend([eqx, eqy, eqz])
    return nonlinsolve(equations, [x_pos, y_pos, z_pos, x_v, y_v, z_v, t1, t2, t3])


def main():
    data = []
    with open('day24_input.txt') as file:
        for line in file:
            position, velocity = line.strip().split('@')
            position = tuple([int(char) for char in position.split(',')])
            velocity = tuple([int(char) for char in velocity.split(',')])
            data.append((position, velocity))

    result, = calc_valid_intersections(data)
    print(sum(result[:3]))


if __name__ == '__main__':
    main()
