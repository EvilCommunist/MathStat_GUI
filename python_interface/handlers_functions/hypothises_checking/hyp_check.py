from handlers_functions.standard_functions.r_functions import (mean, var_unbased as uvar, qnorm,
                                                               t_test)
from handlers_functions.standard_functions.standart_functions import sqrt


def check_a0_hypothises(data: list[int] | list[float], a_0: float, alpha: float = 0.1) -> bool:
    chosen_mean = mean(data)
    sigma = sqrt(uvar(data))
    z_value = (chosen_mean - a_0)/(sigma/sqrt(len(data)))
    crit_val = qnorm(1-alpha)
    return z_value > crit_val  # H0 = false, H1 = true


def get_good_data_len(a0: float, a1: int | float, sigma: float, alpha: float = 0.1, beta: float = 0.05) -> int:
    z_alpha = qnorm(1-alpha)
    z_beta = qnorm(1-beta)
    n = ((z_alpha - z_beta)*sigma/(a1/a0))**2
    return int(n)


def get_hyp_prob_result(data: list[int] | list[float], a_0: int | float, alpha: float = 0.1) -> bool:
    p_value = t_test(data, a_0)
    return p_value < alpha  # H0 = false, H1 = true
