from string import ascii_lowercase, ascii_uppercase

TEST = 'dabAcCaCBAcCcaDA'
LOWER_TO_UPPER = {ch: ascii_uppercase[i]
                  for i, ch in enumerate(ascii_lowercase)}
UPPER_TO_LOWER = {ch: ascii_lowercase[i]
                  for i, ch in enumerate(ascii_uppercase)}
PAIRS = {**LOWER_TO_UPPER, **UPPER_TO_LOWER}  # merge dictinaries into one


def react_polymer(polymer):
    reaction_indexes = []

    # while True:
    reacted = False

    idx = 0
    length = len(polymer)

    while idx < length:
        # for idx, char in enumerate(polymer):
        if idx + 1 < len(polymer):
            char = polymer[idx]
            next_char = polymer[idx + 1]
            if char == PAIRS[next_char]:
                reacted = True
                reaction_indexes.append(idx)
                #  so that consecutive matches only get removed once
                #  'cCc' -> 'c', rather than 'cCc' -> ''
                idx += 1

        idx += 1

    if reacted is False:
        return polymer
    else:
        peices = []
        current_idx = 0
        for idx in reaction_indexes:
            peice = polymer[current_idx:idx]
            peices.append(peice)
            current_idx = idx + 2

        peices.append(polymer[current_idx:])  # last peice

        return react_polymer(''.join(peices))  # recursion


if __name__ == "__main__":
    # polymer = TEST
    polymer = [line.strip('\n') for line in open('day5Input.txt')][0]

    final_polymer = react_polymer(polymer)

    print(final_polymer)
    print(len(final_polymer))
