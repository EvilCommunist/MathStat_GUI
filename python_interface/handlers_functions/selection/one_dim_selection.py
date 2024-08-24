from rpy2 import robjects as r_obj
from handlers_functions.standard_functions.standart_functions import list_is_integer as is_int


def get_sort_data(data: list[int] | list[float]) -> list[int] | list[float]:
    return sorted(data)


def get_chosen_median(sorted_data: list[int] | list[float]) -> float | int:
    if is_int(sorted_data):
        r_data: r_obj.IntVector | r_obj.FloatVector = r_obj.IntVector(sorted_data)
        r_median = r_obj.r["median"]
        chosen_median: int = int(r_median(r_data).r_repr())
    else:
        r_data: r_obj.IntVector | r_obj.FloatVector = r_obj.FloatVector(sorted_data)
        r_median = r_obj.r["median"]
        chosen_median: float = float(r_median(r_data).r_repr())
    return chosen_median


def get_quartile(sorted_data: list[int] | list[float], num_of_quartile: int = 1) -> float | int | Exception:
    try:
        if num_of_quartile < 0 or num_of_quartile > 4:
            raise Exception("Некорректное значение квартиля")
    except Exception as ex:
        return ex
    return sorted_data[int(len(sorted_data) * 0.25 * num_of_quartile)]
