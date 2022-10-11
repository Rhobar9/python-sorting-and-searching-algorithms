# This is a sorting by insertion algorithm
def insertion_sorting(dataset):
    for i in range(1, len(dataset)):
        j = i - 1
        next_element = dataset[i]
        while (dataset[j] > next_element) and (j >= 0):
            dataset[j+1] = dataset[j]
        dataset[j+1] = next_element
    return dataset

# This is a sorting by selection algorithm
def selection_sorting(dataset):
    for fill_slot in range(len(dataset) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if dataset[location] > dataset[max_index]:
                max_index = location
            dataset[fill_slot], dataset[max_index] = dataset[max_index], dataset[fill_slot]
    return dataset

# This is a sorting algorithm, invented by Donald Shell
def Shell_sorting(dataset):
    distance = len(dataset) // 2
    while distance > 0:
        for i in range(distance, len(dataset)):
            temp = dataset[i]
            j = i
            while j >= distance and dataset[j-distance] > temp:
                dataset[j] = dataset[j - distance]
                j = j - distance
            dataset[j] = temp
        distance = distance // 2
    return dataset

# This is a bubblesort algorithm
def bubble_sorting(dataset):
    last_index = len(dataset) - 1
    for number in range(last_index, 0, -1):
        for idx in range(last_index):
            if dataset[idx] > dataset[idx + 1]:
                dataset[idx], dataset[idx + 1] = dataset[idx + 1], dataset[idx]
    return dataset

# This is a sorting by merging algorithm, invented by great mathematician John Neumann
def merge_sorting(dataset):
    if len(dataset) > 1:
        center = len(dataset) // 2
        left = dataset[:center]
        right = dataset[center:]

        merge_sorting(left)
        merge_sorting(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                dataset[k] = left[i]
                i += 1
            else:
                dataset[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            dataset[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            dataset[k] = right[j]
            j += 1
            k += 1

    return dataset