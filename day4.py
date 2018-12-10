import datetime
import re

TEST_DATA = [
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-01 23:58] Guard #99 begins shift',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-03 00:05] Guard #10 begins shift',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-05 00:45] falls asleep',
    '[1518-11-05 00:55] wakes up'
]


def parse_data(record_data):
    regex = r'\[(?P<Y>\d{4})-(?P<M>\d\d)-(?P<D>\d\d) (?P<h>\d\d):(?P<m>\d\d)\] (?P<actn>.*)'
    records = []

    for record in record_data:
        match = re.search(regex, record)
        year = int(match.group('Y'))
        month = int(match.group('M'))
        day = int(match.group('D'))
        hour = int(match.group('h'))
        minute = int(match.group('m'))
        action = match.group('actn')
        date = datetime.datetime(year, month, day, hour, minute)
        print(date)
        records.append(tuple([date, action]))

    return records


if __name__ == "__main__":
    record_data = [line.strip('\n') for line in TEST_DATA]

    records = parse_data(record_data)
    print(records)
