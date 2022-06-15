"""
https://adventofcode.com/2021/day/3

"""


def parse_input_and_solve(filename):
    file = open(filename)
    sum_list = []
    small_number = ""
    big_number = ""
    got_length_sum = False
    last_el = 0
    for i, line in enumerate(file):
        binary_string_list = line
        if not got_length_sum:
            sum_list = [0 for _ in binary_string_list[:-1]]
            got_length_sum = True

        for j, el in enumerate(binary_string_list):
            if el == "1":
                sum_list[j] += 1
        last_el = i
    for el in sum_list:
        if el >= (last_el + 1) / 2:
            small_number += "0"
            big_number += "1"
        else:
            small_number += "1"
            big_number += "0"
    big = int(big_number.encode("ascii"), 2)
    small = int(small_number.encode("ascii"), 2)
    return big, small


def main():
    print()
    input_file_name = "../input"
    big, small = parse_input_and_solve(input_file_name)
    print(f"Final score is: {big*small}")
    return big * small


if __name__ == "__main__":
    main()
