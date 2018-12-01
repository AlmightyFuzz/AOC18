TEST1 = '+1, +1, +1'
TEST2 = '+1, +1, -2'
TEST3 = '-1, -2, -3'


def find_total(input):
    total = 0

    for item in input:
        total += int(item)

    return total


def test_solution(test_input):
    total = find_total(test_input.split(','))

    print('Total: ' + str(total))
    return total


def process_puzzle_input():
    file = open('day1Input.txt', 'r')

    file_data = [line.strip('\n') for line in file]

    total = find_total(file_data)

    print('Puzzle Total: ' + str(total))


if __name__ == "__main__":
    test_solution(TEST1)
    test_solution(TEST2)
    test_solution(TEST3)

    process_puzzle_input()