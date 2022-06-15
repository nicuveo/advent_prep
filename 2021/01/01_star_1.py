"""
https://adventofcode.com/2021/day/1

"""


def parse_input_and_solve(filename):
    number_of_increases = -1
    file = open(filename)
    previous_depth = 0
    for line in file:
        num = int(line)
        if num > previous_depth:
            number_of_increases += 1
        previous_depth = num
    return number_of_increases


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
