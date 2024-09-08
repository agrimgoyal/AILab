# -*- coding: utf-8 -*-
"""Agrim-102215080-Assignment2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n2Wvb6RCWpnN5EibrGbOZcLFuRyOuGBG

1. Generate the following matrix in numpy

A =


1 2 3
4 5 6
7 8 9



and modify the entries to

B =


1 999 999
4 999 999
7 8 9


"""

import numpy as np

A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
A[(A > 1) & (A < 7) & (A != 4)] = 999
print(A)

"""2. Consider the system of equations
3x + 2y = 5
10x − y = 3
Find the unique solution to these equations using matrix calculus in
Numpy array.
"""

import numpy as np

A = np.array([[3, 2],[10, -1]])
b = np.array([5, 3])
det = np.linalg.det(A)
inv = np.linalg.inv(A)
solution = np.dot(inv, b)
print(f"The solution is x = {solution[0]}, y = {solution[1]}")

"""3. Generate a 5 by 5 random matrix and find the maximum, minimum,
average (mean) & variance values along all axes.
"""

import numpy as np
A = np.random.randint(3,12,size = (5,5))
print("Mean: ", A.mean())
print("Max: ", A.max())
print("Min: ", A.min())
print("Variance: ", A.var())

"""4. Generate a 5 by 5 random integer matrix whose values are between 2 & 100. Find the another matrix which produces boolean output as true
where Values of random matrix are between 20 & 70.
"""

import numpy as np
A = np.random.randint(2,100,size = (5,5))
B = (A > 20) & (A < 70)
print(A)
print(B)

"""5. Find the mean square error between two array A = [1,2,3,4,5,6] & B =
[7,8,9,10,12,17] using function in Numpy module.
"""

import numpy as np
A = np.array([1,2,3,4,5,6])
B = np.array([7,8,9,10,12,17])
mse = np.mean((A - B)**2)
mse

"""6. Create a Normalized random variable of size 20 using Numpy and find
out each quantile & their corresponding counts.

"""

import numpy as np
A = np.random.rand(20)
A = (A - A.min()) / (A.max() - A.min())
A

"""Create a Normalized random variable of size 20 using Numpy and find
out each quartile & their corresponding counts.
"""

import numpy as np
A = np.random.rand(20)
A = (A - np.percentile(A, 25)) / (np.percentile(A, 75) - np.percentile(A, 25))
A

"""7. Find out the eigen value and eigen vectors of covariance of the data matrix,
X=[[4,11],[8,4],[13,5],[7,14]] where each row is one observation while colums are
attribures of that observation. (Hint: Question is related to PCA & use np.cov
and np.linalg.eig functions of numpy package)
"""

import numpy as np
X = np.array([[4,11],[8,4],[13,5],[7,14]])
cov = np.cov(X.T)
eigenvalues, eigenvectors = np.linalg.eig(cov)
print(eigenvalues)
print(eigenvectors)

"""Create a pandas data structure (series) X using a dictionary D = "Rohan":
176,"John": 175,"Harvinder": 180,"Hasan": 174 . Then pass other list
["Tinku","John","Ramesh","Hasan"] as index into series X . Comment on
the resultant output & locate the index of NAN values.
"""

import pandas as pd
D = {"Rohan": 176,"John": 175,"Harvinder": 180,"Hasan": 174}
X = pd.Series(D, index = ["Tinku","John","Ramesh","Hasan"])
print(X)
print(X.isna())

"""Draw four line plots using the subplot() function.
Use the following data:
For line 1: x = [0, 1, 2, 3, 4, 5] and y = [0, 100, 200, 300, 400, 500]
For line 2: x = [0, 1, 2, 3, 4, 5] and y = [50, 20, 40, 20, 60, 70]
For line 3: x = [0, 1, 2, 3, 4, 5] and y = [10, 20, 30, 40, 50, 60]
For line 4: x = [0, 1, 2, 3, 4, 5] and y = [200, 350, 250, 550, 450, 150]
"""

import matplotlib.pyplot as plt

# Data for each line
x1, y1 = [0, 1, 2, 3, 4, 5], [0, 100, 200, 300, 400, 500]
x2, y2 = [0, 1, 2, 3, 4, 5], [50, 20, 40, 20, 60, 70]
x3, y3 = [0, 1, 2, 3, 4, 5], [10, 20, 30, 40, 50, 60]
x4, y4 = [0, 1, 2, 3, 4, 5], [200, 350, 250, 550, 450, 150]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x1, y1, label='Line 1', color='blue')
axs[0, 0].set_title('Line 1')
axs[0, 0].grid(True)

axs[0, 1].plot(x2, y2, label='Line 2', color='green')
axs[0, 1].set_title('Line 2')
axs[0, 1].grid(True)

axs[1, 0].plot(x3, y3, label='Line 3', color='red')
axs[1, 0].set_title('Line 3')
axs[1, 0].grid(True)

axs[1, 1].plot(x4, y4, label='Line 4', color='purple')
axs[1, 1].set_title('Line 4')
axs[1, 1].grid(True)

plt.tight_layout()
plt.show()

"""10. Using the following data plot a bar plot and a horizontal bar plot.
company = [”Apple”, ”Microsoft”, ”Google”, ”AMD”]
profit = [3000, 8000, 1000, 10000]
"""

import matplotlib.pyplot as plt

company = ["Apple", "Microsoft", "Google", "AMD"]
profit = [3000, 8000, 1000, 10000]

plt.bar(company, profit)
plt.xlabel("Company")
plt.ylabel("Profit")
plt.title("Bar Plot of Company Profits")
plt.show()

"""11. Using the following data to plot a box plot.
import numpy as np
box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)
"""

import matplotlib.pyplot as plt
import numpy as np

box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)

data = [box1, box2]

plt.boxplot(data)
plt.xlabel("Box")
plt.ylabel("Value")
plt.title("Box Plot")
plt.show()

"""12. You have a dataset containing sales data for a retail store. Design a program using
pandas to:
(a) Load the dataset into a pandas DataFrame.
(b) Calculate the total sales revenue for each month.
(c) Identify the top-selling product for each month.
(d) Visualize the monthly sales trend using a line plot.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('retail_sales_dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['Total Amount'].sum()
monthly_product_sales = df.groupby(['Month', 'Product Category'])['Quantity'].sum().reset_index()
top_selling_product = monthly_product_sales.loc[monthly_product_sales.groupby('Month')['Quantity'].idxmax()]

plt.figure(figsize=(10, 6))
plt.plot(monthly_revenue.index.astype(str), monthly_revenue.values, marker='o')
plt.title('Monthly Sales Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales Revenue')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()