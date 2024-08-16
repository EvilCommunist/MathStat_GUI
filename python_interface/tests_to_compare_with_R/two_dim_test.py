import os
from handlers_functions.selection import two_dim_selection as two_dim_sel


script_dir = os.path.dirname(__file__)
data_file_path = os.path.join(
    script_dir, "../../RStudio_test/r_test_data/test_data_for_2dimension.txt"
)

with open(data_file_path, "r") as data_file:
    next(data_file)
    data_x: list[int] | list[float] = []
    data_y: list[int] | list[float] = []
    for line in data_file:
        x, y = map(float, line.split())
        data_x.append(x)
        data_y.append(y)

print(data_x, data_y)

correlation_coefficient: float = two_dim_sel.get_cor_coef(data_x, data_y)
print(correlation_coefficient)
