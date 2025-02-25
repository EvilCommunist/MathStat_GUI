from handlers_functions.standard_functions.r_functions import kol_smir_test as ks_test
from handlers_functions.standard_functions.standart_functions import (Rtype as StandDist,
                                                                      convert_list_to_tuple as ltt)


def estimate_distribution(data: list[int] | list[float]) -> tuple[str, float, float]:
    standart_distributions = StandDist.get_values()
    res = [ks_test(data, type_) for type_ in standart_distributions]
    p_list = [res_tuple[1] for res_tuple in res]
    d_list = [res_tuple[0] for res_tuple in res]
    chosen_p = max((p for p in p_list if 0 < p <= 1), default=-1)
    chosen_dist: str = "unset"
    chosen_d: float = -1
    if chosen_p != -1:
        chosen_dist = standart_distributions[p_list.index(chosen_p)]
        chosen_d = d_list[p_list.index(chosen_p)]
    return ltt([chosen_dist, chosen_p, chosen_d])  # если возвращается -1 - распределение не указано
                                                   # если 0.05 - нулевая гипотеза, что по-сути то же самое
