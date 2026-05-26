> **Navigation:** [Part Index](00-index.md) | [Main Index](../index.md) | [Structural Cleaning and Encoding -->](02-cleaning-encoding.md)

---

# Feature Engineering

**Requires**: [Data Types and Measurement Scales](../part-03-data-understanding/02-data-types.md) · `eda-correlation-visualizations`

**Motivation:** EDA usually leaves you with a "pot-pourri" of findings: a skewed distribution here, a cluster of correlated survey items there, a categorical column with dozens of rare values. Often it turns out that raw columns are not the best input for a model or analysis. How do you systematically convert your columns into better-structured columns that actually represent what you care about?

> In this nugget, you'll learn specific construction operations for new features: from collapsing thresholds into binary indicators and averaging item sets into composite indexes, to combining columns through ratios or products and grouping rare categories. You'll also see a set of structural transformations, such as binning and aggregation, that reshape data for modeling.

## Table of Contents

- [Feature Construction](#feature-construction)
- [General-Purpose Transformations](#general-purpose-transformations)
- [Summary](#summary)

## Feature Construction

Every EDA finding is a potential feature idea. In the following, we discuss several construction operations along with typical "trigger points". 

As you saw in [🖝 Data Types and Measurement Scales](../part-03-data-understanding/02-data-types.md), the permissable construction operations also depend on the measurement scales of source attributes: arithmetic on nominal data is meaningless, and ratios require a ratio scale.

---

### Binarization and Recoding

**Trigger:** A skewed distribution, a meaningful threshold, or a scale-direction inconsistency.

**Binarization** converts a continuous or ordinal attribute into a 0/1 indicator. In the ESS data, health is recorded on a 1–5 scale. Converting it to a binary health-good-or-not indicator could be reasonable for easier interpretation (however, also some detail is lost):

```python
# Binary health indicator: 1 = Good or Very Good (health >= 4 on the 1–5 scale)
df["health_good"] = (df["health"] >= 4).astype(int)
```

**Recoding** covers the broader case:
- collapsing a continuous attribute into fewer categories,
- reversing the direction of a scale.

*Note: For the ESS data, I did the latter for a few columns so that higher values _consistently_ mean "more" of the construct. The intention was to make understanding the data easier.*

---

### Composite Indexes/Indices

**Trigger:** Several items in the dataset measure the same underlying construct.

This is common for [Likert-scale](https://en.wikipedia.org/wiki/Likert_scale) survey questions, which yield ordinal variables. Surveys often use several questions to  measure the same concept more reliably. A **composite index** then helps to quantify this concept.
You usually obtain it by averaging. Before doing so, verify two things:
1. all source columns point in the same direction (e.g., higher means "more"), and
2. a unit increase must mean the same thing across columns.

If those conditions hold, a simple mean is a valid summary. In the ESS, the [Schwartz-style value](https://en.wikipedia.org/wiki/Theory_of_basic_human_values) columns all run from 1 ("Not like me at all") to 6 ("Very much like me"), so both conditions are satisfied. Here's some example code for building the corresponding average composite:

```python
SELF_TRANSCENDENCE_COLS = ["val_equality", "val_understand_others", "val_helping_others", "val_environment"]
df["val_transcendence"] = df[SELF_TRANSCENDENCE_COLS].mean(axis=1)
```

<!--See the demo code for a complete scale-compatibility check before averaging.-->

---

### Grouping High-Cardinality Columns

**Trigger:** A categorical column contains many rare values.

Rare categories produce sparse one-hot columns that add noise and inflate feature matrices. Collapsing infrequent country codes or job titles into an "other" bucket could reduce that noise.

> Apply grouping before the kind of encoding operation that we discuss in the next nugget [🖝 Structural Cleaning and Encoding](../part-04-data-preparation/02-cleaning-encoding.md).

---

### Derived Combinations

**Trigger:** Domain knowledge or an EDA finding suggests that combining two ore more columns yields something more informative than either alone.

Products, ratios, and differences are the most common operations, but any functional combination is conceivable as long as the result captures a new relationship.

- *Domain-driven:* `income` _per_ household member is more informative than raw income for predicting poverty risk. Correlation alone indeed cannot generate this idea: you need to know what the numbers represent.
- product columns like `income × education` may capture joint effects that neither column encodes alone.

These combinations are only meaningful for numeric attributes (at least interval scale).

> **Discussion:** You notice during EDA that a feature correlates strongly with a _target_ variable that you want to predict. You engineer a ratio that incorporates both that feature and the target variable. What would be the consequence of using this ratio as an input feature for a machine learning model that predicts the target variable?

<!-- example: predict tip given total_bill, engineer feature tip_rate=tip/total_bill -->

*See also [🖝 Data Preparation Best Practices](../part-04-data-preparation/04-prep-best-practices.md): the target leakage principle. A constructed feature is only valid if its value does not depend on the outcome/target variable.*
<!-- TODO overfitting, data leakage nugget link-->

---

## General-Purpose Transformations

Beyond EDA-driven construction, several transformations reshape data structurally without being motivated by a specific finding. They appear regularly in preprocessing pipelines and can be applied before the [🖝 Train/Test Split](../part-05-supervised-learning/02-train-test-split.md).

---

### Smoothing

**Trigger:** Sensor readings or time-series data with high-frequency noise.

Smoothing replaces each value with a local estimate, for example the mean of its neighboring values. The goal is to reduce noise rather than to extract a new construct.

---

### Aggregation

**Trigger:** Data needs to be summarized at a coarser granularity for modeling.

Summing up daily sales to weekly totals, or averaging individual-level survey responses to country-level means, are both forms of aggregation. Aggregation reduces data volume and can also reduce noise.

---

### Generalization of Specific Values

**Trigger:** Specific values are too granular for the model or for interpretation.

Mapping street-level addresses to city names, or grouping exact ages into age brackets, replaces specific values with higher-level concepts. The result is a coarser representation that is sometimes more interpretable and more generalizable.

Grouping high-cardinality columns that we discussed above can be seen as a special case of this with the goal of "collapsing" rare categories.

---

### Binning

**Trigger:** A model benefits from ordinal inputs, or you want to reduce sensitivity to outliers.

**Binning** (also called discretization) converts a continuous attribute into an ordinal one by grouping values into bins. This is related to the construction of histograms in [🖝 EDA: Distributions](../part-03-data-understanding/06-eda-distributions.md).

Two common strategies are:

- **Equal-width binning:** divide the value range (min to max) into $k$ intervals of equal width.
- **Equal-frequency binning:** divide the data so that each bin contains the same number of observations.

Equal-width bins are easier to interpret. Equal-frequency bins produce more balanced categories when the distribution is skewed.

---

## Summary

- Feature engineering sits at the boundary between data _understanding_ and _preparation_: EDA reveals patterns, and feature construction acts on them. The two phases are intertwined, not cleanly sequential.
- Each EDA finding type suggests a specific construction: correlations (or domain knowledge) suggest derived combinations, thresholds suggest binarization, item sets suggest composite indexes, and rare categories suggest grouping.
- The measurement scale of the source columns constrains which operations are valid. Check scale direction and unit compatibility before averaging or multiplying.
- Smoothing, aggregation, generalization, and binning are structural transformations often applied for pipeline or modeling reasons rather than in response to a specific EDA finding.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [Part Index](00-index.md) | [Main Index](../index.md) | [Structural Cleaning and Encoding -->](02-cleaning-encoding.md)

Script v1.1 (2026-05-18) · FGN
