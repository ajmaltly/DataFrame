# -*- coding: utf-8 -*-
"""pandas.DataFrame.merge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z3324XA5qgxYgNrNs5vaACu9W6anrFCa
"""

import pandas as pd
df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]})
df1

df1.merge(df2, left_on='lkey', right_on='rkey')

df1.merge(df2, left_on='lkey', right_on='rkey',
          suffixes=('_left', '_right'))

df1 = pd.DataFrame({'a': ['foo', 'bar'], 'b': [1, 2]})
df2 = pd.DataFrame({'a': ['foo', 'baz'], 'c': [3, 4]})
df1

df2

df1.merge(df2, how='inner', on='a')

df1.merge(df2, how='left', on='a')

df1 = pd.DataFrame({'left': ['foo', 'bar']})
df2 = pd.DataFrame({'right': [7, 8]})
df1

df2

df1.merge(df2, how='cross')