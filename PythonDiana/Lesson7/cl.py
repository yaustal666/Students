#%%
import pandas as pd 
df = pd.read_csv('data.csv')
df.head(10)

#%%
df.info()

#%%
df.describe()

#%%
df.isna().sum()

#%%
ls = list(df.columns)
ls.remove("GENDER")
ls.remove("AGE")
ls.remove("LUNG_CANCER")
ls

# for i in ls:
#     print(i, df[df[i] > 2].sum().sum())


#%%
(~df["SMOKING"].between(1, 2)).sum()

#%%
df[ls] = df[ls] - 1

#%%
df

#%%
def foo(s):
    return s - 1

# df[ls].apply(foo)
df[ls].apply(lambda s: s - 1)

#%%
df[ls].map(lambda s: s - 1)

#%%