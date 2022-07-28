def factors_of_a(a):
    '''generates factors of a'''
    factors_a = []
    
    for i in range(1, a+1):
        if a % i == 0:
            factors_a.append(i)
        else:
            continue
    
    return factors_a


def factors_of_b(b):
    '''generates factors of b'''

    factors_b = []
    
    for i in range(1, b+1):
        if b % i == 0:
            factors_b.append(i)
        else:
            continue

    return factors_b


a = int(input('Enter a positive integer: '))
b = int(input('Enter another positive integer: '))


print('\nFactors of', a, 'are:', factors_of_a(a))
print('Factors of', b, 'are:', factors_of_b(b))

common_factors = []

for i in factors_of_a(a):
    if i in factors_of_b(b):
        common_factors.append(i)
    else:
        continue

print('\nCommon factors of', a, 'and', b, 'are:', common_factors)
print('\nGCD is:', max(common_factors))
    
