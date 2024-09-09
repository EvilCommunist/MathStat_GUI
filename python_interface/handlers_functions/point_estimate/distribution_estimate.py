from handlers_functions.standard_functions.r_functions import kol_smir_test as ks_test
from handlers_functions.standard_functions.standart_functions import (Rtype as StandDist,
                                                                      convert_list_to_tuple as ltt)


def estimate_distribution(data: list[int] | list[float]) -> tuple[str, float, float]:
    standart_distributions = StandDist.get_values()
    res = [ks_test(data, type_) for type_ in standart_distributions]
    p_list = [res_tuple[1] for res_tuple in res]
    d_list = [res_tuple[0] for res_tuple in res]
    chosen_dist = standart_distributions[p_list.index(max(p_list))]
    chosen_p = max(p_list)
    chosen_d = d_list[p_list.index(max(p_list))]
    return ltt([chosen_dist, chosen_p, chosen_d])
