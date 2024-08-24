import os
from handlers_functions.confidence_interval.confidence_interval import (get_error_estimation as err_est,
                                                                        get_interval_borders_chisq as ibchisq,
                                                                        get_interval_borders_t as ib_t,
                                                                        get_inteval_borders_norm as ib_norm)


script_dir = os.path.dirname(__file__)
data_file_path = os.path.join(
    script_dir, "../../RStudio_test/r_test_data/conf_int/test_data_error_estimation.txt"
)

with open(data_file_path, "r") as data_file:
    raw_data: list[str] = data_file.read().split()
data = list(map(int, raw_data))

print(err_est(data, 0.05))


data_file_path = os.path.join(
    script_dir, "../../RStudio_test/r_test_data/conf_int/test_data_qchisq.txt"
)

with open(data_file_path, "r") as data_file:
    raw_data: list[str] = data_file.read().split()
data = list(map(float, raw_data))

print(ibchisq(data, 0.05))

print(ib_t(16, 10.3, 1.21, 0.05))

print(ib_norm(100, 249, 10, 0.9))
