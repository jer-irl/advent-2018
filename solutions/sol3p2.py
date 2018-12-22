def counts_generator(counts, claim):
    for i in range(claim[0][0], claim[0][0] + claim[1][0]):
        for j in range(claim[0][1], claim[0][1] + claim[1][1]):
            yield counts[i][j]


def solve(input_data):
    claims = input_data.split('\n')[:-1]

    edges = [claim.split(' ')[2].split(',') for claim in claims]
    edges = [(int(edge[0]), int(edge[1][:-1])) for edge in edges]

    sizes = [claim.split(' ')[3].split('x') for claim in claims]
    sizes = [(int(size[0]), int(size[1])) for size in sizes]

    claim_ids = [int(claim.split(' ')[0][1:]) for claim in claims]

    counts = {}

    for claim in zip(edges, sizes):
        for i in range(claim[0][0], claim[0][0] + claim[1][0]):
            for j in range(claim[0][1], claim[0][1] + claim[1][1]):
                if i not in counts:
                    counts[i] = {}
                if j not in counts[i]:
                    counts[i][j] = 0

                counts[i][j] += 1

    for claim in zip(edges, sizes, claim_ids):
        if all(count == 1 for count in counts_generator(counts, claim)):
            return claim[2]

    raise Exception("Couldn't find claim that doesn't overlap")
