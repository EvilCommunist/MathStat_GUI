from rpy2 import robjects as r_obj
from handlers_functions.standard_functions.standart_functions import convert_list_to_tuple as ltt


def get_inteval_borders_norm(selection_size: int, average_weight: int | float,  # use this one for bigger selections
                             std_deviation: int | float, confidence_prob: float = 0.95) -> tuple[float]:
    r_qnorm = r_obj.r["qnorm"]

    standard_error = std_deviation/(selection_size**0.5)
    alpha = 1-confidence_prob
    z_crit = float(r_qnorm(1-alpha/2).r_repr())
    lower_border = average_weight - z_crit*standard_error
    upper_border = average_weight + z_crit * standard_error
    return ltt([lower_border, upper_border])


def get_interval_borders_t(selection_size: int, average_weight: int | float,  # use this one for lesser selections
                           unbased_disp: float, alpha: float = 0.1) -> tuple:
    r_qt = r_obj.r["qt"]

    standard_dev = unbased_disp**0.5
    t_crit = float(r_qt(1-alpha/2, selection_size-1).r_repr())
    lower_border = average_weight - t_crit * (standard_dev/(selection_size**0.5))
    upper_border = average_weight + t_crit * (standard_dev/(selection_size**0.5))
    return ltt([lower_border, upper_border])

