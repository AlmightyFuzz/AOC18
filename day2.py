from collections import Counter

TEST1 = 'abcdef'  # 0     # 0
TEST2 = 'bababc'  # 2a 3b # 2, 3
TEST3 = 'abbcde'  # 2b    # 2
TEST4 = 'abcccd'  # 3c    # 3
TEST5 = 'aabcdd'  # 2a 2d # 2
TEST6 = 'abcdee'  # 2e    # 2
TEST7 = 'ababab'  # 3a 3b # 3

TEST_INPUT = [TEST1, TEST2, TEST3, TEST4, TEST5, TEST6, TEST7]


def find_pairs_triplets(input):
    item_counter = Counter(input)
    unique_items = set(input)
    vals = set()

    if(len(input) == len(unique_items)):
        # No repetitions
        return vals

    for item in unique_items:
        if item_counter[item] == 2:
            vals.add(2)
        if item_counter[item] == 3:
            vals.add(3)

    # contains '2' if a pair is present
    # contains '3' if a triplet is present
    return list(vals)


def find_checksum(input):
    pairs_triplets = [find_pairs_triplets(item) for item in input]

    # take each item in the inner list in the list of lists pairs_triplets
    ls = [item for inner_list in pairs_triplets for item in inner_list]

    group_counter = Counter(ls)
    checksum = (group_counter[2] * group_counter[3])
    print("Checksum: " + str(checksum))


def load_puzzle_input():
    with open('day2Input.txt', 'r') as file:
        return [line.strip('\n') for line in file]


if __name__ == "__main__":
    # find_checksum(TEST_INPUT)
    puzzle_input = load_puzzle_input()
    find_checksum(puzzle_input)
