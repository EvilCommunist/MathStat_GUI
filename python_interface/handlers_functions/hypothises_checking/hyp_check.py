from handlers_functions.standard_functions.r_functions import (mean, var_unbased as uvar, qnorm)
from handlers_functions.standard_functions.standart_functions import sqrt


def check_a0_value(data: list[int] | list[float], a_0, alpha=0.1) -> bool:
    chosen_mean = mean(data)
    sigma = sqrt(uvar(data))
    z_value = (chosen_mean - a_0)/(sigma/sqrt(len(data)))
    crit_val = qnorm(1-alpha)
    return z_value > crit_val  # H0 = false, H1 = true
