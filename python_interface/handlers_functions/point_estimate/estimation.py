from rpy2 import robjects as r_obj
from handlers_functions.selection.one_dim_selection import (get_chosen_middle as mean,
                                                            get_unbased_chosen_disp as disp,
                                                            list_is_integer as is_int)
# value estimation means finding mean() from the data || оценка значения равняется поиску выборочного среднего
r_sum = r_obj.r["sum"]  # defining global R function for processing likelihood ||
                        # определение функции R для определения правдоподобности


def get_variance_sample_mean(data: list[int] | list[float]) -> float:
    return disp(data, mean(data)) / len(data)


def get_parameter_estimate(data: list[int] | list[float]) -> float:  # IDK if this one's really needed
    return 0


def get_pois_function_likelihood(data: list[int], lambda_value: float | None = None,
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


def get_binomial_function_likelihood(data: list[int], size: float | None = None,
                                     prob: float | None = None, is_log: bool = True) -> float | Exception:
    try:
        if not is_int(data):
            raise Exception(
                "Данные для Биномиального распределения должны быть целочисленными!"
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


def get_normal_function_likelihood(data: list[int] | list[float], ch_middle: float | None = None,
                                   std_deviation: float | None = None, is_log: bool = True) -> float:
    if is_int(data):
        r_data = r_obj.IntVector(data)
    else:
        r_data = r_obj.FloatVector(data)
    if ch_middle is None:
        ch_middle = mean(data)
    if std_deviation is None:
        r_sd = r_obj.r["sd"]
        std_deviation = r_sd(r_data)
    r_dnorm = r_obj.r["dnorm"]
    return float(r_sum(r_dnorm(r_data, ch_middle, std_deviation, is_log)).r_repr())
