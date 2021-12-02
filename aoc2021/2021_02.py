from utils.utils import get_data

if __name__ == '__main__':
    data = map(lambda x: x.split(' '), get_data(2021, 2).splitlines())
    aim, depth_a, depth_b, horizontal = 0, 0, 0, 0
    for direction, distance in data:
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
            depth_b += distance * aim
        elif direction == "down":
            depth_a += distance
            aim += distance
        elif direction == "up":
            depth_a -= distance
            aim -= distance

    print("Answer part a:", horizontal * depth_a)
    print("Answer part a:", horizontal * depth_b)
