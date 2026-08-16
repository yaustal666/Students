# RENAMING
df.columns = ['new_col1', 'new_col2', 'new_col3']

# Adds 'raw_' to the front of every column
df = df.add_prefix('raw_')

# Adds '_id' to the end of every column
df = df.add_suffix('_id')

# Equivalent to {"A": "Alpha"}, axis=1
df = df.rename(columns={'A': 'Alpha'})

#get unique values
df["column"].unique()


# changing type
df[" class_participation"] = df[" class_participation"].astype(float)
# changing specifically to numbers
df[' class_participation'] = pd.to_numeric(df[' class_participation'], errors='coerce')


mapping = {'A': 5, 'B': 4, 'C': 3, 'D': 2}
df['grade'] = df['grade'].map(mapping)
#or
df['grade'] = df['grade'].apply(lambda x: mapping.get(x))


# Матрица корреляции
import matplotlib.pyplot as plt
import seaborn as sns

# Compute the matrix
corr_matrix = df.corr()

# Plot the heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()