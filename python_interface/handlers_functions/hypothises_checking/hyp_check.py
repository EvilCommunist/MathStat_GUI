from handlers_functions.standard_functions.r_functions import (mean, var_unbased as uvar, qnorm,
                                                               t_test, pchisq)
from handlers_functions.standard_functions.standart_functions import sqrt


def check_a0_hypothises(data: list[int] | list[float], a_0: float, alpha: float = 0.1) -> bool:
    chosen_mean = mean(data)
    sigma = sqrt(uvar(data))
    z_value = (chosen_mean - a_0)/(sigma/sqrt(len(data)))
    crit_val = qnorm(1-alpha)
    return z_value > crit_val  # H0 = false, H1 = true


def check_variance0_hypothises(data: list[int] | list[float], var_0: float, alpha: float = 0.1) -> bool:
    chosen_var = uvar(data)
    chi_sq_stat = (len(data)-1)*chosen_var/var_0
    p_val = 1 - pchisq(chi_sq_stat, len(data)-1)
    return p_val < alpha  # H0 = false, H1 = true


def get_good_data_len(a0: float, a1: int | float, sigma: float, alpha: float = 0.1, beta: float = 0.05) -> int:
    z_alpha = qnorm(1-alpha)
    z_beta = qnorm(1-beta)
    n = ((z_alpha + z_beta)*sigma/(a1-a0))**2
    return int(n+0.5)


def get_hyp_prob_result(data: list[int] | list[float], a_0: int | float, alpha: float = 0.1) -> bool:
    p_value = t_test(data, a_0)
    return p_value < alpha  # H0 = false, H1 = true


def get_critical_area():
    pass
