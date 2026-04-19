#%%
"""
# Data Preparation

![Data Preparation](images/crisp-dm/datapreparation.png)

**CRISP-DM phase:** Data Preparation  
**Learning objectives:**
- Handle missing values using appropriate strategies (drop, impute, fill)
- Identify and correct inconsistent categorical entries
- Convert columns to appropriate data types (nominal, ordinal, one-hot)
- Remove outliers and duplicate rows

**Estimated time:** ~90 minutes
"""

#%%
"""
## Motivation: Data Is Never Ready Out of the Box

In a real DS project, the gap between raw data and model-ready data is where most of the work happens. Real datasets arrive with:
- **Missing values** — sensors fail, forms are skipped, records are lost
- **Inconsistent entries** — "F", "female", "Female" all meaning the same thing
- **Wrong types** — a column labeled `int64` that is actually a nominal category
- **Outliers** — a negative age, a temperature reading of 999 °C

Data Preparation is not glamorous, but skipping it silently corrupts every downstream step. A model trained on dirty data learns the dirt.

**The business question for this session:**  
*Given a dataset with typical collection errors, which issues are present, what is the right strategy for each, and what does the cleaned result look like?*
"""

#%%
"""
## Importing Basic Modules
"""

#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from pandas.plotting import scatter_matrix
from pandas.api.types import CategoricalDtype

#%%
"""
## 1. Loading the data
"""

#%%
"""
We start by loading the dataset. It is defined in a `csv` file so we load it directly to a pandas data frame using `read_csv()`.

"""

#%%
data=pd.read_csv('data/dataPreparation.csv')

#%%
data

#%%
"""
## 2. Getting to know the data
"""

#%%
"""
Please use the code elements you learned in the notebook "1 Getting to Know the Data":
"""

#%%
"""
- Display the first five rows of the data
"""

#%%
# Your code here


#%%
"""
- Display the information about the data 
"""

#%%
# Your code here


#%%
"""
**Questions:**
- how many data entries are there?
- how many columns are there?
- are there any missing values? How many? In which column?
"""

#%%
"""
**Answer:**

"""

#%%
"""
- Display the statistical information of the numerical data
"""

#%%
# Your code here


#%%
"""
Execute the following code. Does this plot display useful information?
"""

#%%
data.plot.box()

#%%
"""
Create a scatter matrix for the data:
"""

#%%
# Your code here


#%%
"""
**Question:** Are there any attributes that might be correlated?
"""

#%%
"""
**Answer:**
"""

#%%
"""
## 3. Filling in missing values
"""

#%%
"""
In the data frame we have missing values: each one value is missing in column `B`, `D` and `E`.

We will now look at three different methods to deal with the missing values. As the data set is random, this is used to demonstrate how we could handle missing values. For real data we need of course to carefully investigate the data and make a well informed decision.

As a hint we will always mention "*after careful deliberation we decided to*".
"""

#%%
"""
First we are interested in taking a look at the rows with `na`s. In order to do so we use Boolean indexing. We write a function so we can call it later to easily check whether we solved all problems:
"""

#%%
def printNARows(data):
    # First we create the Boolean mask for na values
    mask=pd.isna(data)
    # We remember that Boolean values are numeric data types: True has the value of 1 and False of 0
    # we now create a vector with the sums of the rows
    sums=mask.sum(axis=1)
    # and now we select the rows where the sum is >=1 (i.e. there is at least one na)
    naFrame=data[sums>0]
    print(naFrame)

#%%
"""
When removing `NA` values, data is changed. We should never modify / change the originial data. Therefore we copy the data into a new data frame. We do this usinging the `copy()` method. This ensures that data is copies into a new data frame. Otherwise we create a second variable pointing to the same data frame. 
"""

#%%
"""
### 3.1 Copying data frames using `copy()`
"""

#%%
"""
We create a sample data frame:
"""

#%%
theDF=pd.DataFrame({"A":[10,20,30,40],"B":[11,21,31,41]})


#%%
theDF

#%%
"""
Let's create a copy using the method `copy()`:
"""

#%%
theCopy=theDF.copy()

#%%
"""
and modify the `A` value in the first row in the copy:
"""

#%%
theCopy.loc[0,"A"]=33

#%%
"""
and let's display `theCopy` and `theDF`
"""

#%%
theCopy

#%%
theDF

#%%
"""
`theDF` is unchanged.
Now let's create a "copy" by initializing a new variable with `theDF` using the assignment operator `=`:
"""

#%%
theCopy2=theDF

#%%
"""
and let's modify the value in `B` in the first row:
"""

#%%
theCopy2.loc[0,"B"]=100

#%%
"""
and let's display `theCopy2` and `theDF`
"""

#%%
theCopy2

#%%
theDF

#%%
"""
The original data frame was modified!

the `B` value in `theCopy` was not modified:
"""

#%%
theCopy

#%%
"""
### 3.2 Filling in missing values
"""

#%%
"""
In order to avoid modifying data, we first create a copy and work on the copy of the data:
"""

#%%
dataDF=data.copy()

#%%
# We call the function
printNARows(dataDF)

#%%
"""
We now assume we carefully investigated the rows with the missing data.
Lets take a look at the different values of column `B`:
"""

#%%
dataDF['B'].unique()

#%%
"""
The values are either `yes` or `no`. We count the values:
"""

#%%
dataDF['B'].value_counts()

#%%
"""
The method `value_counts()` ignores `na`s. *After careful deliberation we decided to* **replace** the `na` with **the most frequent value**, that is a `no`.
"""

#%%
dataDF.loc[15,'B']='no'

#%%
"""
And now we again display the `na` rows:
"""

#%%
printNARows(dataDF)

#%%
"""
*After careful deliberation we decided to* **replace** the `na` for the `D` value in row 8 **with the mean value** of the column:
"""

#%%
dataDF.loc[8,'D']=dataDF['D'].mean()

#%%
"""
And we check again the `na` rows:
"""

#%%
printNARows(dataDF)

#%%
"""
Unfortunately we cannot solve the problem with the last `na`. We assume that this is an indication for an errorneous data collection so *after careful deliberation we decided to* **drop the whole row**:
"""

#%%
dataNoNA=dataDF.dropna()
printNARows(dataNoNA)

#%%
"""
We will now continue working with `dataNoNA`.
"""

#%%
"""
### 3.3 `pandas` Methods
"""

#%%
"""
In this example we handled each NaN individually. `pandas` also offers automatic strategies — useful when you want to apply a single rule across many columns:

| Method | Behaviour |
|--------|-----------|
| `dropna()` | Remove rows (or columns) that contain any NaN |
| `fillna(value)` | Replace all NaNs with a fixed value |
| `fillna(df.mean())` | Replace each NaN with the column mean |
| `ffill()` | Forward-fill: propagate the last valid value forward |
| `bfill()` | Backward-fill: use the next valid value to fill back |
| `interpolate()` | Fill using an interpolation method |

Each strategy encodes an assumption about *why the value is missing*. Choose accordingly.
"""

#%%
"""
## 4. Examining Column `A`
"""

#%%
"""
Let's take a look at the boxplot of column `A` alone:
"""

#%%
dataNoNA['A'].plot.box()

#%%
"""
It looks very regular. But this should be no surprise: when we take a closer look at the data, we realize that it is an index. So this column does not contain any specific information. We evaluate the situation and determine that it is not important to keep this index for our analysis. Therefore, we simply **drop the column** (of course if we needed to refer back to the data object, we should keep the index. In this assignment we simply do many things to learn how they are done!) and **save the result in a new data frame** `df1`. 
"""

#%%
df1=dataNoNA.drop('A',axis=1)

#%%
df1.head()


#%%
"""
## 5. Examining Column `B`
"""

#%%
"""
Let's take a look at column `B`. 
"""

#%%
df1.B.unique()

#%%
"""
This column has two different values. As `dtype` `object` is specified. But by understanding the data we realize that the data is categorical. So we add a new column with categorical data.

**Hint**: In fact this categorical data is nominal, as we cannot specify an order.
"""

#%%
df1['B_cat']=df1['B'].astype('category')

#%%
df1.info()

#%%
"""
**Hint:** There is no general rule whether you should keep the original column and add a new one or, after adding the column with categorical `B` values delete the original `B` column. In this example we will delete (drop) the original column.
"""

#%%
df1=df1.drop('B',axis=1)

#%%
"""
## 6. Examining Column `C`
"""

#%%
"""
Let's take a look at the boxplot for column `C`.
"""

#%%
df1.C.plot.box()

#%%
"""
It really looks a bit weird. When we look at the numerical data (type `int64`) we see that there are only two different values:
"""

#%%
df1.C.value_counts()

#%%
"""
When investigating the attribute we learn that the values `1` and `0` are not numerical but *ordinal* attributes, with `0` < `1`. We want that the values are treated as categories and not as numbers, as average values, etc., are not defined (i.e. do not make sense). Therefore, we create a new column for the `C` attribute as **ordinal type**:
"""

#%%
cat_dtype = CategoricalDtype(categories=[0,1], ordered=True)

df1['C_ord']=df1.C.astype(cat_dtype)

#%%
df1.info()

#%%
"""
Please check out the differences.
"""

#%%
df1.B_cat.dtype

#%%
df1.C_ord.dtype

#%%
df1.describe()

#%%
"""
**Hint:** We will equally drop the original C column, as we do not want any average values for the ordinal values 0 and 1 to be displayed in a summary like the one above.
"""

#%%
df1=df1.drop('C',axis=1)

#%%
"""
## 7. Examining Columns `D` and `E` 
"""

#%%
"""
The columns `D` and `E` are numerical floating point data. We can take a look at the boxplots. In order to only display the boxplots for those two data, we need to create a new data frame
"""

#%%
(df1.loc[:,['D','E']]).plot.box()

#%%
"""
## 8. Examining the `age` column
"""

#%%
"""
Column `age` contains the age in form of an integer. Let's take a look at the boxplot:

"""

#%%
(df1.loc[:,['age']]).plot.box()

#%%
"""
This looks weird. So let's check the statistical summary of data:

"""

#%%
df1.age.describe()

#%%
"""
We have a negative `age` value which is apparently wrong. 
"""

#%%
"""
Now let's take a look at the row(s) with a negative age:
"""

#%%
df1.loc[df1.age<0,:]

#%%
"""
We see that it is one single row. There must be a data entry error. Let's assume, the data was collected anonymously, so we do not know, how to fix it. We drop the row:

"""

#%%
df1=df1.drop(16,axis=0)

#%%
"""
and check the result:
"""

#%%
df1.age.describe()

#%%
"""
A histogram might be helpful to display the age disctribution: 
"""

#%%
sns.histplot(df1.age,kde=True)

#%%
"""
## 9. Examining the column `gender`
"""

#%%
"""
Now let's take a look at the column `gender`. First we will display the unique values:
"""

#%%
df1.gender.unique()

#%%
"""
And here we see now a problem that might be a result of data entry: `F` and `female` are both values for  `female`. `M`, `m` and `male` are all values for `male`. Additionally the attribute is an `object` and not a category.

First we will fix the wrong entries by replacing the values with the correct values.

To do so we use the method `replace()`. Using the parameter `inplace=True` we modify the original data frame.
"""

#%%
df1.replace({"gender":{"F":"female","M":"male","m":"male"}}, inplace=True)

#%%
"""
The `replace()` method expects a dictionary. A dictionary is defined inside `{}` and consists of key-value pairs. First the key is specified followed by a `:` and the value.
In above code we state that we want to apply the `replace()` method to the column `gender`. As value we specify a second dictionary that contains as keys the values to be replaces and as values the new values. So we state that "F" should be replaced by "female", "M" by "male" and "m" by "male". The singe key-value pairs are separated by commas. 

We coulds equally specify values in other columns to be replaced.

With the keyword argument `inplace=True` we speciify that the values should be replaced in the original data frame and not on a copy, that would then be returned by the method.
"""

#%%
"""
And we control the result:
"""

#%%
df1.gender.unique()

#%%
"""
Now we need to modify the type of the column to a category (not an ordinal value). Please proceed as explained above and create a new column named `genderCat` and drop the origial `gender` category:
"""

#%%
# Your code here


#%%
"""
Let's check the result:
"""

#%%
df1.info()

#%%
"""
## 9. Examining the column `country`
"""

#%%
"""
Let's take a look at the values of the column `country`:
"""

#%%
df1.country.unique()

#%%
"""
Here we equally have the problem of errornous entries. Please correct the wrong entries as above. Use `India`, `Germany`, `France` and `UK` as the correct entries: 
"""

#%%
# Your code here


#%%
"""
Let's check the solution:
"""

#%%
df1.country.unique()

#%%
"""
Let's count the data objects per value:
"""

#%%
df1.country.value_counts()

#%%
"""
And now let's create a plot that displays the counts of the country data
"""

#%%
sns.countplot(df1,x='country')

#%%
"""
We can now distinguish the number of counts per gender (please ignore the Furure Warning):
"""

#%%
sns.countplot(df1,x='country',hue='genderCat')

#%%
"""
Here we can, e.g. see, that the gender distribution differs significantly per country. (Keep in mind, this is just an artificial data set for this lab assignment, so this does not really mean anything.)
"""

#%%
"""
We can equally display the percentage:
"""

#%%
sns.countplot(df1,x='country',hue='genderCat',stat="percent")

#%%
"""
Now we want to modify the type of the `country` column. The `country` shall be (for whatever reason) an ordinal attribute. The order is defined by the population size in descending order. 
"""

#%%
from pandas.api.types import CategoricalDtype

#Your code

cat_dtype = CategoricalDtype(categories=['India','Germany','UK',"France"], ordered=True)

df1['countryOrd']=df1.country.astype(cat_dtype)

#%%
"""
## 10. Some statistical information
"""

#%%
"""
As already seen, we display statistical information for numeric / quantitative attributes using `describe()`:
"""

#%%
df1.describe()

#%%
"""
Let's take a look at the mean values of `D` and `E`:
"""

#%%
df1[['D','E']].mean()

#%%
"""
With `groupby()` we can calculate this information (or the sum or the minimum etc) per one attribute, e.g. the county:
"""

#%%
df1.groupby('country')[['D','E']].mean()

#%%
"""
`groupby()` equally works on different levels:
"""

#%%
df1.groupby(['country','genderCat','B_cat'], observed=False)[["D","E"]].mean()

#%%
"""
In two lines you can see an `NaN`. This indicates that there are no data objects with the respective combination of values of country, gender and `B_cat`. This is not displayed if we set observed to `True`.
"""

#%%
df1.groupby(['country','genderCat','B_cat'],observed=True)[["D","E"]].mean()

#%%
"""
Many Machine Learning algorithms cannot cope with multivalues categorical attributes. For this reason often one hot encoding is used to encode categorical values. For each value a boolean column is created.
"""

#%%
df1New=pd.get_dummies(data=df1,columns=["country"])

#%%
df1New

#%%
"""
Now we can store the cleaned data frame to a **csv* file:
"""

#%%
df1New.to_csv("myData/cleanedData.csv")

#%%
"""
**Duplicates** are another common data quality issue. `pandas` provides:
- `duplicated()` — returns a boolean Series flagging duplicate rows
- `drop_duplicates()` — removes them

Always inspect duplicates before dropping: not every row that looks identical is necessarily an error (e.g., two people with the same age and country are not duplicates).
"""

#%%
"""
## 11. Exercise
"""

#%%
"""
Load `dataPreparation_Exercise.csv` — a dataset capturing course, study hours, gender, country, age, and grades. It contains the full range of data quality issues from this notebook.

Work through the complete preparation pipeline:
1. Load the file and inspect it (shape, types, missing values, statistics)
2. Identify and fix inconsistent entries in categorical columns
3. Handle missing values — justify each decision in a comment
4. Remove any true duplicate rows (check first, then drop)
5. Convert categorical columns to the appropriate type (nominal or ordinal)
6. Save the cleaned data to `myData/cleanedData_exercise.csv`
"""

#%%
data2 = pd.read_csv('data/dataPreparation_Exercise.csv')

# Your code here


#%%
"""
---
## CRISP-DM Checkpoint: Step Back

**Where are we in the process?** Data Preparation

**What did we do?** *(fill in after completing the exercise)*  
- Which NaN handling strategy did you choose for each missing column, and why?
- Which columns needed type conversion, and what type is correct?
- How many rows did you lose through cleaning? Is that acceptable?

**Translate for a stakeholder:**  
In 1–2 sentences, without technical jargon: what was wrong with the raw data, and is the cleaned version trustworthy enough to train a model on?

**What comes next?**  
With clean, correctly typed data, we move to **Modelling** — but only after we have chosen the right algorithm for the problem at hand.
"""
