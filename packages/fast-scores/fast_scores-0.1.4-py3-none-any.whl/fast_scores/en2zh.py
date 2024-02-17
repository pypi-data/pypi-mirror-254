"""Translate english to chinese via a dict."""
from typing import List, Union

import copy
from fast_scores.word_tr import word_tr


# fmt: off
def en2zh(
        text: Union[str, List[List[str]]],
) -> List[str]:
    # fmt: on
    """Translate english to chinese via a dict.

    Args
        text: to translate, list of list of str

    Returns
        res: list of str
    """
    res = copy.deepcopy(text)
    if isinstance(text, str):
        res = [text.split()]

    # if res and isinstance(res[0], str):
        # res = [line.lower().split() for line in res]

    res = ["".join([word_tr(word) for word in line]) for line in res]

    return res
