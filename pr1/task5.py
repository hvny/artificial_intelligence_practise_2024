import math

point1 = [1, 2, 3]
point2 = [4, 5, 6]

def euclidean_distance(a, b):
    if len(a) != len(b):
        raise ValueError("Массивы координат должны быть одинаковой длины")

    diff = [(a[i] - b[i])**2 for i in range(len(a))]    #массив квадратов разностей
    distance = math.sqrt(sum(diff))                     #корень суммы квадратов разностей
    return distance

result = euclidean_distance(point1, point2)
print("Евклидово расстояние:", result)
