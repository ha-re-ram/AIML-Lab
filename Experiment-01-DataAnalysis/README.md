# 🧪 AIML Experiment 1 – Data Analysis & Visualization

This experiment demonstrates how to generate a sample dataset and perform basic statistical operations and visualizations using Python libraries like `pandas`, `numpy`, `matplotlib`, and `seaborn`.

---

## 🎯 Aim

To create a synthetic dataset and explore statistical operations such as mean, median, and mode using Pandas, and visualize the results using various plotting techniques.

---

## 🧾 Files Included

- `data_generator.py` – Script to generate synthetic employee data and save it to `employee_data.csv`.
- `analysis_visualization.py` – Loads the dataset, performs analysis, and generates visual plots.
- `employee_data.csv` – Auto-generated dataset containing random records of employees.

---

## ⚙️ Procedure

1. Import required libraries like `pandas`, `numpy`, `matplotlib.pyplot`, and `seaborn`.
2. Generate a synthetic dataset with fields like Name, Age, Department, and Salary.
3. Load and inspect the dataset using `.head()`, `.info()`, and `.describe()`.
4. Handle missing values and check for duplicates.
5. Perform statistical operations: mean, median, mode.
6. Create shallow and deep copies of the dataset.
7. Visualize data using:
   - Bar Chart (e.g., department vs count)
   - Count Plot
   - Pie Chart (e.g., gender distribution)
   - Histogram (e.g., salary distribution)
   - Scatter Plot (e.g., age vs salary)
   - Box Plot (to detect outliers)
   - Correlation Heatmap (using seaborn)

---

## 💡 Features

- 📦 Data generation using NumPy and Pandas
- 📊 Multiple chart types for insights
- 🧼 Data cleaning and preparation
- 🔍 Central tendency calculations
- 🧪 Exploratory Data Analysis (EDA)

---

## ▶️ How to Run

1. **Generate the dataset**
   ```bash
   python data_generator.py
