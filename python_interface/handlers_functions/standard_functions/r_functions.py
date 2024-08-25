from rpy2 import robjects as r_obj


def rtp(some_value) -> float:  # R to Python data
    return float(some_value.r_repr())


def list_is_integer(some_list: list[int] | list[float]) -> bool:
    for val in some_list:
        if isinstance(val, float):
            return False
    return True


def ptr(some_list: list[int] | list[float]) -> r_obj.IntVector | r_obj.FloatVector:  # Python to R data
    if list_is_integer(some_list):
        r_data = r_obj.IntVector(some_list)
    else:
        r_data = r_obj.FloatVector(some_list)
    return r_data


def mean(data: list[int] | list[float]) -> float:
    r_mean = r_obj.r["mean"]
    return rtp(r_mean(ptr(data)))


def var(data: list[int] | list[float]) -> float:
    r_var = r_obj.r["var"]
    return rtp(r_var(ptr(data)))


def var_unbased(data: list[int] | list[float], chosen_middle: float | None = None,  # Not R function, anyway it is
                make_based: bool = False) -> float:                                 # the math base of the program
    if chosen_middle is None:
        chosen_middle = mean(data)
    if make_based:
        chosen_disp: float = sum((val - chosen_middle) ** 2 for val in data) / (len(data)-1)
    else:
        chosen_disp: float = sum((val - chosen_middle) ** 2 for val in data) / len(data)
    return chosen_disp


def median(sorted_data: list[int] | list[float]) -> float | int:
    r_median = r_obj.r["median"]
    return rtp(r_median(ptr(sorted_data)))


def get_cor_coef(data_fst: list[int] | list[float], data_scnd: list[int] | list[float]) -> float:
    r_cor = r_obj.r["cor"]
    return rtp(r_cor(ptr(data_fst), ptr(data_scnd)))
