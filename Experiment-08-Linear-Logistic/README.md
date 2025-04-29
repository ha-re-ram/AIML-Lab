# Experiment 08 – Prediction System using Linear and Logistic Regression

## 🎯 Aim
To develop a prediction system using **Linear Regression** and **Logistic Regression** models on a real-world dataset.

## 📂 Dataset
- **Dataset Name:** Social Network Ads
- **Source:** [Kaggle - Social Network Ads Dataset](https://www.kaggle.com/datasets/rakeshrau/social-network-ads)
- **Description:** The dataset contains demographic details of users and whether they purchased a product after viewing an ad.

### 📊 Features Used
- `Age`
- `EstimatedSalary`
- `Gender` (encoded)
- `Purchased` (Target variable)

## 🧠 Procedure

### Step 1: Import Required Libraries  
Import `pandas`, `numpy`, `sklearn`, and optionally `matplotlib` for visualization.

### Step 2: Load the Dataset  
Use `pandas.read_csv()` to load the dataset.

### Step 3: Data Preprocessing  
- Encode the categorical column `Gender` to numeric format.
- Standardize features like `Age` and `EstimatedSalary` using `StandardScaler`.
- Separate features (X) and target variable (y).

### Step 4: Split the Dataset  
Use `train_test_split()` to split the dataset into training (80%) and testing (20%) sets.

### Step 5: Apply Linear Regression  
- Train a `LinearRegression` model.
- Predict the output on test data.
- Evaluate using metrics like R² score, MSE.

### Step 6: Apply Logistic Regression  
- Train a `LogisticRegression` model on the same data.
- Predict the target class.
- Evaluate using `accuracy_score`, `confusion_matrix`, and `classification_report`.

### Step 7: Save Output  
Store evaluation results of both models in a text file (`output.txt`) for documentation.

## 💻 Files in this Folder

| File Name                    | Description                                         |
|-----------------------------|-----------------------------------------------------|
| `Regression_code.py`        | Python script for linear and logistic regression    |
| `Social_Network_Ads.csv`    | Input dataset                                       |
| `output.txt`                | Model evaluation metrics for both regression models |

## 📌 Output Sample (from `output.txt`)
```text
--- Linear Regression ---
R² Score: 0.54
MSE: 0.19

--- Logistic Regression ---
Accuracy: 0.89
Confusion Matrix:
[[52  2]
 [ 5 21]]
Classification Report:
              precision    recall  f1-score   support
           0       0.91      0.96      0.93        54
           1       0.91      0.81      0.86        26
