# Step 1: Import Libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 2: Load Dataset
df = pd.read_csv('Datasets/Social_Network_Ads.csv')


# Step 3: Explore Dataset
print(df.info())
print(df.describe())
print(df.head())


# Step 4: Check for Missing and Duplicate Values
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())


# Step 5: Encode Categorical Column
encoder = LabelEncoder()
df['Gender'] = encoder.fit_transform(df['Gender'])  # Male = 1, Female = 0


# Step 6: Feature Scaling
features = ['Age', 'EstimatedSalary', 'Gender']
scaler = StandardScaler()
X = scaler.fit_transform(df[features])
y = df['Purchased']








# Step 7: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Step 8: Train Naive Bayes Model
model = GaussianNB()
model.fit(X_train, y_train)


# Step 9: Predict
y_pred = model.predict(X_test)


# Step 10: Evaluate Performance
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

