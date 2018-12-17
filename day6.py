import re

TEST = '''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''


def parse_coords(data):
    coords = []
    regex = r'(\d+), (\d+)'

    for line in data:
        match = re.search(regex, line)
        x = int(match.group(1))
        y = int(match.group(2))

        coords.append((x, y))

    return set(coords)


def find_bounding_box(coords):
    bounding_box = dict()
    bounding_box['min_x'] = min([coord[0] for coord in coords])
    bounding_box['min_y'] = min([coord[1] for coord in coords])
    bounding_box['max_x'] = max([coord[0] for coord in coords])
    bounding_box['max_y'] = max([coord[1] for coord in coords])

    return bounding_box


if __name__ == "__main__":
    coord_data = TEST.split('\n')
    # coord_data = [line.strip('\n') for line in open('day6Input.txt')]

    coords = parse_coords(coord_data)
    bbox = find_bounding_box(coords)

    print(bbox)
