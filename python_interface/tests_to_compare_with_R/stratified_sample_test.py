import os
from handlers_functions.stratified_sample.stratified_sample import (get_mix_mean_data as meand,
                                                                    get_mix_mean_probs as meanp,
                                                                    get_disp_of_strata as sdisp,
                                                                    get_mix_disp as disp,
                                                                    get_volume_of_strata as get_vols)

script_dir = os.path.dirname(__file__)
data_file_path = os.path.join(
    script_dir, "../../RStudio_test/r_test_data/stratas/test_data_stratif_mix.txt"
)

with open(data_file_path, "r") as data_file:
    next(data_file)
    data_w: list[int] | list[float] = []
    data_a: list[int] | list[float] = []
    data_sigma_sq: list[int] | list[float] = []
    for line in data_file:
        w, a, sigma_sq = map(float, line.split())
        data_w.append(w)
        data_a.append(a)
        data_sigma_sq.append(sigma_sq)

print(data_w, data_a, data_sigma_sq)
print(f"{meanp(data_w, data_a)}\n{disp(data_w, data_a, data_sigma_sq)}")


data_file_path = os.path.join(
    script_dir, "../../RStudio_test/r_test_data/stratas/test_data_stratif_selection.txt"
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

print(meand([data_x, data_y], [0.4, 0.6]))
print(sdisp([data_x, data_y], [0.4, 0.6]))
