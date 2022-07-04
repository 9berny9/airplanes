def ProductIteration(*args, repeat):
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    return result


def TwosPair(list_1):
    for curr_value, next_value in zip(list_1, list_1[1:]):
        if curr_value == 1 and next_value == 1:
            return True


test = [155, 55, 2, 55, 43, 87]

all_combinations = ProductIteration(range(2), repeat=len(test))
without_turbulence = [i for i in all_combinations if not TwosPair(i)]
