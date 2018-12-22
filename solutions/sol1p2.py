import itertools

def solve(input_data):
    deltas = [int(line) for line in input_data.split()]
    frequencies = set()
    freq = 0
    frequencies.add(freq)
    for delta in itertools.cycle(deltas):
        freq += delta
        if freq in frequencies:
            return freq
        frequencies.add(freq)

    print(frequencies)
    raise Exception("Didn't visit any frequency twice")
