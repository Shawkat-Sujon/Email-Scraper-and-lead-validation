import pandas as pd
import numpy as np
i = 0
df1 = pd.read_excel('Automation_demo_1.xlsx')
df2 = pd.read_excel('scrape_data.xlsx')
#print(df2[0][4])
mail = df1['DirectEmail'][i]
df3 = df2[0].where(df2[0] == mail)
df4 = df3.dropna()
print(mail)
#print(type(mail))
print(df4)
if df4[0] == mail:
    print('valid')
else:
    print('Invalid')

