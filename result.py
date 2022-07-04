def ProductIteration(*args, repeat):
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    return result


def TwosPair(iteration):
    for curr_value, next_value in zip(iteration, iteration[1:]):
        if curr_value == 1 and next_value == 1:
            return True


def FindValues(without_turbulenc, passengers):
    posibilities = []
    for b in without_turbulenc:
        values = []
        for i, j in enumerate(b):
            if j == 1:
                values.append(passengers[i])
        posibilities.append(values)
    return posibilities


def maximumSum(list1):
    maxi = 0

    # traversal in the lists
    for x in list1:
        sum = 0
        # traversal in list of lists
        for y in x:
            sum += y
        maxi = max(sum, maxi)

    return maxi



test = [463,  73, 282, 422, 271, 118, 112]

all_combinations = ProductIteration(range(2), repeat=len(test))
without_turbulence = [i for i in all_combinations if not TwosPair(i)]
all_possibilities = FindValues(without_turbulence, test)
result = maximumSum(all_possibilities)
print(result)