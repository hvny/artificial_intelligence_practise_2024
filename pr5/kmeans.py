import numpy as np
from random import *
import math

# k - количество искомых кластеров
# X - объекты
def k_means(k, X):
    m = X.shape[0]  # количество точек
    #n = X.shape[1]  # количество признаков объекта
    curr_iteration = prev_iteration = np.zeros([m, 1])

    # генерируем k центров со случайными координатами
    idx = np.arange(0, m)
    shuffle(idx)
    centers = X[idx[0: k], :]

    all_centers = np.copy(centers)
    errors = np.array([])

    # приписываем каждую точку к заданному классу
    curr_iteration, e = class_of_each_point(X, centers)
    errors = np.append(errors, e)

    # цикл до тех пор, пока центры не стабилизируются
    iteration_count = 1
    while not np.all(curr_iteration == prev_iteration):

        prev_iteration = curr_iteration

        # вычисляем новые центры масс
        for i in range(0, k):
            sub_X = X[curr_iteration == i, :]
            if len(sub_X) > 0:
                centers[i, :] = mass_center(sub_X)
            else:
                centers[i, :] = X[randint(0, m-1)]

        all_centers = np.append(all_centers, centers, axis=0)
        # приписываем каждую точку к заданному классу
        curr_iteration, e = class_of_each_point(X, centers)
        errors = np.append(errors, e)
        iteration_count += 1

    all_centers = np.reshape(all_centers, (iteration_count, k, X.shape[1]))
    return centers, all_centers, errors

# вычисление расстояния между двумя точками
def dist(p1, p2):
    return math.sqrt(sum((p1 - p2)**2))


# вычисление центра масс X (среднее по каждому столбцу)
def mass_center(X):
    return np.mean(X, axis=0)


# возвращает список индексов ближайших центров по каждой точке
def class_of_each_point(X, centers):

    m = X.shape[0]
    k = centers.shape[0]

    # матрица расстояний от каждой точки до каждого центра
    distances = np.zeros([k, m])
    for i in range(0, k):
        for j in range(0, m):
            distances[i, j] = dist(centers[i], X[j])

    # поиск ближайшего центра для каждой точки
    min_dist = np.min(distances, axis=0)
    classes = np.argmin(distances, axis=0)
    
    err = np.mean(np.power(min_dist, 2))
    
    return classes, err