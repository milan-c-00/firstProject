def print_squares_upto_limit(limit):
    i = 1
    while i*i < limit:
        print(i*i, end=" ")
        i += 1

# print_squares_upto_limit(30)


def print_cubes_upto_limit(limit):
    i = 1
    while pow(i, 3) < limit:
        print(pow(i, 3), end=" ")
        i += 1


print_cubes_upto_limit(30)