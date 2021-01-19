# p_not: population at t_not
# r: rate of growth

# p = p_not * e ** (r*t)

print('Estimate world population\n')

p_not = 7.8 * 10 ** 9
t_not = 2020
r = 0.0105

t = int(input('Please enter a year: '))

import math

p = p_not * math.exp(r*(t - t_not))
print(f'In {t} the world population will be {format(int(p), ",.0f")}.')