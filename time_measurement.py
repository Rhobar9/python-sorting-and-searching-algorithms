# I have choosen timeit package because
import timeit as ti

environment = '''
import searching_algorithms
import sorting_algorithms
import sets_generator
'''

code = '''
special_number = 37
dataset = sets_generator.generate_dataset()
sorted = sorting_algorithms.Shell_sorting(dataset)
searching = searching_algorithms.binary_searching(sorted, 0, len(sorted) - 1, special_number)
'''

def measure_time(setup, statement):
    result = ti.timeit(setup=setup, stmt=statement, number=100)
    return result
