import numpy as np
from kmeans import *
import matplotlib.pyplot as plt

X = np.array([
    [30, 10], 
    [145, 40], 
    [197, 140],
    [175, 130],
    [81, 139],
    [157, 47],
    [132, 55],
    [28, 31],
    [87, 122],
    [141, 127],
    [160, 63],
    [48, 25],
    [15, 29],
    [205, 152],
    [67, 139],
    [75, 115],
    [12, 18],
    [55, 123],
    [156, 153],
    [135, 32],
], dtype=float)


m = np.mean(X, axis=0)
s = np.std(X, axis=0)
X = (X - m) / s

# Запуск алгоритма кластеризации
k = 4

# запускаем алгоритм кластеризации для данных
centers, all_centers, errors = k_means(k, X)

# отображаем график ошибки для каждой промежуточной итерации
plt.plot(np.arange(1, len(errors) + 1), errors, 'bo-')
plt.title('Error by iteration')
plt.xlabel('iteration number')
plt.ylabel('error level')
plt.grid()
plt.show()

# # отображаем траекторию движения каждого центроида
plt.plot(X[:, 0], X[:, 1], 'bo')
plt.title('Centroid trajectories')
plt.xlabel('standardized height')
plt.ylabel('standardized weight')
plt.grid()

plt.plot(centers[:, 0], centers[:, 1], 'g*')

for i in range(0, all_centers.shape[1]):
    x = all_centers[:, i, 0]
    y = all_centers[:, i, 1]
    plt.plot(x, y, 'r.-')

plt.show()

# исследуем количество кластеров
min_k = 2
max_k = 7
error_by_k = np.array([])

for k in range(min_k, max_k + 1):
    min_err = np.array([])
    for i in range(1, 20):
        centers, all_centers, errors = k_means(k, X)
        min_err = np.append(min_err, np.min(errors))
    error_by_k = np.append(error_by_k, np.min(min_err))

plt.plot(np.arange(min_k, max_k + 1), error_by_k, 'bo-')
plt.title('Error by k')
plt.xlabel('k (number of clusters)')
plt.ylabel('error level')
plt.grid()
plt.show()
