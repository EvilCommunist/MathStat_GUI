import os
from handlers_functions.point_estimate.estimation import (get_variance_sample_mean as get_var_smean,
                                                          get_pois_function_likelihood as get_pois)


script_dir = os.path.dirname(__file__)
data_file_path = os.path.join(script_dir, '../../RStudio_test/r_test_data/test_data_point_estimate.txt')

with open(data_file_path, 'r') as data_file:
    raw_data: list[str] = data_file.read().split()
data = list(map(float, raw_data))
print(data)

print(get_var_smean(data))

print(get_pois([1, 0, 1, 2, 2]))
