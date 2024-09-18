arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]

def modulus_of_differences(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Массивы должны быть одинаковой длины")
    return [abs(arr1[i] - arr2[i]) for i in range(len(arr1))]

result = modulus_of_differences(arr1, arr2)
print(result)
