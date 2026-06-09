> **Navigation:** [<-- Structural Cleaning and Encoding](02-cleaning-encoding.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Data Splits -->](04-data-splits.md)

---

# Scaling and Imputation

**Requires**: [Structural Cleaning and Encoding](02-cleaning-encoding.md) · [EDA: Descriptive Statistics](../part-03-data-understanding/04-eda-descriptive-stats.md)

**Motivation**: After structural cleaning and encoding, three data-preparation steps remain: handling missing values, managing extreme values, and bringing numeric features onto a comparable scale. We group these here because they rely on statistics from data like a mean or a maximum. As we'll see later in [🖝 Data Splits](../part-04-data-preparation/04-data-splits.md), those statistics must be computed on training data only.

> In this nugget, you'll learn how to decide when to cap versus keep extreme values, how to choose an imputation strategy for missing values, and how to apply min-max or z-score scaling.

## Table of Contents

- [Outlier Management](#outlier-management)
- [Imputation](#imputation)
- [Normalization and Scaling](#normalization-and-scaling)
- [Summary](#summary)

## Outlier Management

After [🖝 Structural Cleaning and Encoding](../part-04-data-preparation/02-cleaning-encoding.md), some numeric columns may still contain legitimate extreme values. How you handle them affects scaling and model fitting downstream.

There are two main strategies:

- **Keep as-is.** If the value is plausibly genuine and the model is not sensitive to extreme inputs, leaving it unchanged is often the right call. For example, this is the case for tree-based models like  [🖝 Decision Trees](../part-05-supervised-learning/09-decision-trees.md) that we cover later.

- **Cap (winsorize).** Replace values beyond a threshold with the threshold value itself. For example, capping `age` at the 99th percentile of the training set. This retains the row while limiting the outlier's influence on scaling and model fitting.

> **Warning:** The cap thresholds for winsorizing must be computed on the training set only and applied to all splits. We formally discuss why in the next nugget [🖝 Data Splits](../part-04-data-preparation/04-data-splits.md).

> **Tip:** Outlier capping should be applied before the scaling operations that we'll discuss in the next section. This is to prevent that extreme values "compress" ranges. 

---

## Imputation

After structural cleaning, some columns still contain missing values. You have two main options: deleting affected rows (listwise deletion) and "imputing" missing values.

**Listwise deletion** removes every row that contains at least one missing value. The remaining rows are genuinely complete, but you lose data. For small datasets, this is a serious cost.

**Imputation** fills in missing values with an estimated substitute. Common strategies:

- **Mean imputation**: replace each missing value with the column mean. Suitable for symmetric distributions without strong outliers.
- **Median imputation**: replace with the column median. The safer default for skewed distributions, ordinal data, or columns with outliers.
- **Mode imputation**: replace with the most frequent value. The natural choice for categorical attributes.
- **Model-based imputation**: train a small model to predict the missing value from the other columns. More complex and introduces assumptions. Not recommend at start.

Which strategy you choose follows from the missingness mechanism you identified in [🖝 EDA: Data Quality](../part-03-data-understanding/05-eda-data-quality.md). Data missing completely at random tolerates mean or median imputation. Data missing not at random requires greater care because then the fact itself that a value is missing carries information.

> **Tip:** When you impute, consider adding a binary indicator column recording which rows had missing values. Some models benefit from knowing that a value was substituted rather than observed.

> **Warning (again):** Imputation statistics (mean, median, mode) must be computed on the **training set only** and then applied to both training and held-out data, see [🖝 Data Splits](../part-04-data-preparation/04-data-splits.md).

---

## Normalization and Scaling

Many models are sensitive to the absolute numeric range of their inputs. A distance-based model such as k-nearest neighbors (TODO: nugget link) computes distances between observations.
For example in the ESS dataset, we have

- column `age` ranges 16 to 91,
- column `happiness` ranges from 0 to 10,
- column `health` ranges from 1 to 5.

Here, `age` has values an order of magnitude larger than the other two. It will dominate calculations purely because of its scale, not because it is more informative.

Scaling is the solution. There are two scaling methods that cover most practical needs.

### Z-score standardization

Z-score standarization, also called zero-mean normalization, scales features to have new mean=0 and std=1:

| Feature | Raw mean | Raw std | Z mean | Z std |
|---|---|---|---|---|
| `age` | 51.3 | 18.9 | 0 | 1 |
| `happiness` | 7.8 | 1.7 | 0 | 1 |
| `health` | 3.7 | 0.9 | 0 | 1 |

To do so, Z-score standarization centers the data at zero by subtracting the mean, and it scales by the standard deviation:

$$x' = \frac{x - \bar{x}}{\sigma_x}$$

where $\bar{x}$ is the column mean for feature $x$ and $\sigma_x$ is the standard deviation. After standardization, the column **always** has mean $0$ and standard deviation $1$.

### Min-max scaling

Min-max scaling, also called min-max normalization, scales features to have new minimum=0 and maximum=1:

| Feature | Raw min | Raw max | Scaled min | Scaled max |
|---|---|---|---|---|
| `age` | 16 | 91 | 0 | 1 |
| `happiness` | 0 | 10 | 0 | 1 |
| `health` | 1 | 5 | 0 | 1 |

Min-max scaling is a linear transformation.
The most common special case maps values to the interval $[0, 1]$ using the formula
$$x' = \frac{x - \min_x}{\max_x - \min_x}.$$
The difference in the enumerator offsets the whole feature to have min=0, then we normalize by the range.

More generally, we can map a feature $x$ to a target range $[a,b]$ using the minimum and maximum of the original feature column $x$:

$$x' = \frac{x - \min_x}{\max_x - \min_x}(b - a) + a,$$
The first term is still the same and scales to $[0,1]$, then we apply another linear transformation to obtain the new range $[a, b]$.

Min-max scaling preserves the shape of the original distribution. However:

> Min-max scaling has a high sensitivity to outliers: a single extreme value compresses all other values into a narrow band.

A further limitation is the **out-of-bounds problem**: if future data fall outside the range $[\min_x, \max_x]$ observed during training, the scaled values will fall outside the target range.

Because of these limitations, z-score standardization is the more robust standard choice for most regression and neural network models.

> **Warning (again, again):** The mean, standard deviation, minimum, and maximum used for scaling are statistics computed from data. They must be determined on the training set only and then applied to all splits: same as for outlier capping and imputation before.

> **Tip:** You'll find a checklist for the overall preparation sequence in [🖝 Data Preparation Checklist](../part-04-data-preparation/05-prep-checklist.md) with a clear before/after for the [🖝 Data Splits](../part-04-data-preparation/04-data-splits.md).

---

## Summary

- Genuine extreme values can be capped to limit their influence on scaling and model fitting, or kept as-is when the model is not sensitive to extremes.
- Imputation fills missing values using statistics: mean for symmetric distributions, median for skewed or ordinal data, mode for categoricals. Alternatively, listwise deletion removes incomplete rows at the cost of data.
- Scaling brings numeric features to a comparable range. Z-score standardization centers and scales by standard deviation and is a safe default. Min-max scaling maps values to a fixed interval but is sensitive to outliers. 
- All three families estimate statistics from data and must be fitted on the training set only, then applied identically to all splits, see [🖝 Data Splits](../part-04-data-preparation/04-data-splits.md).

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Structural Cleaning and Encoding](02-cleaning-encoding.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Data Splits -->](04-data-splits.md)

Script v1.3 (2026-06-09) · FGN
