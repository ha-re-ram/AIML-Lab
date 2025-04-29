EX.NO : 5
Data Preprocessing on Social Network Ads Dataset


AIM:
To take a sample dataset and apply suitable data preprocessing techniques like cleaning, encoding, scaling, and splitting for machine learning.

PROCEDURE:
Step 1: Import Libraries
 Use necessary Python libraries like pandas, sklearn, and numpy.


Step 2: Load Dataset
 Load the CSV file using pandas.read_csv() function.


Step 3: Explore Basic Information
Use .info() to view column types and non-null counts.
Use .describe() to view statistical details like mean, std dev, min, max, etc.


Step 4: Preview the Data
 Use .head() to view the first few rows of the dataset.


Step 5: Check for Duplicates and Missing Values
Use .duplicated().sum() to find duplicate rows.
Use .isnull().sum() to find null/missing values.


Step 6: Check Unique Values
 Use .nunique() to see how many unique values are in each column.


Step 7: Handle Missing or Duplicate Values (if any)
 Drop or fill missing/duplicate values using dropna() or fillna().


Step 8: Encode Categorical Data
 Convert the Gender column (Male/Female) to numeric format (e.g., Male = 1, Female = 0).


Step 9: Scale Numerical Features
 Standardize features like Age and EstimatedSalary using StandardScaler.


Step 10: Split Dataset into Train and Test Sets
 Use train_test_split() to divide the dataset into 80% training and 20% testing data.


Step 11: Preprocessed Data
	Display the shapes and sample values of the preprocessed data to verify the steps.

