# This is a binary_search algorithm
def binary_searching(dataset, startpoint, endpoint, item):
    while startpoint <= endpoint:
        middle = startpoint + (endpoint - startpoint) // 2

        if dataset[middle] == item:
            return True

        elif dataset[middle] < item:
            startpoint = middle + 1

        else:
            endpoint = middle -1

    return False

# This is a linear_search algorithm
def linear_searching(dataset, item):
    index = 0
    found = False

    while index < len(dataset) and found is False:
        if dataset[index] == item:
            found = True
        else:
            index = index + 1
    return found

# This is a searching by interpolation algorithm
# It is only abstract base to further extensions, we need to add some peculiar properties to appropriately use it
def interpolar_searching(dataset, item):
    idx0 = 0
    idxn = len(dataset) - 1
    found = False

    while idx0 <= idxn and item >= dataset[idx0] and item <= dataset[idxn]:
        middle = idx0 + int(((float(idxn - idx0) / (dataset[idxn] - dataset[idx0])) * (item - dataset[idx0])))
        if dataset[middle] == item:
            found = True
            return True
        if dataset[middle] < item:
            idx0 = middle + 1

    return found
