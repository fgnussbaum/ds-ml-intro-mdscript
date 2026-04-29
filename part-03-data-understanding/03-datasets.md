> **Navigation:** [<-- Data Types and Measurement Scales](02-data-types.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [EDA: Descriptive Statistics -->](04-eda-descriptive-stats.md)

# Datasets

**Requires:** [Data Types and Measurement Scales](02-data-types.md)

**Motivation:** You know that data arrives as collections of typed attributes. But before you can profile, clean, or model a dataset, you need to understand its overall shape: how many records, how many columns, and whether the structure itself creates challenges. This nugget answers: what does first contact with a new dataset look like in practice?

> You will learn the structural properties of tabular datasets — dimensionality, sparsity, and resolution — and practice the first-inspection workflow in pandas using `df.head()`, `df.info()`, and `df.shape` on the ESS Well-Being dataset that will serve as the running example throughout this part.

> **Note:** This nugget covers tabular data, the dominant format in this course. For non-tabular formats (images, text, time series, and spatial data), see [Beyond Tabular Data](..part-zz-appendix/01-beyond-tabular-eda.md).

## Table of Contents

- [From Attributes to a Dataset](#from-attributes-to-a-dataset)
- [Loading and First Inspection](#loading-and-first-inspection)
- [Running Examples for This Part](#running-examples-for-this-part)

---

## From Attributes to a Dataset

You know what a single attribute is. Now, a **dataset** is a collection of objects, each described by the same set of attributes.
Specifically, for tabular datasets,
* the rows correspond to the objects (which are also called records, data objects, instances, or observations),
* the columns correspond to the attributes.

For tabular data, every cell holds the value of one attribute for one record.

Now, let's discuss some of the most important structural properties that datasets can have:

**Dimensionality** refers to the number of attributes, that is, the number of columns. A dataset with many columns is called high-dimensional.

> **Curse of dimensionality (outlook):** High dimensionality causes the so-called curse of dimensionality, where distances between data points lose meaning and algorithms require much more data to generalize.
<!--You'll revisit this in feature selection and model evaluation (TODO: links).-->

**Sparsity** describes datasets or attributes in which most values are zero or absent. Survey datasets and text data are typically sparse: a respondent may have answered only a subset of questions, and documents contain only a tiny fraction of all possible words.

> Sparse data can be stored efficiently with specialized formats that record only the non-zero values.

**Resolution** refers to the granularity at which data was captured. The same underlying phenomenon can look quite different at different resolutions: daily vs. hourly temperature readings, or national vs. city-levek survey responses.

> The resolution to chose depends on the question you are asking. It's a trade-off: Coarser resolution loses detail while requiring less storage space. Finer resolution gives more detail, but may introduce noise.

## Loading and First Inspection

The first thing you do with any new dataset is load it and examine its structure.
Here's a walkthrough for the **ESS 11 Well-Being (Germany)** dataset.

**Load the data.**

```python
import pandas as pd
df = pd.read_csv("ess_wellbeing.csv", sep=",", encoding="utf-8")
```

- The `sep` parameter sets the column delimiter: `,`, `;`, and tab are common. Tab-separated files use `sep="\t"`.

- The `encoding` parameter handles character encoding: `"utf-8"` is the default, European datasets sometimes use `"latin-1"`.

`print(df)` gives a first overview of the loaded data, including row and column count.

It is also possible to take a look at just a few rows with these commands:

```python
df.head()   # first 5 rows
df.head(3)   # first 3 rows
df.tail()   # last 5 rows
```

Check whether values look sensible, headers are readable, and no obvious formatting issues stand out.

**Check the dimensions.**

`df.shape` can also be used to inspect dimension and yield (rows, columns) as result, here `(2420, 11)`.

2,420 records and 12 attributes. One number tells you the dataset's size; the other its dimensionality.


**Check for missing values.**

```python
df.info()   # column names, non-null counts, dtypes
```

`df.info()` adds non-null counts to the dtype information. A column with fewer non-null entries than rows has missing values — something `df.head()` alone would not reveal:

```
 #   Column     Non-Null Count  Dtype
 0   happiness  2417 non-null   float64
 1   health     2417 non-null   float64
 3   gender     2420 non-null   int
```

`happiness` and `health` each have three missing values; `gender` is complete. You will investigate missing values further in the [Data Quality](05-eda-data-quality.md) nugget.

```python
df.dtypes   # dtype per column
```

`Dtype` column shows inferred data type for each column. The inferred is not always correct or optimal: See for example the inferred dtype `float64` for `gender`.

> Always verify dtypes against your domain knowledge before computing statistics or feeding columns into a model.

---

## Running Examples
### ESS 11 Well-Being Dataset (Germany)

We'll actually use the ESS dataset from above as a running example in this script. Time to introduce it a little more:

The **European Social Survey (ESS)** is a large cross-national survey conducted every two years. The dataset used here is the German subset of Round 11, with approximately 2,400 respondents.

We don't use all attributes of the dataset. Also, for presentation in this script, some attributes have been renamed for improved readability and some of their scales recoded. Here are the most important attributes that we'll use:

| Column/Attribute | Scale | Values |
|--------|-------|--------|
| `happiness` | Quasi-continuous (0–10) | 0 = extremely unhappy, 10 = extremely happy |
| `health` | Ordinal | 1 = very bad, 5 = very good |
| `social_meeting_freq` | Ordinal | 1 = never, 7 = every day |
| `gender` | Binary (nominal) | 0 = Female, 1 = Male |
| `age_group` | Ordinal | 1 = 15–24, 7 = 75+ |
| `religiosity` | Quasi-continuous (0–10) | 0 = not religious, 10 = very religious |
| `close_social_ties` | Ordinal | 0 = none, 6 = 10 or more |
| `climate_worry` | Ordinal | 1 = not at all worried, 5 = extremely worried |

---

## Summary

- A tabular dataset organizes records as rows and attributes as columns.
- Dimensionality (number of columns) affects how much data algorithms need.
- Sparsity and resolution are structural properties that influence storage choices and analysis granularity.
- After loading a new dataset, it is common to check its size, content, missingness, and attribute types.

As always: Happy learning, happy life! 🫶

---

> **Navigation:** [<-- Data Types and Measurement Scales](02-data-types.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [EDA: Descriptive Statistics -->](04-eda-descriptive-stats.md)
