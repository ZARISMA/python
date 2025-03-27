def majority_element(arr: list) -> int:
    count = 0
    candidate = None
    for i in arr:
        if count == 0:
            candidate = i
        count += (1 if i == candidate else -1)
    return candidate
print(majority_element([3, 3, 4, 2, 3, 3, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))