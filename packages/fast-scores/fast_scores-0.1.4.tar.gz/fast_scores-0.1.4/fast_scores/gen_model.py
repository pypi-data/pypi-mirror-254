"""Gen a tfidf model."""
from typing import List, Union
from sklearn.feature_extraction.text import TfidfVectorizer

from logzero import logger


# fmt: off
def gen_model(
        text: Union[str, List[str]],
        max_features: int = 1000,
) -> TfidfVectorizer:
    # fmt: on
    """Gen a tfidf model.

    Args:
        text: space delimited words/chinese chars/numbers
            or normal Chinese text: see token_pattern below
    Returns:
        TfidfVectorizer
    """
    # patt = re.compile(r"[一-龟]|\d+|[a-zA-Z]+")

    # model = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b", max_features=max_features).fit(text)

    # TfidfVectorizer needs a list
    if isinstance(text, str):
        text = [text]

    try:
        model = TfidfVectorizer(
            token_pattern=r"[一-龟]|\d+|[a-zA-Z]+",
            max_features=max_features,
        ).fit(text)
    except Exception as e:
        logger.error(e)
        raise
        # raise SystemExit(1) from e

    return model
