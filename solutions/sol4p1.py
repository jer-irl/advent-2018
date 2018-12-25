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

    minutes_asleep = {}
    current_guard = None
    fell_asleep_minute = None
    for record in sorted_records:
        if "begins shift" in record.observation_str:
            current_guard = record.observation_str.split()[1]
        elif "falls asleep" == record.observation_str:
            fell_asleep_minute = record.datetime.minute
        elif "wakes up" == record.observation_str:
            if current_guard not in minutes_asleep:
                minutes_asleep[current_guard] = []
            minutes_asleep[current_guard].append((fell_asleep_minute, record.datetime.minute))

    sleepiest_guard = max(minutes_asleep.keys(),
                          key=lambda guard: sum(nap[1] - nap[0] for nap in minutes_asleep[guard]))

    minutes_sleeping = {}
    for nap in minutes_asleep[sleepiest_guard]:
        fell_asleep_minute, woke_up_minute = nap
        for n in range(fell_asleep_minute, woke_up_minute):
            if n not in minutes_sleeping:
                minutes_sleeping[n] = 0
            minutes_sleeping[n] += 1

    sleepiest_minute = max(minutes_sleeping, key=lambda k: minutes_sleeping[k])

    return int(sleepiest_guard[1:]) * sleepiest_minute
