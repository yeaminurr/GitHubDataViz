import pandas as pd
import numpy as np
datasetissueshortnot_othersc = pd.read_csv("datasetissueshortnot_othersc.csv")
print("okauy")
def newview(month):
  global datasetissueshortnot_othersc
  print("Iam okay")
  temp = datasetissueshortnot_othersc.copy()
  temp = temp[temp["just_month"]==month]
  temp = temp[temp['Closed At'].notna()]
  temp = temp.groupby(["types"])["types"].count()

  temp.to_csv("temp.csv")
  return "hello"





#newview("2022-01-01")



