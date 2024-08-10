import os
from handlers_functions.selection import one_dim_selection as one_dim_sel


script_dir = os.path.dirname(__file__)
data_file_path = os.path.join(script_dir, '../../RStudio_test/r_test_data/test_data_for_1dimension.txt')
raw_data: list[str]

with open(data_file_path, 'r') as data_file:
    raw_data = data_file.read().split()
data = list(map(float, raw_data))
print(data)

sorted_data = one_dim_sel.get_sort_data(data)
mean = one_dim_sel.get_chosen_middle(sorted_data)
ch_disp = one_dim_sel.get_chosen_disp(sorted_data, mean)
ch_median = one_dim_sel.get_chosen_median(sorted_data)
fst_quartile = one_dim_sel.get_quartile(sorted_data)
thrd_quartile = one_dim_sel.get_quartile(sorted_data, 3)

print(sorted_data)
print(mean)
print(ch_disp)
print(ch_median)
print(fst_quartile, thrd_quartile)
