# 🧪 Experiment 05 - Data Preprocessing

## 🎯 AIM
To take a sample dataset and apply suitable data preprocessing techniques like cleaning, encoding, scaling, and splitting to prepare it for machine learning.

---

## 📂 Dataset Used

- **Name**: Social Network Ads  
- **Source**: [Kaggle - Social Network Ads Dataset](https://www.kaggle.com/datasets/rakeshrau/social-network-ads)  
- **Description**: This dataset contains user demographic data such as age, gender, and salary, and whether they purchased a product after seeing an ad. Useful for binary classification problems.

---

## ⚙️ Tools & Libraries Used

- **Python 3**
- **Pandas**
- **NumPy**
- **Scikit-learn**

---

## 📋 PROCEDURE

### Step 1: Import Libraries  
Use necessary Python libraries like `pandas`, `sklearn`, and `numpy`.

### Step 2: Load Dataset  
Load the CSV file using `pandas.read_csv()`.

### Step 3: Explore Basic Information  
Use `.info()` to view column types and non-null counts.  
Use `.describe()` to view statistical summaries (mean, std dev, etc.).

### Step 4: Preview the Data  
Use `.head()` to view the first few rows of the dataset.

### Step 5: Check for Duplicates and Missing Values  
Use `.duplicated().sum()` to find duplicate rows.  
Use `.isnull().sum()` to find missing/null values.

### Step 6: Check Unique Values  
Use `.nunique()` to check how many unique values exist in each column.

### Step 7: Handle Missing or Duplicate Values  
If present, drop or fill missing values using `dropna()` or `fillna()`.  
Remove duplicates if necessary.

### Step 8: Encode Categorical Data  
Convert categorical variables (like Gender) to numeric format using `LabelEncoder`.

### Step 9: Scale Numerical Features  
Standardize features like Age and EstimatedSalary using `StandardScaler`.

### Step 10: Split Dataset  
Use `train_test_split()` to divide data into 80% training and 20% testing sets.

### Step 11: Verify Preprocessed Data  
Print the shape and preview of the processed dataset using `.shape` and `.head()`.

---

## ✅ RESULT

The dataset was successfully preprocessed:
- Cleaned nulls and checked for duplicates.
- Encoded categorical data.
- Scaled numerical values.
- Split into training and testing sets.

The final dataset is now ready for building machine learning models.

---

## 📁 Files in This Folder

- `Preprocessing_code.py` - Python script containing all preprocessing steps.
- `Social_Network_Ads.csv` - Original dataset from Kaggle.
- `output.txt`

---

## 🧠 Next Steps
You can now apply classification models like Logistic Regression or Decision Trees on this cleaned dataset for prediction.

