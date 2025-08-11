import pandas as pd

# Replace with your file name
df = pd.read_csv("salary_data.csv")
df.head()  # Preview first 5 rows
df.isnull().sum()     # Count NaN values
df = df.dropna()      # Drop rows with NaN (or fill them)
salary_by_Experince = df.groupby('Salary')['Experience'].sum()
print(salary_by_Experince)
import matplotlib.pyplot as plt

# Line chart
x=df['Experience']
y=df['Salary']
plt.title('Salary vs Experience')
plt.xlabel("Salary")
plt.ylabel('Experience')
plt.plot(x,y)
plt.show()