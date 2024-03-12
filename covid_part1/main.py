import numpy as np
import pandas as pd

print('NumPy', np.__version__)
print('pandas', pd.__version__)

df = pd.read_csv('./data/data.csv')

print(df.head(10))