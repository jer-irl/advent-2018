from datetime import datetime


class GuardRecord:
    def __init__(self, line):
        date_str = ' '.join(line.split()[0:2])
        self.datetime = datetime.strptime(date_str, '[%Y-%m-%d %H:%M]')

        self.observation_str = ' '.join(line.split()[2:])

    def __lt__(self, other):
        return self.datetime < other.datetime


def solve(input_data):
    sorted_records = sorted([GuardRecord(line) for line in input_data.split('\n')[:-1]])

    slept_minutes = {}
    current_guard = None
    fell_asleep_minute = None
    for record in sorted_records:
        if "begins shift" in record.observation_str:
            current_guard = record.observation_str.split()[1]
        elif "falls asleep" == record.observation_str:
            fell_asleep_minute = record.datetime.minute
        elif "wakes up" == record.observation_str:
            if current_guard not in slept_minutes:
                slept_minutes[current_guard] = {}
            for minute in range(fell_asleep_minute, record.datetime.minute):
                if minute not in slept_minutes[current_guard]:
                    slept_minutes[current_guard][minute] = 0

                slept_minutes[current_guard][minute] += 1

    sleepiest_guard = None
    sleepiest_minute = None
    sleepiest_minute_occurences = 0
    for guard in slept_minutes:
        for minute in slept_minutes[guard]:
            if slept_minutes[guard][minute] > sleepiest_minute_occurences:
                sleepiest_guard = guard
                sleepiest_minute = minute
                sleepiest_minute_occurences = slept_minutes[guard][minute]

    return int(sleepiest_guard[1:]) * sleepiest_minute
