import argparse
import time
from functools import wraps

import numba
import numpy as np

# cython
# ctypes
# python C module
# cffi
# pybynd11

parser = argparse.ArgumentParser(
    prog="Numba/Numpy micro experiment."
)
parser.add_argument("-o", "--output-csv", action="store_true")

_RECORDS = []


def _get_implementation_optimization(function_name: str) -> tuple[str, str]:
    split_name = function_name.split("_", 2)

    if len(split_name) == 1:
        return split_name[0], "vanilla"

    return split_name


def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        seconds = end - start
        _RECORDS.append(list((seconds, *_get_implementation_optimization(fn.__name__))))
        return result

    return wrapper


@timeit
def loops(l1: int, l2: int, l3: int) -> int:
    res = 0
    for i1 in range(l1):
        res += i1 * 1000
        for i2 in range(l2):
            res += i2 * 100
            for i3 in range(l3):
                res += i3 * 10
    return res


@timeit
@numba.njit
def loops_njit(l1: int, l2: int, l3: int) -> int:
    res = 0
    for i1 in range(l1):
        res += i1 * 1000
        for i2 in range(l2):
            res += i2 * 100
            for i3 in range(l3):
                res += i3 * 10
    return res


@timeit
@numba.jit
def loops_jit(l1: int, l2: int, l3: int) -> int:
    res = 0
    for i1 in range(l1):
        res += i1 * 1000
        for i2 in range(l2):
            res += i2 * 100
            for i3 in range(l3):
                res += i3 * 10
    return res


@timeit
def builtins(l1: int, l2: int, l3: int) -> int:
    return (1000 * sum(range(l1))) + (l1 * 100 * sum(range(l2))) + (l1 * l2 * 10 * sum(range(l3)))


@timeit
@numba.jit
def builtins_jit(l1: int, l2: int, l3: int) -> int:
    return (1000 * sum(range(l1))) + (l1 * 100 * sum(range(l2))) + (l1 * l2 * 10 * sum(range(l3)))


@timeit
@numba.njit
def builtins_njit(l1: int, l2: int, l3: int) -> int:
    return (1000 * sum(range(l1))) + (l1 * 100 * sum(range(l2))) + (l1 * l2 * 10 * sum(range(l3)))


@timeit
def fnnumpy(l1: int, l2: int, l3: int) -> int:

    return np.concatenate(
        (
            l1 * l2 * (10 * np.arange(l3)),
            l1 * (100 * np.arange(l2)),
            (1000 * np.arange(l1)),
        )
    ).sum()


@timeit
@numba.jit
def fnnumpy_jit(l1: int, l2: int, l3: int) -> int:

    return np.concatenate(
        (
            l1 * l2 * (10 * np.arange(l3)),
            l1 * (100 * np.arange(l2)),
            (1000 * np.arange(l1)),
        )
    ).sum()


@timeit
@numba.njit
def fnnumpy_njit(l1: int, l2: int, l3: int) -> int:

    return np.concatenate(
        (
            l1 * l2 * (10 * np.arange(l3)),
            l1 * (100 * np.arange(l2)),
            (1000 * np.arange(l1)),
        )
    ).sum()


def main():
    l = (239, 357, 3650)
    parsed_args = parser.parse_args()

    res = {
        loops(*l),
        loops_njit(*l),
        loops_jit(*l),
        builtins(*l),
        fnnumpy(*l),
        fnnumpy_jit(*l),
        fnnumpy_njit(*l),
        builtins_jit(*l),
        builtins_njit(*l),
    }

    assert len(res) == 1

    if parsed_args.output_csv:
        print("seconds,implementation,optimization")
        for record in _RECORDS:
            print(*record, sep=",")


if __name__ == "__main__":
    main()
