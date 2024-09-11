from handlers_functions.standard_functions.standart_functions import convert_list_to_tuple as ltt
from handlers_functions.standard_functions.r_functions import (mean, var, var_unbased as uvar,
                                                               qnorm, qt, qchisq)


def get_mean_inteval_borders_norm(selection_size: int, average_weight: int | float,  # use this one for bigger selections
                                  std_deviation: int | float, confidence_prob: float = 0.95) -> tuple[float]:
    standard_error = std_deviation/(selection_size**0.5)
    alpha = 1-confidence_prob
    z_crit = qnorm(1-alpha/2)
    lower_border = average_weight - z_crit*standard_error
    upper_border = average_weight + z_crit * standard_error
    return ltt([lower_border, upper_border])


def get_mean_interval_borders_t(selection_size: int, average_weight: int | float,  # use this one for lesser selections
                                unbased_disp: float, alpha: float = 0.1) -> tuple:
    standard_dev = unbased_disp**0.5
    t_crit = qt(1-alpha/2, selection_size-1)
    lower_border = average_weight - t_crit * (standard_dev/(selection_size**0.5))
    upper_border = average_weight + t_crit * (standard_dev/(selection_size**0.5))
    return ltt([lower_border, upper_border])


def get_variance_interval_borders_chisq(data: list[int] | list[float], alpha: float = 0.1,
                                        average_weight: int | float | None = None,) -> tuple:
    if average_weight is None:
        disp = var(data)
    else:
        disp = uvar(data, average_weight, True)
    chisq_lower = qchisq(1-alpha/2, len(data))
    chisq_upper = qchisq(alpha/2, len(data))
    lower_border = (len(data)-1)*disp / chisq_lower
    upper_border = (len(data)-1)*disp / chisq_upper
    return ltt([lower_border, upper_border])


def get_error_estimation(data: list[int] | list[float], alpha: float = 0.1,
                         average_weight: int | float | None = None,) -> tuple:
    if average_weight is None:
        average_weight = mean(data)
    z = qnorm(1-alpha/2)
    std_err = (average_weight*(1-average_weight)/len(data))**0.5
    lower_border = average_weight - std_err*z
    upper_border = average_weight + std_err * z
    return ltt([lower_border, upper_border])

