"""
https://adventofcode.com/2021/day/3

"""


def compare_and_keep(big_not_small, input_list, index):
    if len(input_list) == 1:
        return input_list
    zero_list = []
    one_list = []
    for el in input_list:
        if el[index] == "1":
            one_list.append(el)
        else:
            zero_list.append(el)
    if len(one_list) == len(zero_list):
        if big_not_small:
            return one_list
        else:
            return zero_list

    if len(one_list) > len(zero_list):
        if big_not_small:
            return one_list
        else:
            return zero_list
    else:
        if big_not_small:
            return zero_list
        else:
            return one_list


def parse_input_and_solve(filename):
    file = open(filename)
    sum_list = []
    small_number = ""
    big_number = ""
    got_length_sum = False
    first_ones_list = []
    first_zeros_list = []
    for i, line in enumerate(file):
        binary_string_list = line
        if not got_length_sum:
            sum_list = [0 for _ in binary_string_list[:-1]]
            got_length_sum = True

        for j, el in enumerate(binary_string_list):
            if j == 0:
                if el == "1":
                    first_ones_list.append(line)
                else:
                    first_zeros_list.append(line)
            if el == "1":
                sum_list[j] += 1
    if len(first_ones_list) > len(first_zeros_list):
        big_list = first_ones_list
        small_list = first_zeros_list
    else:
        big_list = first_zeros_list
        small_list = first_ones_list
    index = 1
    while len(big_list) > 1:
        big_list = compare_and_keep(True, big_list, index)
        index += 1
    big = int(big_list[0].encode("ascii"), 2)
    index = 1
    while len(small_list) > 1:
        small_list = compare_and_keep(False, small_list, index)
        index += 1
    small = int(small_list[0].encode("ascii"), 2)

    return big, small


def main():
    input_file_name = "../input"
    big, small = parse_input_and_solve(input_file_name)
    print(f"Final score is: {big*small}")
    return big * small


if __name__ == "__main__":
    main()
