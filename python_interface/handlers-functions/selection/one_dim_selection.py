from rpy2.robjects.packages import importr
from rpy2 import robjects as r_obj

# imports the base module for R.
base = importr("base")

# imports the utils package for R.
utils = importr("utils")


def list_is_integer(some_list: list[int] | list[float]) -> bool:
    for val in some_list:
        if isinstance(val, float):
            return False
    return True


def get_sort_data(data: list[int] | list[float]) -> r_obj.IntVector | r_obj.FloatVector:
    r_data: r_obj.IntVector | r_obj.FloatVector
    if list_is_integer(data):
        r_data = r_obj.IntVector(data)
    else:
        r_data = r_obj.FloatVector(data)
    r_sort = r_obj.r['sort']
    return r_sort(r_data)


def get_chosen_middle(sorted_data: r_obj.IntVector | r_obj.FloatVector):
    r_mean = r_obj.r['mean']
    return r_mean(sorted_data)



#################################_TEST ZONE_######################################################
res1 = get_sort_data([4, 2, 5, 6, 7, 1, 10])
print(res1.r_repr())
res2 = get_chosen_middle(res1)
print(res2.r_repr())
