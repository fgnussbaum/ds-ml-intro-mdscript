> **Navigation:** [<-- Feature Engineering](01-feature-engineering.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Scaling and Imputation -->](03-scaling-imputation.md)

---

# Structural Cleaning and Encoding

**Requires**: [Data Types and Measurement Scales](../part-03-data-understanding/02-data-types.md) · [EDA: Data Quality](../part-03-data-understanding/05-eda-data-quality.md)

**Motivation**: Before any model can work with your data, two additional types of preparation are often needed: structural problems must be fixed, and categorical attributes must be converted to numeric form.

> In this nugget, you'll learn to fix the structural problems EDA revealed: duplicates, type errors, sentinel values, and implausible entries. You'll also learn to convert categorical attributes to numeric form using the encoding that matches each attribute's measurement scale.

## Table of Contents

- [Structural Cleaning](#structural-cleaning)
- [Encoding Categorical Attributes](#encoding-categorical-attributes)
- [Summary](#summary)

## Structural Cleaning

EDA tells you what problems exist in your data (see [🖝 EDA: Data Quality](../part-03-data-understanding/05-eda-data-quality.md)). Cleaning is how you fix them so that a model can work with the result.
Let's review a couple of structural problems along with potential fixes.

**Duplicate records** arise when the same observation appears more than once, often due to errors in data collection or merging.
Exact duplicates can be detected and in many cases, removing them is the right fix (if they should genuinely be just one record). Near-duplicates require judgment about whether they represent different events or the same event recorded twice.

**Wrong data types** occur when a column is stored as the wrong type, for example a numeric column stored as a string because one cell contained an erroneous letter.

> Use **type coercions** like `df["happiness"].astype(int)` to convert columns to the correct type.

Erroneous cells, like the presumed string cell, also need to be fixed.

**Sentinel values** are values that look valid but encode something else, such as "not applicable" or "refused to answer". The ESS dataset contains a concrete example: the `climate_worry` column uses a 1–5 scale, but a response coded 6 represents "not applicable". Without consulting the codebook, 6 looks like a scale value above the maximum.

> Always check the data dictionary (aka documentation) before treating a column as numeric, and recode sentinel values to missing before passing the column to any model.

**Data entry and measurement errors** produce implausible values: an `age` of 200, a happiness score outside the declared scale range, a negative income. Correct the value if the true one is recoverable; otherwise remove you'll usually need to remove the row.

> **Document removals (What + Why)**: This can just be one line.

---

## Encoding Categorical Attributes

Most models expect numeric inputs: Categorical attributes must be converted before training. The right encoding depends on the attribute type, introduced in [🖝 Data Types and Measurement Scales](../part-03-data-understanding/02-data-types.md).

**Binary encoding** handles nominal attributes with exactly two values by creating a single 0/1 column. In the ESS dataset, `gender` is encoded as 0 (female) and 1 (male).

**One-hot encoding** handles nominal attributes with more than two values by creating one binary column per category. If a `country` column has five values, you get five columns: `country_AT`, `country_BE`, `country_CH`, `country_DE`, `country_FR`.

> **Leaving out one column**: If you have $k$ categories, you only need $k - 1$ indicator columns to encode it because the $k$-th column is then fully determined by the others: $x_k=1-x_1-\ldots​-x_{k-1}$. The $k$ columns are perfectly _colinear_.

Including all $k$ indicators is redundant but harmless for many models. For models with learnable parameters, perfect collinearity can prevent a unique solution and complicate interpretation of those parameters, as you will see later in [🖝 Linear Regression](../part-05-supervised-learning/02-linear-regression.md). Dropping one column resolves this: the omitted category becomes the reference level, and every remaining coefficient is interpreted as a difference relative to it.

**Ordinal encoding** handles ordinal attributes by assigning consecutive integers that respect the rank order. An education level column (primary, secondary, tertiary) could be encoded as 1, 2, 3. This assumes equal spacing between levels. If the model is sensitive to that assumption, one-hot encoding is a safer alternative.

| Attribute type | Encoding | ESS example |
|---|---|---|
| Nominal, binary | Binary (0/1) | `gender` (female = 0, male = 1) |
| Nominal, many values | One-hot ($k - 1$ columns) | `country` |
| Ordinal | Ordered integers | `health` |
| Numeric | No encoding needed | `age` |

---

## Summary

- Structural cleaning addresses duplicates, type coercion, sentinel values, and rows with data entry errors.
- Always consult the data dictionary ("code book") before treating data.
- Encoding converts categorical attributes to numeric form: binary for two-category nominal, one-hot for multi-category nominal (dropping one column), and ordered integers for ordinal attributes.
- Neither cleaning nor encoding requires distributional estimates. Apply both to the full dataset before the Data Splits.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Feature Engineering](01-feature-engineering.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Scaling and Imputation -->](03-scaling-imputation.md)

Script v1.5 (2026-06-24) · FGN
