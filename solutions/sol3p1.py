def solve(input_data):
    claims = input_data.split('\n')[:-1]

    edges = [claim.split(' ')[2].split(',') for claim in claims]
    edges = [(int(edge[0]), int(edge[1][:-1])) for edge in edges]

    sizes = [claim.split(' ')[3].split('x') for claim in claims]
    sizes = [(int(size[0]), int(size[1])) for size in sizes]

    formatted_claims = zip(edges, sizes)

    counts = {}

    for claim in formatted_claims:
        for i in range(claim[0][0], claim[0][0] + claim[1][0]):
            for j in range(claim[0][1], claim[0][1] + claim[1][1]):
                if i not in counts:
                    counts[i] = {}
                if j not in counts[i]:
                    counts[i][j] = 0

                counts[i][j] += 1

    num_with_2 = 0
    for _, x in counts.items():
        for _, count in x.items():
            if count >= 2:
                num_with_2 += 1

    return num_with_2
