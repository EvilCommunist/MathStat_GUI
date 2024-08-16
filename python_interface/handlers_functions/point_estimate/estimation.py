from rpy2 import robjects as r_obj
from rpy2.robjects.packages import importr
from handlers_functions.selection.one_dim_selection import (get_chosen_middle as mean,
                                                            get_chosen_disp as disp,
                                                            list_is_integer as is_int)
# value estimation means finding mean() from the data || оценка значения равняется поиску выборочного среднего
r_sum = r_obj.r['sum']  # defining global R function for processing likelihood ||
                        # определение функции R для определения правдоподобности


def get_variance_sample_mean(data: list[int] | list[float]) -> float:
    return disp(data, mean(data))/len(data)


def get_pois_function_likelihood(data: list[int] | list[float], lyambda: float | None = None, is_log: bool = True) -> float | Exception:
    try:
        if not is_int(data):
            raise Exception("Данные для распределения Пуассона должны быть целочисленными!")
    except Exception as ex:
        return ex
    if lyambda is None:
        lyambda = mean(data)
    r_data = r_obj.IntVector(data)
    r_dpois = r_obj.r['dpois']
    return float(r_sum(r_dpois(r_data, lyambda, is_log)).r_repr())
