from handlers_functions.standard_functions.r_functions import (mean, var_unbased as uvar,
                                                               dpois_sum, dnorm_sum, dbinom_sum,
                                                               list_is_integer as is_int)
# value estimation means finding mean() from the data || оценка значения равняется поиску выборочного среднего


def get_variance_sample_mean(data: list[int] | list[float]) -> float:
    return uvar(data, mean(data)) / len(data)


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
    return dpois_sum(data, lambda_value, is_log)


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
    return dbinom_sum(data, size, prob, is_log)


def get_normal_function_likelihood(data: list[int] | list[float], ch_middle: float | None = None,
                                   std_deviation: float | None = None, is_log: bool = True) -> float:
    if ch_middle is None:
        ch_middle = mean(data)
    return dnorm_sum(data, ch_middle, std_deviation, is_log)
