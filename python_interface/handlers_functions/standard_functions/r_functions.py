from rpy2 import robjects as r_obj
r_sum = r_obj.r["sum"]  # defining global R function for processing likelihood ||
                        # определение функции R для определения правдоподобности


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


def dpois_sum(data: list[int], lambda_value: float, is_log: bool) -> float:
    r_dpois = r_obj.r["dpois"]
    return rtp(r_sum(r_dpois(ptr(data), lambda_value, is_log)))


def dbinom_sum(data: list[int], size: float, prob: float, is_log: bool) -> float:
    r_dbinom = r_obj.r["dbinom"]
    return rtp(r_sum(r_dbinom(ptr(data), size, prob, is_log)))


def dnorm_sum(data: list[int] | list[float], ch_middle: float,
              std_deviation: float, is_log: bool) -> float:
    if std_deviation is None:
        r_sd = r_obj.r["sd"]
        std_deviation = r_sd(ptr(data))
    r_dnorm = r_obj.r["dnorm"]
    return rtp(r_sum(r_dnorm(ptr(data), ch_middle, std_deviation, is_log)))


def qnorm(prob: float) -> float:
    r_qnorm = r_obj.r["qnorm"]
    return rtp(r_qnorm(prob))


def qt(prob: float, df: int) -> float:
    r_qt = r_obj.r["qt"]
    return rtp(r_qt(prob, df))


def qchisq(prob: float, df: int) -> float:
    r_qchisq = r_obj.r["qchisq"]
    return rtp(r_qchisq(prob, df))
