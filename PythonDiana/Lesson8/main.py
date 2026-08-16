#%%
import pandas as pd 
df = pd.read_csv("student_performance.csv")

# %%
df.isna().sum()
# %%
df.info()
# %%
df.head()

# %%

df = df.rename(columns={
    ' class_participation': "participation",
    ' attendance_percentage': "attendance",
    " total_score": "total_score",
    " grade": "grade"
})
# %%
df = df.rename(columns={
    " weekly_self_study_hours" : "self_study"
})

# %%
df['participation'].unique()

# %%
import numpy as np
df.loc[df["participation"] == "ABOBA", "participation"] = np.nan

# %%
# df["participation"] = df["participation"].astype(float)
df['participation'] = pd.to_numeric(df['participation'], errors='coerce')

# %%
df['participation'] = df['participation'].fillna(df['participation'].median())

# %%
df.nlargest(10, 'total_score')

# %%
df.sort_values(by='total_score', ascending=False).head(10)