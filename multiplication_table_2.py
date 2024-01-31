def print_multiplication_table(table=1, start=1, end=10):
    for i in range(start, end + 1):
        print(f"{table} * {i} = {table * i}")
    print()


print_multiplication_table()
print_multiplication_table(5)
print_multiplication_table(6,2,8)
print_multiplication_table(end=6)