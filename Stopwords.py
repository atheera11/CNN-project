import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re

my_dataset = pd.read_csv("Text1clean11.csv", encoding='utf-8')
my_dataset["Text_clean"]=''
for x in range(0,len(my_dataset)):
  Tex = re.sub('@[^\\s]+', ' ', my_dataset["Text_clean"][x])
  Tex = re.sub("ة", "ه", my_dataset["Text_clean"][x])
  Tex = re.sub("وووو", "و", my_dataset["Text_clean"][x])
  text = text.strip()
  text = re.sub("[إأٱآا]", "ا", text)
  text = re.sub("ى", "ي", text)
  text = re.sub("ؤ", "ء", text)
  text = re.sub("ئ", "ء", text)
  text = re.sub("ة", "ه", text)
  noise = re.compile(""" ّ    | # Tashdid
  	                             َ    | # Fatha
  	                             ً    | # Tanwin Fath
  	                             ُ    | # Damma
  	                             ٌ    | # Tanwin Damm
  	                             ِ    | # Kasra
  	                             ٍ    | # Tanwin Kasr
  	                             ْ    | # Sukun
  	                             ـ     # Tatwil/Kashida
  	                         """, re.VERBOSE)
  text = re.sub(noise, '', text)
  text = re.sub(r'(.)\1+', r"\1\1", text)  # Remove longation


my_dataset.to_csv('Text1clean11.csv', index=False)