#  Enter all standard functions here
import enum


def list_is_integer(some_list: list[int] | list[float]) -> bool:
    for val in some_list:
        if isinstance(val, float):
            return False
    return True


def convert_list_to_tuple(some_list) -> tuple:
    return tuple(some_list)


class Rtype(enum.Enum):
    norm: str = "norm"
    pois: str = "pois"
    binom: str = "binom"

    @classmethod
    def get_values(cls):
        return list(map(lambda c: c.value, cls))
