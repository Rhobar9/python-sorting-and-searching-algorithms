import searching_algorithms
import sorting_algorithms
import sets_generator
import time_measurement

# In this section we are creating dataset and we are testing our algorithms
special_number = 37
dataset = sets_generator.generate_dataset()
print(f'This is a input dataset: {dataset}')

sorted = sorting_algorithms.Shell_sorting(dataset)
print(f'This is a dataset sorted by Shell algorithm: {sorted}')

searching = searching_algorithms.binary_searching(sorted, 0, len(sorted) - 1, special_number)
# There we can simply use truthy-false property of Python language to compare outputs
if searching == 1:
    print(f'Number {special_number} has occured in our dataset!')
else:
    print(f'Number {special_number} does not exist in our dataset!')

# We have computed there only raw process, without print statements
time_consumption = time_measurement.measure_time(time_measurement.environment, time_measurement.code)
print(f'This process, repeated 100 times, have consumed only {time_consumption} seconds!')
