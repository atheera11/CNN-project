import re
import pandas as pd

my_dataset = pd.read_csv("Text1clean11(1).csv", encoding='utf-8')
my_dataset["Text_clean14"]=''

for x in range(0,len(my_dataset)):
 text = my_dataset["Text_clean13"][x]
 def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)
 my_dataset["Text_clean14"][x] = (deEmojify(text))


my_dataset.to_csv("Text1clean11(1).csv", index=False)
