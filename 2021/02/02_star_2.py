"""
https://adventofcode.com/2021/day/2

"""


def parse_input_and_solve(filename):
    file = open(filename)
    depth = 0
    horizontal = 0
    aim = 0
    for line in file:
        instruction, value = line.split()

        if instruction == "forward":
            horizontal += int(value)
            depth += aim * int(value)
        if instruction == "down":
            aim += int(value)
        if instruction == "up":
            aim -= int(value)
    return horizontal, depth


def main():
    input_file_name = "../input"
    horizontal, depth = parse_input_and_solve(input_file_name)
    print(f"Final score is: {horizontal*depth}")
    return horizontal * depth


if __name__ == "__main__":
    main()
