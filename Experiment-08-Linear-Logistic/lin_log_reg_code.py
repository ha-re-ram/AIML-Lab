# Step 1: Import Libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report

# Step 2: Load Dataset
df = pd.read_csv('Datasets/Social_Network_Ads.csv')


# Step 3: Explore Data
print(df.info())
print(df.describe())
print(df.head())


# Step 4: Preprocessing
# Encode Gender
df['Gender'] = LabelEncoder().fit_transform(df['Gender'])  # Male=1, Female=0


# Feature Scaling
scaler = StandardScaler()
df[['Age', 'EstimatedSalary']] = scaler.fit_transform(df[['Age', 'EstimatedSalary']])


# Step 5: Prepare Feature and Target
# Linear Regression: Predict salary from age
X_lin = df[['Age']]
y_lin = df['EstimatedSalary']
# Logistic Regression: Predict Purchased
X_log = df[['Age', 'EstimatedSalary', 'Gender']]
y_log = df['Purchased']

# Step 6: Split Data
X_lin_train, X_lin_test, y_lin_train, y_lin_test = train_test_split(X_lin, y_lin, test_size=0.2, random_state=42)
X_log_train, X_log_test, y_log_train, y_log_test = train_test_split(X_log, y_log, test_size=0.2, random_state=42)


# Step 7: Train Models
lin_model = LinearRegression()
lin_model.fit(X_lin_train, y_lin_train)


log_model = LogisticRegression()
log_model.fit(X_log_train, y_log_train)


# Step 8: Make Predictions
y_lin_pred = lin_model.predict(X_lin_test)
y_log_pred = log_model.predict(X_log_test)


# Step 9: Evaluate Models
# Linear Regression Evaluation
print("Linear Regression Evaluation:")
print("MSE:", mean_squared_error(y_lin_test, y_lin_pred))
print("R2 Score:", r2_score(y_lin_test, y_lin_pred))


# Logistic Regression Evaluation
print("\nLogistic Regression Evaluation:")
print("Accuracy:", accuracy_score(y_log_test, y_log_pred))
print("Confusion Matrix:\n", confusion_matrix(y_log_test, y_log_pred))
print("Classification Report:\n", classification_report(y_log_test, y_log_pred))

