import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import os
import warnings
import pyarabic.araby as strip_harakat
import re

df = pd.read_csv('Text1.csv')
df["TextAfter"]=''
for x in range(0,len(df)):
	text = df["Text"][x]
    strip_harakat(text)
    df["TextAfter"][x] = text

df.to_csv('Text1after1.csv', index=False)
