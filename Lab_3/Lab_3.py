import random
import numpy as np
import scipy.stats

x1_min = 10; x1_max = 50
x2_min = -20; x2_max = 60
x3_min = 10; x3_max = 15

x_min = (x1_min + x2_min + x3_min) / 3
x_max = (x1_max + x2_max + x3_max) / 3

y_min = 200 + x_min
y_max = 200 + x_max

n = 4

x0_n = (1, 1, 1, 1)
x1_n = (-1, -1, 1, 1)
x2_n = (-1, 1, -1, 1)
x3_n = (-1, 1, 1, -1)

x1 = (x1_min, x1_min, x1_max, x1_max)
x2 = (x2_min, x2_max, x2_min, x2_max)
x3 = (x3_min, x3_max, x3_max, x3_min)

def experiment(m):
    y = [[round(random.uniform(y_min, y_max), 3) for i in range(m)] for j in range(n)]
    print('Матриця планування експерименту:\n{0}\n{1}\n{2}\n{3}\n'.format(y[0], y[1], y[2], y[3]))

    # the average value of the response functions in the rows
    y_response = (sum(y[0][i] for i in range(m)) / m,
                  sum(y[1][i] for i in range(m)) / m,
                  sum(y[2][i] for i in range(m)) / m,
                  sum(y[3][i] for i in range(m)) / m)

    print('Середні значення функції відгуку:\n{0}  {1}  {2}  {3}\n'
          .format(round(y_response[0], 3), round(y_response[1], 3), round(y_response[2], 3), round(y_response[3], 3)))

    # calculation of normalized coefficients of the regression equation
    mx1 = (x1[0] + x1[1] + x1[2] + x1[3]) / n
    mx2 = (x2[0] + x2[1] + x2[2] + x2[3]) / n
    mx3 = (x3[0] + x3[1] + x3[2] + x3[3]) / n
    my = (y_response[0] + y_response[1] + y_response[2] + y_response[3]) / n

    a1 = (x1[0] * y_response[0] + x1[1] * y_response[1] + x1[2] * y_response[2] + x1[3] * y_response[3]) / 4
    a2 = (x2[0] * y_response[0] + x2[1] * y_response[1] + x2[2] * y_response[2] + x2[3] * y_response[3]) / 4
    a3 = (x3[0] * y_response[0] + x3[1] * y_response[1] + x3[2] * y_response[2] + x3[3] * y_response[3]) / 4

    a11 = (x1[0] ** 2 + x1[1] ** 2 + x1[2] ** 2 + x1[3] ** 2) / 4
    a22 = (x2[0] ** 2 + x2[1] ** 2 + x2[2] ** 2 + x2[3] ** 2) / 4
    a33 = (x3[0] ** 2 + x3[1] ** 2 + x3[2] ** 2 + x3[3] ** 2) / 4

    a12 = (x1[0] * x2[0] + x1[1] * x2[1] + x1[2] * x2[2] + x1[3] * x2[3]) / 4
    a13 = (x1[0] * x3[0] + x1[1] * x3[1] + x1[2] + x3[2] + x1[3] + x3[3]) / 4
    a23 = (x2[0] * x3[0] + x2[1] * x3[1] + x2[2] * x3[2] + x2[3] * x3[3]) / 4

    b = [np.linalg.det([[my, mx1, mx2, mx3], [a1, a11, a12, a13], [a2, a12, a22, a23], [a3, a13, a23, a33]]) /
         np.linalg.det([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a23], [mx3, a13, a23, a33]]),

         np.linalg.det([[1, my, mx2, mx3], [mx1, a1, a12, a13], [mx2, a2, a22, a23], [mx3, a3, a23, a33]]) /
         np.linalg.det([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a23], [mx3, a13, a23, a33]]),

         np.linalg.det([[1, mx1, my, mx3], [mx1, a11, a1, a13], [mx2, a12, a2, a23], [mx3, a13, a3, a33]]) /
         np.linalg.det([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a23], [mx3, a13, a23, a33]]),

         np.linalg.det([[1, mx1, mx2, my], [mx1, a11, a12, a1], [mx2, a12, a22, a2], [mx3, a13, a23, a3]]) /
         np.linalg.det([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a23], [mx3, a13, a23, a33]])]

    print('Отримане рівняння регресії:\ny = {0} + {1} * x1 + {2} * x2 + {3} * x3\n'
          '\nПеревірка:\nb0 + b1 * x1_min + b2 * x2_min + b3 * x3_min = {4}\n'
          'b0 + b1 * x1_min + b2 * x2_max + b3 * x3_max = {5}\n'
          'b0 + b1 * x1_max + b2 * x2_min + b3 * x3_max = {6}\n'
          'b0 + b1 * x1_max + b2 * x2_max + b3 * x3_min = {7}\n'
          .format(round(b[0], 3), round(b[1], 3), round(b[2], 3), round(b[3], 3),
                  round(b[0] + b[1] * x1[0] + b[2] * x2[0] + b[3] * x3[0], 3),
                  round(b[0] + b[1] * x1[1] + b[2] * x2[1] + b[3] * x3[1], 3),
                  round(b[0] + b[1] * x1[2] + b[2] * x2[2] + b[3] * x3[2], 3),
                  round(b[0] + b[1] * x1[3] + b[2] * x2[3] + b[3] * x3[3], 3)))

    # checking the homogeneity of the variance according to the Cochren's criterion
    # variance by lines and the main deviation
    dispersions = [sum([(y[0][i] - y_response[0]) ** 2 for i in range(m)]) / m,
                   sum([(y[1][i] - y_response[1]) ** 2 for i in range(m)]) / m,
                   sum([(y[2][i] - y_response[2]) ** 2 for i in range(m)]) / m,
                   sum([(y[3][i] - y_response[3]) ** 2 for i in range(m)]) / m]

    gp = max(dispersions) ** 2 / sum([dispersions[i] ** 2 for i in range(n)])

    f1 = m - 1; f2 = n; q = 0.05

    if f1 == 1: gt = 0.9065
    elif f1 == 2: gt = 0.7679
    elif f1 == 3: gt = 0.6841
    elif f1 == 4: gt = 0.6287
    elif f1 == 5: gt = 0.5892
    elif f1 == 6: gt = 0.5598
    elif f1 == 7: gt = 0.5365
    elif f1 == 8: gt = 0.5175
    elif f1 == 9: gt = 0.5017
    elif f1 == 10: gt = 0.4884
    elif 11 <= f1 <= 16: gt = 0.4366
    elif 17 <= f1 <= 136: gt = 0.3720
    else: gt = 0.2500

    if gp > gt:
        i = input(
            'Дисперсія неоднорідна. Якщо ви хочете повторити експериметн при m = m + 1 = {}, введіть 1: \n'.format(
                m + 1))
        if i == '1':
            experiment(m + 1)
            m += 1
    else:
        print('Дисперсія однорідна.')

        # assessment of the significance of regression coefficients according to Student's criterion
        s_b = sum(dispersions) / n
        s = np.sqrt(s_b / (n * m))

        beta = [sum([dispersions[i] * x0_n[i] for i in range(n)]) / n,
                sum([dispersions[i] * x1_n[i] for i in range(n)]) / n,
                sum([dispersions[i] * x2_n[i] for i in range(n)]) / n,
                sum([dispersions[i] * x3_n[i] for i in range(n)]) / n]

        t = [abs(beta[i]) / s for i in range(n)]

        f3 = f1 * f2

        d = 0
        for i in range(n):
            if t[i] < scipy.stats.t.ppf(q=0.975, df=f3):
                print('Коефіцієнт рівняння регресії b{0} приймаємо незначним при рівні значимості 0.05'.format(i))
                b[i] = 0
                d += 1


        # Fisher's criterion
        f4 = n - d
        s_ad = (m * sum([(b[0] + b[1] * x1[i] + b[2] * x2[i] + b[3] * x3[i] - y_response[i]) ** 2 for i in range(n)]) / f4)
        f_p = s_ad / s_b

        if f_p > scipy.stats.f.ppf(q=0.95, dfn=f4, dfd=f3): 
            print('Рівняння регресії неадекватно оригіналу при рівні значимості 0.05')
        else: print('Рівняння регресії адекватно оригіналу при рівні значимості 0.05')

try:
    m = int(input(("Введіть значення m: ")))
    experiment(m)
except:
    breakpoint()
    print("Ви ввели не ціле число. Спробуйте знову.")

