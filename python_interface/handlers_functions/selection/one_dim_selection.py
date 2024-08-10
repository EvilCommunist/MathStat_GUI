from rpy2 import robjects as r_obj


def list_is_integer(some_list: list[int] | list[float]) -> bool:
    for val in some_list:
        if isinstance(val, float):
            return False
    return True


def get_sort_data(data: list[int] | list[float]) -> list[int] | list[float]:
    return sorted(data)


def get_chosen_middle(sorted_data: list[int] | list[float]) -> float:
    r_data: r_obj.IntVector | r_obj.FloatVector
    if list_is_integer(sorted_data):
        r_data = r_obj.IntVector(sorted_data)
    else:
        r_data = r_obj.FloatVector(sorted_data)
    r_mean = r_obj.r['mean']
    return float(r_mean(r_data).r_repr())


def get_chosen_disp(sorted_data: list[int] | list[float], mean: float) -> float:
    chosen_disp: float = sum((val-mean)**2 for val in sorted_data)/len(sorted_data)
    return chosen_disp


def get_chosen_median(sorted_data: list[int] | list[float]) -> float:
    r_data: r_obj.IntVector | r_obj.FloatVector
    chosen_median: float | int
    if list_is_integer(sorted_data):
        r_data = r_obj.IntVector(sorted_data)
        r_median = r_obj.r['median']
        chosen_median = int(r_median(r_data).r_repr())
    else:
        r_data = r_obj.FloatVector(sorted_data)
        r_median = r_obj.r['median']
        chosen_median = float(r_median(r_data).r_repr())
    return chosen_median


def get_quartile(sorted_data: list[int] | list[float], num_of_quantile: int = 1) -> float | int:
    if num_of_quantile < 0 or num_of_quantile > 4:
        print("Некорректное значение квартиля")
        return 0
    return sorted_data[int(len(sorted_data)*0.25*num_of_quantile)]
