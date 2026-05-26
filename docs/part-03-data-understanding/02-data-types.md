> **Navigation:** [<-- Why Data Work Dominates](01-why-data-work.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Datasets -->](03-datasets.md)

---

# Data Types and Measurement Scales

**Requires**: [Why Data Work Dominates](01-why-data-work.md)

**Motivation**: Before you can summarize, visualize, or model any column in your dataset, you need to know what kind of value it holds. The same column might look like a number and yet be meaningless to average. This nugget asks: what distinguishes a valid arithmetic operation on data from a meaningless one?

> You will learn to classify any attribute by its measurement scale (nominal, ordinal, interval, ratio) and by whether it is discrete, continuous, or binary — knowledge that determines which statistics and encodings are valid for each column.

## Table of Contents

- [Measurement Scales](#measurement-scales)
- [Discrete, Continuous, and Binary Attributes](#discrete-continuous-and-binary-attributes)
- [Summary](#summary)

## Measurement Scales

Every column in your dataset represents an **attribute**: a property of the objects you are studying. Attributes come in four **measurement scales**: nominal, ordinal, interval, ratio. The scale describes what operations and comparisons are meaningful for that attribute.

The four scales form a strict hierarchy: each level inherits everything below it and adds exactly one new capability.

| Scale | What's added | Permissible Operations | Valid Statistics | Example Attributes |
|-------|-------------|-----------|---------------------------|-------------------|
| Nominal | Distinctness | =, ≠ | Mode, frequency, counts | Country, sensor type, loan status |
| Ordinal | Order | =, ≠, <, > | Median, percentiles, rank correlation | Survey ratings, severity levels, grades |
| Interval | Equal differences | +, − (+comparisons) | Mean, standard deviation, Pearson correlation | Temperature (°C/°F), calendar year |
| Ratio | True zero | +, −, ×, ÷ (+comparisons) | All statistics, geometric mean, % change | Temperature (K), length, mass, voltage |

**Nominal scale** supports only distinctness: you can tell whether two values are the same or different.
Even if we assign numbers to nominal categories (e.g., 1 = "type A", 2 = "type B"), they are just labels. Assigned numbers do not carry mathematical meaning.

**Ordinal scale** adds order: you can rank values. However, the gaps between ranks are not guaranteed to be equal.
Survey scales ("rate your agreement 1 to 5") are ordinal. The number 4 is higher than 3, but the _psychological_ difference between them may not equal the difference between 2 and 3.

**Interval scale** adds the ability to measure differences.
You can say one value is 5 units more than another, and that gap is meaningful and consistent. However, the zero point is arbitrary: it is just a reference point, not "nothing." Multiplying interval values produces nonsense: the year 1000 CE is not "twice as old" as 500 CE, because the year zero is a human choice, not true zero.

**Ratio scale** adds a true zero, making multiplication and division meaningful. Most physical measurement quantities are ratio-scale: length, mass, voltage, time duration, angular displacement.

> **Common errors**: Applying an operation the scale does not support produces numbers that look real but mean nothing. The most common errors: computing the mean of nominal codes (the codes are just labels), treating ordinal gaps as equal intervals (e.g., averaging a 1–5 survey scale — technically wrong, but widely done and often acceptable for exploratory work), and computing ratios on interval data (e.g., claiming 20°C is "twice as warm" as 10°C).

The scale also controls which encoding choices make sense when preparing data for a model: nominal attributes need one-hot or dummy encoding; ordinal attributes can sometimes be passed as ordered integers; interval and ratio attributes can be fed directly to numeric models, typically after scaling. You will apply these rules in [🖝 Structural Cleaning and Encoding](../part-04-data-preparation/02-cleaning-encoding.md).

[Source: Tan et al. (2020), *Introduction to Data Mining*, Pearson]

---

## Discrete, Continuous, and Binary Attributes

The measurement scale describes *what operations the data supports*. A complementary question is *how many values the attribute can take*. This distinction matters for storage, algorithm choices, and how you interpret statistics.

There are essentially three answers to the "how many values"-question:

| Domain | Typical storage | Examples |
|--------|----------------|---------|
| Binary | bool / int | Loan approved, course attended, gender indicator |
| Discrete | int | Course registration count, social tie count, defect count |
| Continuous | float | Temperature, sensor output, age computed from a birth year |

A **discrete attribute** has a finite or countably infinite set of possible values. Discrete attributes can be categorical or numeric: the number of close social ties in the ESS (0, 1, 2, 3...) is discrete numeric, while a country code is discrete categorical. Values are typically stored as integers.

A **continuous attribute** takes real-number values within a range. Temperature, height, weight, and sensor readings are continuous. In practice, measurements are recorded with limited precision, but the underlying quantity is treated as continuous. Continuous attributes are stored as floats.

A **binary attribute** is a special case of discrete with exactly two values: true/false, on/off, or 0 and 1. The `gender` column in the ESS (0 = Female, 1 = Male) is binary. Binary attributes are usually stored as integers 0 and 1, or as Boolean values.

> **Note:** Some attributes sit in a gray area. The ESS happiness rating (0–10) is technically discrete with 11 values, but researchers often treat it as quasi-continuous to compute means and standard deviations. Knowing you are making this simplification, and checking whether it changes your conclusions, is good analytical practice.

[Source: Tan et al. (2020), *Introduction to Data Mining*, Pearson]

---

## Summary

- Every column in a dataset is an attribute. Its measurement scale — nominal, ordinal, interval, or ratio — determines what operations and statistics are valid.
- The four scales form a hierarchy: each level adds one capability, from distinctness only (nominal) to full arithmetic (ratio).
- Common errors: averaging nominal codes, treating ordinal gaps as equal, or computing ratios on interval data.
- Encoding choices for models follow from the scale: nominal needs one-hot encoding, ordinal can sometimes use ordered integers, numeric attributes need scaling.
- Separately, attributes are discrete, continuous, or binary — describing how many values they can take, not what operations apply.
- Identifying attribute types is one of the first steps in any EDA workflow.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Why Data Work Dominates](01-why-data-work.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Datasets -->](03-datasets.md)

Script v1.2 (2026-05-26) · FGN
