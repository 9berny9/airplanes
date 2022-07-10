def productIteration(*args: range, repeat: int) -> list[list]:
    '''
    Iteration creates all combinations according to
    the range of numbers and the length of the list.

    Example:
        productIteration(range(2), repeat=3)
    Return:
        [[0,0,0], [0,0,1], [0,1,0] [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]
    '''
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    return result


def twosPair(iteration: list[list]) -> bool:
    '''
    The function checks if there are 1 next to each other in the list
    and returns True or False for each list.
    '''
    for curr_value, next_value in zip(iteration, iteration[1:]):
        if curr_value == 1 and next_value == 1:
            return True


def findValues(no_turbulence: list[list], passengers: list[int]) -> list[list]:
    '''
    The function returns a list of all combinations
    with the number of passengers.
    '''
    possibilities = []
    for b in no_turbulence:
        values = []
        for i, j in enumerate(b):
            if j == 1:
                values.append(passengers[i])
        possibilities.append(values)
    return possibilities


def maximumSum(passengers_list: list[list]) -> int:
    '''
    The function returns the sum of the maximum
    number of passengers from all combinations
    '''
    maxi = 0
    for x in passengers_list:
        amount = 0
        for y in x:
            amount += y
        maxi = max(amount, maxi)
    return maxi


if __name__ == "__main__":
    test = [
        [155, 55, 2, 96, 67, 203, 3],
        [155, 54, 3, 10],
        [12, 43, 10, 8, 90, 123, 5, 3, 56],
        [1, 10, 200, 154, 160, 289, 454, 5, 10, 34],
        [347, 440, 342, 297, 104, 118, 119, 268, 218],
        [463, 73, 282, 422, 271, 118, 112]
    ]

    test_cases = list()

    for plane in test:
        all_combinations = productIteration(range(2), repeat=len(plane))
        # List without adjacent ones
        without_turbulence = [i for i in all_combinations if not twosPair(i)]
        all_possibilities = findValues(without_turbulence, plane)
        max_passengers = maximumSum(all_possibilities)
        result_tuple = (plane, max_passengers)
        test_cases.append(result_tuple)
    print(test_cases)


