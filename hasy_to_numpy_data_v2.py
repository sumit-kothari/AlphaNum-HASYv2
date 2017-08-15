import numpy as np
import pandas as pd
import string
from PIL import Image


INPUT_DATASET_BASEPATH = "HASYv2_data/"
# hasy data with labels
INPUT_DATASET = "HASYv2_data/hasy-data-labels.csv"

# output numpy dataset
OUTPUT_DATASET_X = "output_data_alpha_num/alphanum-hasy-data-X"
OUTPUT_DATASET_y = "output_data_alpha_num/alphanum-hasy-data-y"


# create a list of all alphanumeric characters
TEST_DATA_LOWER_CASE = list(string.ascii_lowercase)
TEST_DATA_UPPER_CASE = list(string.ascii_uppercase)
TEST_DATA_NUMBERS = list(range(0, 10))
TEST_DATA_NUMBERS = [str(s) for s in TEST_DATA_NUMBERS]

TEST_DATA_LOWER_CASE.extend(TEST_DATA_UPPER_CASE)
TEST_DATA_LOWER_CASE.extend(TEST_DATA_NUMBERS)

TEST_DATA_ALL = TEST_DATA_LOWER_CASE

print("alphanumeric characters length = ", len(TEST_DATA_ALL))

# load input data set of hasy data with labels
df = pd.read_csv(INPUT_DATASET)
df["latex"] = df["latex"].str.strip()

# filter hasy data for only alphanumeric characters
df = df[df.latex.isin(TEST_DATA_ALL)]

print(df.head(2))
print(df.shape)


# Create numpy array X = images and y = corresponding lables

X = []
y = []

for index, row in df.iterrows():
    print(INPUT_DATASET_BASEPATH + row['path'], row['symbol_id'], row["latex"])
    im = Image.open(INPUT_DATASET_BASEPATH + row['path'])
    im = im.convert('L')
    im = np.asarray(im)

    y.append(row['symbol_id'])
    X.append(im)

X = np.array(X)
y = np.array(y)

print(X.shape)
print(y.shape)


# print labels vs frequency matrix
unique, counts = np.unique(y, return_counts=True)
print(np.asarray((unique, counts)).T)
print("lables = ", len(unique))

np.save(OUTPUT_DATASET_X, X)
np.save(OUTPUT_DATASET_y, y)
