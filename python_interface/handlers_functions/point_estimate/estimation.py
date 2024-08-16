from rpy2 import robjects as r_obj
from handlers_functions.selection.one_dim_selection import (get_chosen_middle as mean,
                                                            get_chosen_disp as disp,
                                                            list_is_integer as is_int)
# value estimation means finding mean() from the data || оценка значения равняется поиску выборочного среднего
r_sum = r_obj.r["sum"]  # defining global R function for processing likelihood ||
                        # определение функции R для определения правдоподобности


def get_variance_sample_mean(data: list[int] | list[float]) -> float:
    return disp(data, mean(data)) / len(data)


def get_pois_function_likelihood(data: list[int] | list[float], lambda_value: float | None = None,
                                 is_log: bool = True) -> float | Exception:
    try:
        if not is_int(data):
            raise Exception(
                "Данные для распределения Пуассона должны быть целочисленными!"
            )
    except Exception as ex:
        return ex
    if lambda_value is None:
        lambda_value = mean(data)
    r_data = r_obj.IntVector(data)
    r_dpois = r_obj.r["dpois"]
    return float(r_sum(r_dpois(r_data, lambda_value, is_log)).r_repr())


def get_binomial_function_likelihood(data: list[int] | list[float], size: float | None = None,
                                     prob: float | None = None, is_log: bool = True) -> float | Exception:
    try:
        if not is_int(data):
            raise Exception(
                "Данные для распределения Пуассона должны быть целочисленными!"
            )
    except Exception as ex:
        return ex
    if size is None:
        size = max(data)
    if prob is None:
        prob = mean(data)/size
    r_data = r_obj.IntVector(data)
    r_dbinom = r_obj.r["dbinom"]
    return float(r_sum(r_dbinom(r_data, size, prob, is_log)).r_repr())
