import random

# This function will fill up our dataset of different random numbers, necessary to further algorithms testing
def generate_dataset():
    dataset = []
    for i in range(20):
        buffer = 101 + i
        new_number = random.randint(1, 100)
        # In this case if-else will be better choice than try-catch block or assertion because
        # we only choose way to further work of script, internal bug can not occur
        if new_number not in dataset:
            dataset.append(new_number)
        else:
            dataset.append(buffer)

    return dataset
