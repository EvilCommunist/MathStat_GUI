import os
from handlers_functions.selection import one_dim_selection as one_dim_sel
from handlers_functions.standard_functions import standart_functions as base


script_dir = os.path.dirname(__file__)
data_file_path = os.path.join(
    script_dir, "../../RStudio_test/r_test_data/selection/test_data_for_1dimension.txt"
)

with open(data_file_path, "r") as data_file:
    raw_data: list[str] = data_file.read().split()
data = list(map(float, raw_data))
print(data)

sorted_data = one_dim_sel.get_sort_data(data)
mean = base.mean(sorted_data)
ch_disp = base.var_unbased(sorted_data, mean)
based_ch_disp = base.var(sorted_data)
ch_median = one_dim_sel.get_chosen_median(sorted_data)
fst_quartile = one_dim_sel.get_quartile(sorted_data)
thrd_quartile = one_dim_sel.get_quartile(sorted_data, 3)

print(sorted_data)
print(mean)
print(ch_disp)
print(based_ch_disp)
print(ch_median)
print(fst_quartile, thrd_quartile)
