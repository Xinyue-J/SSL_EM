import numpy as np
import matplotlib.pyplot as plt


def nor(x, u, sigma):
    return 1 / ((2 * np.pi * sigma * sigma) ** 0.5) * np.exp(-(x - u) ** 2 / (2 * sigma * sigma))


x1 = [1, 2]
y1 = 1
x2 = [4]
y2 = 2
pi1 = 0.5
pi2 = 0.5
sigma1 = 1
sigma2 = 1
xh = 3
u1 = 1.5
u2 = 4

gamma_1 = []
gamma_2 = []
u_1 = [u1]
u_2 = [u2]
t = [0]
for i in range(0, 10):
    # E step
    alpha = nor(xh, u1, sigma1) * pi1 + nor(xh, u2, sigma2) * pi2
    gamma1 = pi1 / alpha * nor(xh, u1, sigma1)
    gamma2 = pi2 / alpha * nor(xh, u2, sigma2)

    # M step
    u1 = (gamma1 * xh + sum(x1)) / (gamma1 + len(x1))
    u2 = (gamma2 * xh + sum(x2)) / (gamma2 + len(x2))

    # print(gamma1, gamma2)
    # print(u1, u2)

    gamma_1.append(gamma1)
    gamma_2.append(gamma2)
    u_1.append(u1)
    u_2.append(u2)
    t.append(i + 1)

plt.figure(1)
plt.plot(t, u_1, markersize=6, c='r', marker='o', label='u1')
plt.plot(t, u_2, markersize=6, c='b', marker='o', label='u2')
plt.legend()
plt.show()
plt.figure(2)
plt.plot(t[1:], gamma_1, markersize=6, c='r', marker='o', label='gamma1')
plt.plot(t[1:], gamma_2, markersize=6, c='b', marker='o', label='gamma2')
plt.legend()
plt.show()
print(gamma_1[-1], gamma_2[-1])
print(u_1[-1], u_2[-1])
