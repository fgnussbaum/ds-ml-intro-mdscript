> **Navigation:** [<-- Datasets](03-datasets.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [EDA: Data Quality -->](05-eda-data-quality.md)

---

# EDA: Descriptive Statistics

**Requires**: [Datasets](03-datasets.md)

**Motivation**: After first inspection of a dataset as in [🖝 Datasets](../part-03-data-understanding/03-datasets.md), the next question is: what are the typical values, and how much do they vary?

> In this nugget, you'll get to know summary statistics that answer those questions. We'll also consider Python pandas shortcuts that computes them all at once, like `df.describe()`. You'll learn about mean and median as measures of center, variance and standard deviation as measures of spread, and the five-number summary as a more robust alternative that the boxplot will later make visual.

## Table of Contents

- [Getting Oriented with df.describe()](#getting-oriented-with-dfdescribe)
- [Measures of Central Tendency](#measures-of-central-tendency)
- [Measures of Spread](#measures-of-spread)
- [Summary](#summary)

## Getting Oriented with df.describe()

In addition to the previously discussed `df.info()`, there is also `df.describe()` to produce a compact summary of every numeric column in your dataset. Reading it carefully is a habit that pays off every time.

Here is the output for the ESS Well-Being dataset (three columns shown for space):

```
           happiness   health  gender
count       2417.00  2417.00  2420.0
mean           7.76     3.68     0.5
std            1.68     0.90     0.5
min            0.00     1.00     0.0
25%            7.00     3.00     0.0
50%            8.00     4.00     1.0
75%            9.00     4.00     1.0
max           10.00     5.00     1.0
```

What each row tells you:

- **count**: the number of non-null values. `happiness` and `health` show 2,417 out of 2,420 records, meaning three respondents left these questions blank.
- **mean** and **std**: the arithmetic average and standard deviation. A mean of 7.76 for happiness suggests Germans tend toward the happy end of the scale (they do!). A std of 1.68 means most respondents fall roughly between 6 and 9.
- **min** and **max**: the range endpoints. Happiness spans the full 0–10 range, though the 25th percentile is already 7, which hints at left-skew (see [🖝 EDA: Distributions](../part-03-data-understanding/06-eda-distributions.md) nugget).
- **25%, 50%, 75%**: the quartiles. For happiness, Q1 = 7, median = 8, Q3 = 9. Half of all respondents rated themselves 8 or above.

All quantities are defined in detail below.

What `df.describe()` does *not* tell you:

- distribution shape
- the number of distinct values (use `df.unique()` on a column for this)
- whether missing values are random or systematic

We'll revisit these questions in [🖝 EDA: Distributions](../part-03-data-understanding/06-eda-distributions.md).
`df.describe()` also does not tell you whether the computed statistics actually make sense for the attribute and its measurement scale: For example, what's your impression of the `gender` column above? It is considered a numeric column due to its coding, though it conceptually is a categorical one.

> **Categorical columns:** By default `df.describe()` includes only numeric columns. Pass `include="all"` to also summarize categorical columns (which show count, unique, top, and freq instead of mean and std).

---

## Measures of Central Tendency

A measure of central tendency answers: what is a typical value for this attribute? Two measures dominate in practice.

### Arithmetic Mean

The **arithmetic mean** is the sum of all values divided by the count:

$$\bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i$$

Here, $x_i$ are the observations for the attribute, $N$ is the observation count.

The mean is sensitive to extreme values. A single very high or very low observation pulls the mean toward itself.

### Median

The **median** is the middle value when the data is sorted. For $N$ observations sorted in increasing order:

$$\tilde{x} = \begin{cases} x_{(m+1)}, & \text{if } N = 2m + 1 \\ \dfrac{x_{(m)} + x_{(m+1)}}{2}, & \text{if } N = 2m \end{cases}$$

The median is not affected by extreme values, which makes it the better choice whenever the distribution is skewed or when the attribute is ordinal. The 50% row in `df.describe()` is the median: for ESS happiness it is 8.0, above the mean of 7.76, confirming a mild left skew (a few unhappy respondents pull the mean down).

<!-- distributions knoweledge prerequisite-->
**When to use which** depends largely on the distribution at hand (see [🖝 EDA: Distributions](../part-03-data-understanding/06-eda-distributions.md)):

- Symmetric, unimodal distributions with no strong outliers: the mean is efficient and commonly reported
- Skewed distributions or heavy tails: prefer the median.
- Ordinal attributes (survey scales, ratings): the median is technically appropriate. Reporting a mean is common but assumes equal intervals between ranks.

---

## Measures of Spread

Knowing the center is not enough. Two distributions can share the same mean while looking entirely different. Measures of spread describe how much the data varies around the center.

### Variance and Standard Deviation

The **variance** quantifies average squared deviation from the mean. Two formulas exist depending on whether you have a sample or the full population:

$$s^2 = \frac{1}{N-1} \sum_{i=1}^{N} (x_i - \bar{x})^2 \qquad \text{(sample)}$$

$$\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \bar{x})^2 \qquad \text{(population)}$$

In data science you almost always work with samples, so $s^2$ with $N-1$ in the denominator is the default. The $N-1$ adjustment ([🔗 Bessel's correction](https://en.wikipedia.org/wiki/Bessel%27s_correction)) accounts for the fact that the sample mean is itself an estimate, which causes a naive formula to slightly underestimate the true spread.

The **standard deviation** is the square root of the variance: $s = \sqrt{s^2}$. It restores the original units. For ESS happiness, $s \approx 1.68$, meaning roughly two-thirds of respondents fall within $7.76 \pm 1.68$, that is, between about 6.1 and 9.4.

### Range

The **range** is the simplest spread measure: $\max - \min$. For happiness it is $10 - 0 = 10$. The range is easy to compute but very sensitive to a single extreme value.

### Five-Number Summary

The **five-number summary** provides a more robust picture:

$$\text{minimum}, \quad Q_1, \quad \text{median}, \quad Q_3, \quad \text{maximum}$$

The **interquartile range (IQR)** is the distance between the first and third quartiles:

$$\text{IQR} = Q_3 - Q_1$$

The IQR captures the spread of the central 50% of the data, ignoring extreme values at either end. For ESS happiness: $\text{IQR} = 9 - 7 = 2$, meaning the middle half of respondents gave ratings between 7 and 9. The `df.describe()` output already gives you Q1 (25%), median (50%), and Q3 (75%) directly.

*See also: [🖝 EDA: Distributions](../part-03-data-understanding/06-eda-distributions.md) covers the boxplot, which visualizes the five-number summary and uses the IQR to flag potential outliers.*

---

## Summary

- `df.describe()` gives you count, mean, std, min, quartiles, and max for each numeric column in one call.
- The mean is sensitive to extreme values; the median is not. For skewed distributions and ordinal attributes, prefer the median.
- Variance and standard deviation measure average deviation from the mean.
- The five-number summary (min, Q1, median, Q3, max) and the IQR describe spread without being distorted by extreme values.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Datasets](03-datasets.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [EDA: Data Quality -->](05-eda-data-quality.md)

Script v1.5 (2026-06-24) · FGN
