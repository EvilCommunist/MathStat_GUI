import re
from rpy2 import robjects as r_obj
from handlers_functions.standard_functions.standart_functions import (list_is_integer,
                                                                      convert_list_to_tuple as ltt,
                                                                      Rtype)
r_sum = r_obj.r["sum"]  # defining global R function for processing likelihood ||
                        # определение функции R для определения правдоподобности


def rtp(some_value) -> float:  # R to Python data
    return float(some_value.r_repr())


def rtp_list_to_list(some_r_list: r_obj.FloatVector | r_obj.IntVector) -> list:
    values = re.findall(r"[-+]?\d*\.\d+|\d+", some_r_list.r_repr())
    python_list = list(map(float, values))
    return python_list


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


def generate_ideal_data(data: list[int] | list[float], rtype: str):
    match rtype:
        case Rtype.pois.value:
            generated_data = r_obj.r["rpois"](len(data), 1)
            return rtp_list_to_list(generated_data)
        case Rtype.norm.value:
            generated_data = r_obj.r["rnorm"](len(data), 0, 1)
            return rtp_list_to_list(generated_data)
        case Rtype.binom.value:
            generated_data = r_obj.r["rbinom"](len(data), 100, 0.5)
            return rtp_list_to_list(generated_data)


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


def kol_smir_test(data: list[int] | list[float], rtype: str) -> tuple:
    r_ks = r_obj.r["ks.test"]
    generated_data = generate_ideal_data(data, rtype)
    try:
        res = r_ks(ptr(data), ptr(generated_data)).r_repr()

        d_value = re.search(r'D = ([0-9.]+)', res)
        d_value = float(d_value.group(1)) if d_value else None

        p_value = re.search(r'p\.value = ([0-9.]+)', res)
        p_value = float(p_value.group(1)) if p_value else None
    except Exception as ex:
        print("Указано неизвестное распределение")
    return ltt([d_value, p_value])  # D - указывает на достоверность анализа (чем ближе к 1, тем меньше гарантия)
                                    # p - указывает на схожесть между выборками, чем ближе к 1, тем больше схожесть


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
