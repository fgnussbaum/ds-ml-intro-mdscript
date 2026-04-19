#%%
"""
# Getting to Know Your Data

![Data Understanding](images/crisp-dm/dataunderstanding.png)

**CRISP-DM phase:** Data Understanding  
**Learning objectives:**
- Load a tabular dataset and inspect its structure using pandas
- Use descriptive statistics and visualizations to characterize data
- Identify missing values and understand why they matter
- Ask diagnostic questions before reaching for any model

**Estimated time:** ~90 minutes
"""

#%%
"""
## Motivation: Diagnose Before You Model

A research team has collected physical measurements from iris flowers — sepal length, sepal width, petal length, petal width — across three species. The goal is eventually to build a classifier that identifies species from measurements alone.

**But before any model runs, a data scientist asks:**
- What does this data actually look like?
- Are there gaps, outliers, or encoding problems that would silently break a model?
- Do the three species actually differ in measurable ways — or is this a hopeless task from the start?

This is the **Data Understanding** phase of CRISP-DM. Its job is *diagnosis*, not prescription. You are not yet cleaning data (that is Data Preparation) and you are definitely not yet modeling. You are building a picture.

**The business question for this session:**  
*What patterns are visible in the iris measurement data, and is the data quality sufficient to train a reliable classifier?*
"""

#%%
"""
## Your Primary Tool: the pandas DataFrame

The central data structure for tabular data in Python is the **DataFrame** from the `pandas` library. Think of it as a spreadsheet that lives in code: rows are observations, columns are variables, and every column has a name you can address directly.

In this notebook you will load a real dataset into a DataFrame, explore its structure, and build the habit of asking questions *about the data* before asking questions *of the data*.
"""

#%%
"""
A DataFrame is a two-dimensional table: rows are observations, columns are named variables. Columns can hold different data types (numbers, text, categories). You can add, remove, filter, and transform rows and columns — and every operation leaves a traceable, reproducible record in your notebook.

Data for a DataFrame typically comes from a **CSV file** (comma-separated values). Read one with `pd.read_csv('path/to/file.csv')`. Some datasets are bundled directly with libraries like `seaborn` — no file needed.
"""

#%%
"""
We will use the **Iris dataset** — 150 observations of iris flowers, each described by four physical measurements (sepal length, sepal width, petal length, petal width) and a species label. It is a clean, well-documented dataset that lets us focus on the exploration workflow rather than data wrangling. It is available directly from `seaborn`.
"""

#%%
"""
## 3. Importing Required Python Modules
"""

#%%
"""
We will need some basic modules:

- `pandas` implements the class DataFrame that we get to know in this notebook
- `seaborn` provides statistical plots and some basic data sets like the iris flower data set, and
- `matplotib.pyplot` provides basic (MATLAB like) plotting functionality.

We will thus import all three modules first.
"""

#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%%
"""
## 4. Loading the data
"""

#%%
"""
Load the Iris dataset from `seaborn` and store it in a variable. Then display it — Jupyter renders DataFrames as a table.
"""

#%%
iris=sns.load_dataset('iris')

#%%
iris

#%%
"""
**Question:**

How many rows and columns does the `iris` data frame have? What are the types of the columns? Can you make a guess?
"""

#%%
"""
**Answer:**


"""

#%%
"""
## 5. Getting to know the data
"""

#%%
"""
A DataFrame comes with a rich set of methods for inspection. Methods are called as `variable.method()`. Work through the exercises below — call each method on `iris`, observe the output, and add a short comment describing what you see.
"""

#%%
"""
- the method `head()` to **display the top 5 rows**. If you pass an integer value `n` as parameter (`head(n)`), the top `n` rows are displayed. 
"""

#%%
# Your code here


#%%
"""
- the method `tail()` to **view the bottom rows**. If you pass an integer value `n` as parameter, the bottom `n` rows are displayed. 
"""

#%%
# Your code here


#%%
# Your code here


#%%
"""
- Attributes of objects are accessed using the variable name and a dot followed by the attribute name: `variableName.attributeName`.
<p>Display the following attribute values (using the `print()` function) and describe their values in a comment:</p>

    - `index`
    - `columns`
    - `shape`
    - `axes`

"""

#%%
# Your code here


#%%
"""
- the method `info()` summarizes information about the data frame.
"""

#%%
# Your code here


#%%
"""
- the method `describe()` gives a statistical overview of the numerical data.
"""

#%%
# Your code here


#%%
"""
## 6. Accessing data in the data frame
"""

#%%
"""
Data Columns (series) can be easily accessed using the column name like an attribute:
"""

#%%
iris.sepal_length

#%%
"""
The column name can equally be used inside `[]` to access the series. Don't forget to use quotation marks around the column name.
"""

#%%
iris['sepal_length']

#%%
"""
`loc` can be used to access single elements (rows) or to create slices:
"""

#%%
#second row
iris.loc[1]

#%%
#second row
iris.loc[1,'sepal_length']

#%%
# the firsth three rows
iris.loc[0:2]

#%%
"""
Please note that the slice indices are **inclusive**.
"""

#%%
# rows 10 to 15, petal_length and petal_width
iris.loc[10:15,['petal_length', 'petal_width']]

#%%
"""
We can use boolean values in an index vector to access data.
The third quartile, Q3, of sepal_length is 6.4. Let's create a boolean array that has `True` if the length is > 6.4, `False` otherwise:
"""

#%%
booleanArray=iris.sepal_length>6.4

#%%
print(booleanArray)

#%%
"""
We can now use this array to display/access only the rows where sepal_length is > 6.4:
"""

#%%
iris.loc[booleanArray]

#%%
"""
or store the result in a new data frame:
"""

#%%
largeSepalLength=iris.loc[booleanArray]

#%%
"""
Let's check by displaying the statistics:
"""

#%%
largeSepalLength.describe()

#%%
"""
With `iloc` access to columns and rows is possible in the same way as with `numpy` arrays: 
"""

#%%
iris.iloc[1:3,:]

#%%
"""
Please note, the (end-)index in `iloc` is **exclusive**!

Values in the data frame are accessed with `iloc` using the index. 
"""

#%%
"""
By contrast the (end-)index in `loc` is **inclusive**!
"""

#%%
iris.loc[1:3,:]

#%%
"""
`loc` enables the access to columns using columns names also.
"""

#%%
iris.loc[1:3,'sepal_width']


#%%
"""
Use lists to access different columns by names or equally specific rows:
"""

#%%
iris.loc[1:3,['sepal_width','petal_width']]


#%%
iris.loc[[2,4,6,8],['sepal_width','petal_width']]


#%%
"""
## 7. Derived Features: Arithmetic on Columns

Arithmetic operations on DataFrames work **element-wise** across entire columns. This is useful when you want to derive a new feature from existing measurements — for example, computing a ratio or normalizing a value.
"""

#%%
"""
As an example: the ratio of petal length to sepal length might capture something about the flower's proportions that neither measurement alone expresses.
"""

#%%
iris['petal_ratio'] = iris['petal_length'] / iris['sepal_length']

#%%
iris[['sepal_length', 'petal_length', 'petal_ratio', 'species']].head(10)

#%%
"""
**Exercise:** Create a new column `sepal_ratio` that holds the ratio of sepal width to sepal length. Then display the mean of `sepal_ratio` grouped by species — does this ratio differ between species?
"""

#%%
# Your code here


#%%
"""
## 8. Missing Values

Real measurement data rarely arrives complete. Sensors fail, readings are out of range and discarded, forms are left blank. Python represents missing values as `NaN` (Not a Number). Knowing where your NaNs are — and how many — is one of the first things to check in Data Understanding.
"""

#%%
"""
We load a small synthetic file (`NATest.csv`) that has intentional missing entries — a stand-in for what you will encounter with real sensor data.
"""

#%%
data=pd.read_csv('data/NATest.csv')

#%%
data

#%%
"""
Let's taka a look:
"""

#%%
data.info()

#%%
"""
`NaN` indicates a missing value. Most aggregation functions (`sum()`, `mean()`, `median()`, `cumsum()`) silently skip NaNs and compute over the remaining values — which can be misleading if you are not aware of how many are missing.
"""

#%%
data['Value 1'].sum()

#%%
data['Value 1'].cumsum()

#%%
data['Value 1'].mean()

#%%
data.describe()

#%%
"""
To test a value for `NaN`, the comparison operator `==` is not working. You need to apply the method `isna()` or `notna()`:
"""

#%%
data['Value 1'].isna()

#%%
data['Value 2'].notna()

#%%
"""
We can thus count the `NaN` values by simply using the `sum()` method:
"""

#%%
print('Value 1 has',data['Value 1'].isna().sum(),'NaN values')

#%%
"""
## 9. Plots
"""

#%%
"""
Visualization is the fastest way to spot patterns, outliers, and structure that summary statistics miss. We use pandas built-in plots and `seaborn` for more expressive statistical graphics.
"""

#%%
"""
Let's go back to the iris data set:
"""

#%%
iris=sns.load_dataset('iris')
iris.columns

#%%
"""
A small scatter plot of sepal length versus sepal width:
"""

#%%
iris.plot.scatter(x='sepal_length',y='petal_length')

#%%
"""
Instead of a 3-D plot the value of a third dimension, here the petal width, can be added as color coding.
"""

#%%
iris.info()

#%%
iris.plot.scatter(x='sepal_length',y='petal_length',c='petal_width')

#%%
"""
We can also use a third value to control the size of the points:
"""

#%%
iris.plot.scatter(x="sepal_length", y="sepal_width", s=iris["petal_width"] * 10);

#%%
"""
In order to color the dots according to the classes we need a categorial column for the class. In order not to modify the data, we copy our data frame and modify the copy:
"""

#%%
myIris=iris.copy()
myIris["class"] = myIris["species"].astype("category")
myIris.plot.scatter(x='sepal_length',y='petal_length',c='class',cmap="viridis")

#%%
"""
We can easily create boxplots for the different attributes.
"""

#%%
iris.plot.box()

#%%
"""
Or a scatter matrix:
"""

#%%
from pandas.plotting import scatter_matrix

#%%
scatter_matrix(iris, alpha=0.2, figsize=(6, 6), diagonal="kde");

#%%
"""
Seaborn offers additional plotting possiblities. A `hue` parameter allows for coloring the dots according to the class. As we need a categroical attribute, we use our copies data frame `myIris` with the newly created colum:
"""

#%%
myIris=iris.copy()
myIris["class"] = myIris["species"].astype("category")
sns.scatterplot(x=myIris.sepal_length,y=myIris.sepal_width,hue=myIris['class'])

#%%
"""
## 10. Exercise: The penguin data
"""

#%%
"""
The **Palmer Penguins** dataset records physical measurements (bill length, bill depth, flipper length, body mass) from three penguin species in Antarctica. It has a different structure than Iris — including some missing values.

Apply the full Data Understanding workflow from this notebook to the penguin data:
1. Load the dataset with `sns.load_dataset('penguins')`
2. Check its shape, column types, and missing values
3. Produce at least two visualizations that tell you something about species differences
4. In a markdown cell, write 2–3 sentences: *what did you learn, and is the data quality sufficient to build a species classifier?*
"""

#%%
penguins = sns.load_dataset('penguins')

# Your code here


#%%
"""
---
## CRISP-DM Checkpoint: Step Back

**Where are we in the process?** Data Understanding

**What did we find?** *(fill in after completing the exercises)*  
- How many rows and columns does the Iris dataset have?
- Are there missing values?
- Which features seem most useful for distinguishing species?

**Translate for a stakeholder:**  
In 1–2 sentences, without using the words "DataFrame", "NaN", or "feature": what would you tell the research team about the data they collected?

**What comes next?**  
If the data has quality issues (missing values, outliers, wrong types), the next step is **Data Preparation** — cleaning and transforming before any model is trained.
"""
