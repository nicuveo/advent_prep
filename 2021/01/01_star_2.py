def parse_input_and_solve(filename):
    number_of_increases = 0
    sliding_window = []
    file = open(filename)
    for line in file:
        num = int(line)
        if len(sliding_window) < 3:
            sliding_window.append(num)
            continue
        else:
            sliding_window.append(num)
            # print(sliding_window)
            # print(sliding_window[:3])
            # print(sliding_window[1:])
            if sum(sliding_window[:3]) < sum(sliding_window[1:]):
                number_of_increases += 1

        if len(sliding_window) >= 3:
            sliding_window.pop(0)
    return number_of_increases


def main():
    input_file_name = "../input"
    print(parse_input_and_solve(input_file_name))
    return -1


if __name__ == "__main__":
    main()
