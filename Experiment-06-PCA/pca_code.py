# Step 1: Import Libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load Dataset
df = pd.read_csv('Datasets/Social_Network_Ads.csv')

# Step 3: Explore Basic Information
print(df.info())
print(df.describe())
print(df.head())

# Step 4: Check for Missing and Duplicate Values
print("Missing Values:\n", df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())

# Step 5: Handle Missing/Duplicate Values
df.drop_duplicates(inplace=True)

# Step 6: Encode Categorical Columns (if any)
encoder = LabelEncoder()
df['Gender'] = encoder.fit_transform(df['Gender'])  # Male=1, Female=0

# Step 7: Feature Scaling
features = ['Age', 'EstimatedSalary', 'Gender']
x = df[features]
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Step 8: Apply PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(x_scaled)

# Step 9: Analyze Explained Variance
print("Explained Variance Ratio:", pca.explained_variance_ratio_)

# Step 10: Visualize PCA Result
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
pca_df['Purchased'] = df['Purchased']


plt.figure(figsize=(8,6))
sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='Purchased', palette='Set1')
plt.title('PCA Result')
plt.show()

# Step 11: Reduced Dataset for Further Use
print(pca_df.head())
