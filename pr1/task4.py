import random

num_arrays = 5
num_elements = 10

def generate_arrays_and_find_max_sum(num_arrays, num_elements):
    if (num_arrays <= 0) | (num_elements <= 0):
        raise ValueError("Аргументы num_arrays и num_elements должны быть больше 0")

    max_sum = 0
    max_array = None

    for i in range(num_arrays):
        array = [random.randint(1, 100) for j in range(num_elements)]
        array_sum = sum(array)
        print(f"массив {i+1}: {array}\tсумма: {array_sum}")

        if array_sum > max_sum:
            max_sum = array_sum
            max_array = array

    return max_array

result = generate_arrays_and_find_max_sum(num_arrays, num_elements)
print("Массив с наибольшей суммой элементов:", result)
