from rpy2 import robjects as r_obj
from handlers_functions.selection.one_dim_selection import (get_chosen_middle as mean,
                                                            get_unbased_chosen_disp as disp,
                                                            list_is_integer as is_int)


def get_mix_mean(w_data: list[int] | list[float], a_data: list[int] | list[float]) -> float:
    merged_data: list[int] | list[float] = []
    for w, a in zip(w_data, a_data):
        merged_data.append(w*a)
    return sum(merged_data)


def get_mix_disp(w_data: list[int] | list[float], a_data: list[int] | list[float],
                 sigma_sq_data: list[int] | list[float], mix_mean: float | None = None) -> float:
    if mix_mean is None:
        mix_mean = get_mix_mean(w_data, a_data)
    result: list[float] = []
    for w, a, s_sq in zip(w_data, a_data, sigma_sq_data):
        result.append(w*(s_sq+(a-mix_mean)**2))
    return sum(result)


