import seaborn as sns
import pandas as pd

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
print(df.head)
print('\n')

def add_10(n):
    return n+10

df_map = df.applymap(add_10)
print(df_map.head())