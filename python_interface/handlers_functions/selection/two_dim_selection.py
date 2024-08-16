from rpy2 import robjects as r_obj
from handlers_functions.selection.one_dim_selection import list_is_integer as is_int


def get_cor_coef(data_fst: list[int] | list[float], data_scnd: list[int] | list[float]) -> float:
    if is_int(data_fst) and is_int(data_scnd):
        r_data_x: r_obj.IntVector | r_obj.FloatVector = r_obj.IntVector(data_fst)
        r_data_y: r_obj.IntVector | r_obj.FloatVector = r_obj.IntVector(data_scnd)
    else:
        r_data_x: r_obj.IntVector | r_obj.FloatVector = r_obj.FloatVector(data_fst)
        r_data_y: r_obj.IntVector | r_obj.FloatVector = r_obj.FloatVector(data_scnd)
    r_cor = r_obj.r["cor"]
    return float(r_cor(r_data_x, r_data_y).r_repr())
