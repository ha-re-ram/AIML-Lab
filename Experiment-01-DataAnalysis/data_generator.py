#Code for random data set creation
import numpy as np
import pandas as pd
departments = ['HR', 'Finance', 'Engineering', 'Marketing']
employee_data = pd.DataFrame({
'EmployeeID': range(1, 101),
'Age': np.random.randint(22, 60, 100),
'Department': np.random.choice(departments, 100),
'Salary': np.random.randint(40000, 150000, 100)
})
employee_data.to_csv('Experiment-01-DataAnalysis/employee_data.csv', index=False)
