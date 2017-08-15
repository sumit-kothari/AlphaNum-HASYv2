# AlphaNum-HASYv2

This repository contains **Alpha-Numeric Handwritten Dataset** stored in Python [Numpy] array; and is sub-set of dataset from [HASYv2].

> [HASYv2] contains 32px x 32px images of 369 symbol classes while **AlphaNum-HASYv2** contains 32px x 32px images of 62 (or 0-61) symbol classes (0-1 = 10, A-Z = 26, a-z = 26)

# Pre-generated Numpy dataset
Under `output_data_alpha_num` directory two files are present, which are as followed:

  - `alphanum-hasy-data-X.npy` : Contains images data-set with size (4658, 32, 32)
  - `alphanum-hasy-data-y.npy` : Contains labels data-set with size (4658,)
  
# Regenerate Numpy dataset

Assumptions:
  - This code is beign run on MacOS, because I have not tested it on any other OS yet ;)
  - User has cloned this repo successfully and is in root of this project
  - This code is using Python 3.x

***Follow below steps to regenerate dataset:***
0: **Download HASYv2 dataset** (Required only once)
```
$ cd HASYv2_data
$ bash dowload_data.sh
```

1: **Regenerate AlphaNum-HASYv2 dataset**
```
$ cd 'TO_ROOT_PATH_OF_THIS_REPO'
$ pip install -r requirements.txt
$ python hasy_to_numpy_data_v2.py
```
[Numpy]: <http://www.numpy.org/>
[HASYv2]: <https://arxiv.org/abs/1701.08380>

Output file are generated under `output_data_alpha_num` directory
