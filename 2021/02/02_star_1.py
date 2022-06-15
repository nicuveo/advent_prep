"""
https://adventofcode.com/2021/day/2

"""


def parse_input_and_solve(filename):
    file = open(filename)
    horizontal = 0
    depth = 0
    for i, line in enumerate(file):
        instruction, value = line.split()
        if instruction == "forward":
            horizontal += int(value)
        if instruction == "down":
            depth += int(value)
        if instruction == "up":
            depth -= int(value)
    return horizontal, depth


def main():
    print()
    input_file_name = "../input"
    horizontal, depth = parse_input_and_solve(input_file_name)
    print(f"Final score is: {horizontal*depth}")
    return horizontal * depth


if __name__ == "__main__":
    main()
