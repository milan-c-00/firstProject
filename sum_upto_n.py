def sum_upto_n(number):
    sum = 0
    for i in range(1, number+1):
        sum = sum + i
    return sum

print(sum_upto_n(6))
print(sum_upto_n(10))