def sum_of_divisors(number):
    sum = 0
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            sum = sum + divisor
    return sum


print(sum_of_divisors(12))