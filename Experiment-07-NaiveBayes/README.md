# Experiment 07 – Naive Bayes Classifier

## 🎯 Aim
To implement and demonstrate the working of the **Naive Bayes classifier** on a real-life application dataset.

## 📂 Dataset
- **Dataset Name:** Social Network Ads
- **Source:** [Kaggle - Social Network Ads Dataset](https://www.kaggle.com/datasets/rakeshrau/social-network-ads)
- **Description:** The dataset contains user demographic data and whether they purchased a product based on social media ads.

### 📊 Features Used
- `Gender`
- `Age`
- `EstimatedSalary`
- `Purchased` (Target variable)

## 🧠 Procedure

### Step 1: Import Libraries  
Import required libraries like `pandas`, `sklearn`, `numpy`, etc.

### Step 2: Load the Dataset  
Read the CSV file using `pandas.read_csv()`.

### Step 3: Data Preprocessing  
- Encode categorical features (`Gender` to 0/1).
- Standardize numerical features (`Age`, `EstimatedSalary`) using `StandardScaler`.
- Separate input features (X) and target variable (y).

### Step 4: Train-Test Split  
Split the dataset into training and testing sets using `train_test_split()` (80% train, 20% test).

### Step 5: Train Naive Bayes Classifier  
Use `GaussianNB()` from `sklearn.naive_bayes` to train the classifier on the training data.

### Step 6: Make Predictions  
Predict the target for the test set using `.predict()`.

### Step 7: Evaluate the Model  
Use:
- `accuracy_score`
- `confusion_matrix`
- `classification_report`

### Step 8: Save Outputs  
- Save printed outputs to `output.txt`
- (Optional) Save predictions or evaluation results in a CSV if needed.

## 💻 Files in this Folder

| File Name                  | Description                                        |
|---------------------------|----------------------------------------------------|
| `NaiveBayes_code.py`      | Python script for training & evaluating the model  |
| `Social_Network_Ads.csv`  | Input dataset                                      |
| `output.txt`              | Model evaluation metrics and predictions           |

## 📌 Output Sample (from `output.txt`)
```text
Accuracy: 0.875
Confusion Matrix:
[[50  3]
 [ 7 20]]
Classification Report:
              precision    recall  f1-score   support
           0       0.88      0.94      0.91        53
           1       0.87      0.74      0.80        27
