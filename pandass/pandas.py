import numpy as np
import panda as pd
dict = { "name":['harry','rohan','roju','sonu'],
         "marks":[90,65,82,99],
         "city":['jodhpur','jaupur','dehli','bihar']
         }
df = pd.DataFrame(dict) # change into excel file
print(df)
