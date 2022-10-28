from numpy import random


def interpolation(y_):
    i_ = 0
    new_y = []
    for i_ in range(len(y) - 1):
        new_y.append(y[i_])
        new_y.append((y_[i_ + 1] + y_[i_]) / 2)
    new_y.append(y_[i_])
    return new_y


def offset(y_, sigma_):
    y_ = [number + random.normal(0, sigma_) for number in y_]
    return y_


H = 0.7
m = 0
sigma = 1
y = random.normal(m, sigma, size=3)
i = 0

while i < 10:
    y = interpolation(y)
    sigma = pow(0.5, H) * sigma
    y = offset(y, sigma)
    i += 1
