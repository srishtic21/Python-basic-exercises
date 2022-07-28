a = int(input('Enter a positive integer: '))
b = int(input('Enter another positive integer: '))

factors_a = []
factors_b = []

i = j = 2

# prime factors of a
while a != 1:
    if a % i == 0:
        a = a / i
        factors_a.append(i)
        i = 2
    else:
        i += 1

# prime factors of b
while b != 1:
    if b % i == 0:
        b = b / i
        factors_b.append(i)
        i = 2
    else:
        i += 1

print('\nPrime factors of a:', factors_a)
print('Prime factors of b:', factors_b)


# prime factors of a AND b
factors_ab = []

for i in factors_a:
    if i in factors_b:
        factors_ab.append(i)
        factors_b.remove(i)
    else:
        factors_ab.append(i)

if factors_b:
    for i in factors_b:
        factors_ab.append(i)
    
print('\nPrime factors of a AND b:', factors_ab)


# calculate lcm
lcm = 1

for i in factors_ab:
    lcm *= i

print('\nLCM:', str(lcm))
