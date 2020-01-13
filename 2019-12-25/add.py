from typing import List
from itertools import chain


def add(*args: List[List[float]]) -> List[List[float]]:
    nested_lengths = [len(k) for k in list(chain(*args))]
    lengths = [len(k) for k in args]
    if not (len(set(lengths)) == len(set(nested_lengths)) == 1):
        raise ValueError('Given matrices are not the same size.')

    output_list = []
    for l in zip(*args):
        output_list.append([sum(k) for k in zip(*l)])
    return output_list
