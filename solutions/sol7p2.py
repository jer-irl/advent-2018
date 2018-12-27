import itertools


def steps_ready(blocked_count):
    return list(sorted([blockee for blockee in blocked_count.keys() if blocked_count[blockee] == 0]))


def step_duration(step):
    return 60 + "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(step) + 1


def solve(input_data):
    pairs = [(toks[1], toks[7]) for toks in [line.split() for line in input_data.split('\n')[:-1]]]
    letters = set([pair[0] for pair in pairs]).union(set(pair[1] for pair in pairs))

    # The steps each step key is blocking
    steps_blocked = {}
    for letter in letters:
        steps_blocked[letter] = []
    for blocker, blockee in pairs:
        steps_blocked[blocker].append(blockee)

    # The count of steps blocking the key, or None if step is not already completed
    blocked_count = {}
    for letter in letters:
        blocked_count[letter] = 0
    for _, blockee in pairs:
        blocked_count[blockee] += 1

    # The job status of each worker, as a tuple of (job, completion_second) or None if not working on a job
    workers_finish_seconds = [None] * 5

    for second in itertools.count():

        # Update available workers
        for job_sec_pair in workers_finish_seconds:
            if job_sec_pair is None:
                continue
            job, sec = job_sec_pair
            if sec > second:
                continue
            # We've finished the job
            for blockee in steps_blocked[job]:
                blocked_count[blockee] -= 1

        workers_finish_seconds = [status if status is None or status[1] > second else None for
                                  status in workers_finish_seconds]

        ready_steps = steps_ready(blocked_count)

        if len(ready_steps) == 0 and all(pair is None for pair in workers_finish_seconds):
            return second

        for ready_step, free_worker_idx in zip(ready_steps, [i for i in range(len(workers_finish_seconds)) if
                                                             workers_finish_seconds[i] is None]):
            blocked_count[ready_step] = None
            workers_finish_seconds[free_worker_idx] = (ready_step, second + step_duration(ready_step))
