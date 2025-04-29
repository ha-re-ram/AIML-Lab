# Experiment 06 – Principal Component Analysis (PCA)

## 🎯 Aim
To perform dimensionality reduction using Principal Component Analysis (PCA) on a large dataset and visualize the variance retained after transformation.

## 📂 Dataset
- **Dataset Name:** Social Network Ads
- **Source:** [Kaggle - Social Network Ads Dataset](https://www.kaggle.com/datasets/rakeshrau/social-network-ads)
- **Attributes Used:**
  - `Gender`
  - `Age`
  - `EstimatedSalary`
  - `Purchased` (Target)

## 🧠 Procedure

### Step 1: Import Libraries  
Import required libraries such as pandas, sklearn, numpy, etc.

### Step 2: Load Dataset  
Use `pandas.read_csv()` to load the dataset.

### Step 3: Preprocess the Data  
- Drop irrelevant columns (e.g., User ID).
- Encode categorical features (e.g., Gender → 0 and 1).
- Separate features and target.
- Standardize features using `StandardScaler`.

### Step 4: Apply PCA  
- Use `sklearn.decomposition.PCA`.
- Choose `n_components=2` to reduce data to 2 dimensions.
- Fit and transform the scaled data.

### Step 5: Save Output  
- Redirect print outputs to `output.txt`.
- Save transformed data with principal components into `PCA_Transformed_Data.csv`.

## 💻 Files in this Folder

| File Name                  | Description                                     |
|---------------------------|-------------------------------------------------|
| `PCA_code.py`             | Python script performing PCA on dataset         |
| `Social_Network_Ads.csv`  | Input dataset used for PCA                      |
| `output.txt`              | Console output redirected and saved             |
| `PCA_Transformed_Data.csv`| PCA output saved as CSV                         |

## 📌 Output Sample (in `output.txt`)
```text
Explained Variance Ratio: [0.9246, 0.0753]
PCA Components Shape: (400, 2)
