import re

TEST = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
]


def parse_claim(claim_data):
    rgx = r'#(?P<cID>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<x_range>\d+)x(?P<y_range>\d+)'

    matches = re.search(rgx, claim_data)

    claim = Claim(matches.group('cID'))
    claim.set_area(
        int(matches.group('x')),
        int(matches.group('x_range')),
        int(matches.group('y')),
        int(matches.group('y_range'))
    )

    return claim


class Claim(object):

    def __init__(self, _ID):
        self.ID = _ID
        self.area = list(tuple())

    def set_area(self, x, x_range, y, y_range):
        x_vals = [x + i for i in range(x_range)]
        y_vals = [y + i for i in range(y_range)]

        # not a zip, make an iteration(?) from itertools
        self.area = list(zip(x_vals, y_vals))
        print(self.area)


if __name__ == "__main__":

    claims = [parse_claim(claim_data) for claim_data in TEST]
