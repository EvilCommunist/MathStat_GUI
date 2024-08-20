from rpy2 import robjects as r_obj
from handlers_functions.selection.one_dim_selection import (get_chosen_middle as mean,
                                                            get_unbased_chosen_disp as disp,
                                                            list_is_integer as is_int)


def get_mix_mean(w_data: list[int] | list[float], a_data: list[int] | list[float]) -> float:
    merged_data = [w*a for w, a in zip(w_data, a_data)]
    return sum(merged_data)


def get_mix_disp(w_data: list[float], a_data: list[int] | list[float],
                 sigma_sq_data: list[int] | list[float] | None = None, mix_mean: float | None = None) -> float:
    if sigma_sq_data is None:
        sigma_sq_data = [0]*len(w_data)
    if mix_mean is None:
        mix_mean = get_mix_mean(w_data, a_data)
    result = [w*(s_sq+(a-mix_mean)**2)
              for w, a, s_sq in zip(w_data, a_data, sigma_sq_data)]
    return sum(result)


def get_disp_of_strata(stratas: list[list[int]] | list[list[float]], probs: list[float]) -> float:
    mix_means = [mean(data) for data in stratas]
    mix_mean = get_mix_mean(w_data=probs, a_data=mix_means)
    answer_prefix = [disp(strata)*prob for strata, prob in zip(stratas, probs)]
    return sum(answer_prefix)+get_mix_disp(w_data=probs, a_data=mix_means, mix_mean=mix_mean)
