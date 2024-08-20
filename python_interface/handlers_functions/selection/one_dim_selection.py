from rpy2 import robjects as r_obj


def list_is_integer(some_list: list[int] | list[float]) -> bool:
    for val in some_list:
        if isinstance(val, float):
            return False
    return True


def get_sort_data(data: list[int] | list[float]) -> list[int] | list[float]:
    return sorted(data)


def get_chosen_middle(data: list[int] | list[float]) -> float:
    if list_is_integer(data):
        r_data: r_obj.IntVector | r_obj.FloatVector = r_obj.IntVector(data)
    else:
        r_data: r_obj.IntVector | r_obj.FloatVector = r_obj.FloatVector(data)
    r_mean = r_obj.r["mean"]
    return float(r_mean(r_data).r_repr())


def get_based_chosen_disp(data: list[int] | list[float]) -> float:
    if list_is_integer(data):
        r_data: r_obj.IntVector | r_obj.FloatVector = r_obj.IntVector(data)
    else:
        r_data: r_obj.IntVector | r_obj.FloatVector = r_obj.FloatVector(data)
    r_var = r_obj.r["var"]
    return float(r_var(r_data).r_repr())


def get_unbased_chosen_disp(data: list[int] | list[float], mean: float | None = None) -> float:
    if mean is None:
        mean = get_chosen_middle(data)
    chosen_disp: float = sum((val - mean) ** 2 for val in data) / len(data)
    return chosen_disp


def get_chosen_median(sorted_data: list[int] | list[float]) -> float | int:
    if list_is_integer(sorted_data):
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
