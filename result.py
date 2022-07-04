def product_iteration(*args, repeat):
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    return print(result)





# test = [155, 55, 2]

# all_combinations = product_iteration(range(2), repeat=len(test))



