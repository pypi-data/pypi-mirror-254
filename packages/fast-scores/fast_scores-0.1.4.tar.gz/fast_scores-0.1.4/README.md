# fast-scores
[![tests](https://github.com/ffreemt/fast-scores/actions/workflows/routine-tests.yml/badge.svg)][![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/fast_scores.svg)](https://badge.fury.io/py/fast_scores)

Calculate correlatioin matrix fast

## Preinstall fasttext

```
pip install fasttext
```

For Windows without a C/C++ compiler:
* Download a proper whl (e.g., `fasttext‑0.9.2‑cp36‑cp36m‑win_amd64.whl` for 64bits Python 3.6 etc)  from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#fasttext](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fasttext)
```bash
pip install fasttext*.whl
```
or (for python 3.8)
```
pip install https://github.com/ffreemt/ezbee/raw/main/data/artifects/fasttext-0.9.2-cp38-cp38-win_amd64.whl
```
## Installation
```
pip install fast-scores
```

## Usage

```shell
# from fast-scores\tests\test_gen_cmat.py

from fast_scores.gen_cmat import gen_cmat

text_en = "test this\nbla bla\n love"
text_zh = "测试\n 爱\n吃了吗\n你好啊"

list1 = [elm.strip() for elm in text_en.splitlines() if elm.strip()]
list2 = [elm.strip() for elm in text_zh.splitlines() if elm.strip()]

cmat = gen_cmat(list1, list2)  # len(list2) x len(list1)
print(cmat)
# [[0.75273851 0.         0.        ]
#  [0.         0.         0.86848247]
#  [0.         0.         0.        ]
#  [0.         0.         0.        ]]

len_y, len_x = cmat.shape

assert cmat.max() > 0.86  # 0.868
_ = divmod(cmat.argmax(), len_x)
assert cmat[_] == cmat.max()

```