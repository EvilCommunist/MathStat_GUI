from rpy2 import robjects as r_obj
from handlers_functions.standard_functions.standart_functions import (list_is_integer as is_int,
                                                                      convert_list_to_tuple as ltt)


def mean(data: list[int] | list[float]) -> float:
    if is_int(data):
        r_data: r_obj.IntVector | r_obj.FloatVector = r_obj.IntVector(data)
    else:
        r_data: r_obj.IntVector | r_obj.FloatVector = r_obj.FloatVector(data)
    r_mean = r_obj.r["mean"]
    return float(r_mean(r_data).r_repr())


def var(data: list[int] | list[float]) -> float:
    if is_int(data):
        r_data: r_obj.IntVector | r_obj.FloatVector = r_obj.IntVector(data)
    else:
        r_data: r_obj.IntVector | r_obj.FloatVector = r_obj.FloatVector(data)
    r_var = r_obj.r["var"]
    return float(r_var(r_data).r_repr())


def var_unbased(data: list[int] | list[float], chosen_middle: float | None = None,
                make_based: bool = False) -> float:
    if chosen_middle is None:
        chosen_middle = mean(data)
    if make_based:
        chosen_disp: float = sum((val - chosen_middle) ** 2 for val in data) / (len(data)-1)
    else:
        chosen_disp: float = sum((val - chosen_middle) ** 2 for val in data) / len(data)
    return chosen_disp



