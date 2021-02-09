import random

x1 = []; x2 = []; x3 = []; y = []

a0 = random.randint(0, 20)
a1 = random.randint(0, 20)
a2 = random.randint(0, 20)
a3 = random.randint(0, 20)

print('a0 = {}; a1 = {}; a2 = {}; a3 = {}\n'.format(a0, a1, a2, a3))

for i in range(8):
    x1.append(random.randint(0, 20))
    x2.append(random.randint(0, 20))
    x3.append(random.randint(0, 20))
    y.append(a0 + a1 * x1[i] + a2 * x2[i] + a3 * x3[i])

print('X1: {}\nX2: {}\nX3: {}\n'.format(x1, x2, x3))
print('Y: {}\n'.format(y))

x10 = (max(x1) + min(x1)) / 2
x20 = (max(x2) + min(x2)) / 2
x30 = (max(x3) + min(x3)) / 2

print('Значення X0: X1_0 = {}; X2_0 = {}; X3_0 = {};'.format(x10, x20, x30))

dx1 = x10 - min(x1)
dx2 = x20 - min(x2)
dx3 = x30 - min(x3)

print('Значення інтервалів зміни фактора dx: dx1 = {}; dx2 = {}; dx3 = {}\n'.format(dx1, dx2, dx3))

x1_n = []; x2_n = []; x3_n = []

for i in range(8):
    x1_n.append(((x1[i] - x10) / dx1).__round__(2))
    x2_n.append(((x2[i] - x20) / dx2).__round__(2))
    x3_n.append(((x3[i] - x30) / dx3).__round__(2))

print('Нормовані значення Xn:\nX1_n: {}\nX2_n: {}\nX3_n: {}\n'.format(x1_n, x2_n, x3_n))

medium_y = sum(y) / 8
print('Середнє значення Y: {}\n'.format(medium_y))

difference = []

for i in range(8):
    if medium_y - y[i] >= 0:
        difference.append(medium_y - y[i])
    else:
        difference.append(1000)

ind = difference.index(min(difference))

print('Варіант 215: -> Y_середнє\ny = {}; x1 = {}; x2 = {}; x3 = {}'.format(y[ind], x1[ind], x2[ind], x3[ind]))
