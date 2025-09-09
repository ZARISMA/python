def next_greater(arr: list) -> list:
    array = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                array.append(arr[j])
                break
        else:
            array.append(-1)
    return array


print(next_greater([4, 5, 2, 10]))    
print(next_greater([3, 7, 1, 8, 4]))  