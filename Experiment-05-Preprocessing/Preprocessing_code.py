# Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# Load the dataset
df = pd.read_csv('Social_Network_Ads.csv')

# 1. Get basic info about the dataset
print("\nDataset Info:")
df_info = df.info()  # Info about data types and non-null values
print(df_info)

# 2. Describe the dataset for statistical summary
print("\nDataset Description:")
df_description = df.describe()  # Summary statistics for numerical columns
print(df_description)

# 3. Check for duplicate rows
duplicates = df.duplicated().sum()
print("\nNumber of Duplicate Rows:", duplicates)

# 4. Check for unique values in each column
print("\nUnique Values in Each Column:")
unique_values = df.nunique()
print(unique_values)

# 5. Check for missing (null) values
print("\nMissing Values in Each Column:")
missing_values = df.isnull().sum()
print(missing_values)

# Display first few rows of the dataset
print("Initial Dataset:\n", df.head())

# 6. Handle Missing Values
imputer = SimpleImputer(strategy='mean')
df[['Age', 'EstimatedSalary']] = imputer.fit_transform(df[['Age', 'EstimatedSalary']])

# 7. Encode Categorical Variables (Gender)
encoder = LabelEncoder()
df['Gender'] = encoder.fit_transform(df['Gender'])  # Male = 0, Female = 1

# 8. Feature Scaling (Normalization/Standardization)
scaler = StandardScaler()
df[['Age', 'EstimatedSalary']] = scaler.fit_transform(df[['Age', 'EstimatedSalary']])

# 9. Splitting the dataset into Training and Test sets
X = df[['Age', 'EstimatedSalary', 'Gender']]
y = df['Purchased']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 10. Display pre-processed dataset
print("\nProcessed Dataset:\n", df.head())