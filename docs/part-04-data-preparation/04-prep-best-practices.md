> **Navigation:** [<-- Scaling and Imputation](03-scaling-imputation.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Part V: 1st Pass — Supervised Learning -->](../part-05-supervised-learning/00-index.md)

---

# Data Preparation Best Practices

**Motivation**: The previous nuggets covered specific preparation steps. In practice you face a raw dataset and need to decide what to do in which order. Some of those decisions depend on the problem you are trying to solve and the model you intend to use. 

> Here you get a checklist for data preparation. This phase of [🖝 CRISP-DM](../part-01-the-big-picture/04-crisp-dm.md) sits between EDA and modeling. The checklist is meant as a standalone reference that gives phase-by-phase checklists to guide you through the major preparation decisions: setup, structural cleaning, feature engineering, the train/test split, statistic-estimating transforms (outlier capping → imputation → scaling). We also discuss reproducibility principles: keep raw data read-only, prevent target leakage, fix random seeds, and document every structural decision.

## Table of Contents

- [Data Preparation Checklist](#data-preparation-checklist)
- [Cross-Cutting Principles](#cross-cutting-principles)
- [Summary](#summary)

## Data Preparation Checklist

This checklist covers the major decision points you'll encounter when preparing a dataset for modeling. Use it as a quick reference when you start working on a new dataset. The main focus is still tabular data, but many principles apply in broad generality.

Steps marked **★** estimate statistics from data. They must be fitted on the training set only, then applied identically to every split. Fitting any of them on the full dataset would leak test-set statistics and likely produce too optimistic evaluation results. The formal explanation is in [🖝 Train/Test Split](../part-05-supervised-learning/02-train-test-split.md), with a deeper treatement in [🖝 Overfitting and Generalization](../part-06-reflection/01-overfitting-and-generalization.md).

---

### Phase 1: Before touching data

- **Protect your raw data.** Place input files in a read-only location. Generally, all transformations should read from raw and write to a derived location.
- **Fix all random seeds.** Set `random_state` to a fixed integer for every operation that uses randomness. Do this before executing any code that splits or shuffles data.

See also the cross-cutting principles below.

---

### Phase 2: Initial inspection and structural cleaning (full dataset, no statistics required)

These operations do use statistics from data for transformation, so they can safely be applied to the full dataset before the train/test split.

- **Consult the data dictionary/documentation.** Documenting a data set is a responsibility of those who create it. For those working with data, reading documentation is best practice. It should inform about column types, how data was recorded and encoded, and potential use of sentinel values.
- **Remove or reconcile duplicate records.** For survey data, exact duplicates can usually be dropped. Near-duplicates require judgment: do they represent different events or the same event recorded twice? Whether this step applies depends on the domain of the data.
- **Resolve wrong data types.** Coerce columns to their correct representation (`int`, `float`, `str`). Correct or remove erroneous data that prevents coercion.
- **Recode sentinel values to missing.** Replace values that encode missingness or special responses (e.g., `99` → `NaN`) before treating a column as numeric.
- **Correct or remove implausible entries.** An `age` of 200 or a score outside the declared scale range is a data-entry error. Recover the true value if possible; otherwise remove the row. Document removals.

*See also: [🖝 Structural Cleaning and Encoding](../part-04-data-preparation/02-cleaning-encoding.md) and [🖝 EDA: Data Quality](../part-03-data-understanding/05-eda-data-quality.md).*

---

### Phase 3: Feature engineering (informed by EDA and the prediction target)

Feature construction (see [🖝 Feature Engineering](../part-04-data-preparation/01-feature-engineering.md)) is driven by what EDA revealed and by what you want to predict. The constructions below can be applied to the full dataset, but any construction that estimates statistics (e.g., group means) needs to happen after in Phase 5.

- **Recode and binarize where EDA motivates it.** Skewed distributions, meaningful thresholds, and scale-direction inconsistencies are all triggers. 
- **Build composite indexes for multi-item constructs.** If several columns measure the same underlying concept, average them into a single index. Verify that all source columns point in the same direction and use the same unit before averaging.
- **Group high-cardinality categorical columns before encoding.** Consider collapsing infrequent categories into an "other" bucket to avoid noise.
- **Engineer derived attributes when domain knowledge or EDA calls for it.** Ratios, products, and differences can produce features more informative than either source column alone. Even single column transformations (like switching to a log scale) can sometimes be useful. Before using any derived feature, ask: *would this value be known before the outcome is observed?* If not, it is target leakage — drop it. See the cross-cutting principle below.
- **Encode categorical attributes by attribute type.** Binary nominal attributes get a single 0/1 column. Multi-value nominal attributes get one-hot encoding: use $k - 1$ columns to avoid perfect collinearity. Ordinal attributes with a natural rank get ordered integers. Avoid ordinal encoding for nominal attributes: it implies an ordering that does not exist. See [🖝 Structural Cleaning and Encoding](../part-04-data-preparation/02-cleaning-encoding.md).
- **Respect measurement scales.** Arithmetic on nominal attributes is meaningless. Averaging ordinal codes treats intervals as equal. Check the measurement scale of source columns before any derived operation. See [🖝 Data Types and Measurement Scales](../part-03-data-understanding/02-data-types.md).

---

### Phase 4: Splitting the data

- **Split before any statistic-estimating step.** The train/test split must happen before any operation that computes statistics from data (means, medians, min/max, frequencies). Your test set must not influence any preprocessing decision. See [🖝 Train/Test Split](../part-05-supervised-learning/02-train-test-split.md).

---

### Phase 5: Statistic-estimating steps (fit on training data only, apply to all splits)

Apply the following three steps in sequence. Each step's output is the next step's input.

- **★ Cap outliers if the model is sensitive to them.** Compute cap thresholds (e.g., 1st and 99th percentile) on the training set and apply to all splits. Capping must come before scaling: a single extreme value can otherwise compress all other values into a narrow band. Skip this step for, e.g., tree-based models that are not sensitive to extreme values. See [🖝 Scaling and Imputation](../part-04-data-preparation/03-scaling-imputation.md).
- **★ Impute missing values, or delete incomplete rows.** Choose between listwise deletion (remove any row with a missing value) and imputation (substitute an estimate from the training set). Match the strategy to the missingness mechanism you identified: Typically, choose mean or median for data missing completely at random (MCAR), and choose model-based imputation for data missing at random (MAR). Consider adding a binary indicator column that flags which rows were imputed. See [🖝 Scaling and Imputation](../part-04-data-preparation/03-scaling-imputation.md) and [🖝 EDA: Data Quality](../part-03-data-understanding/05-eda-data-quality.md).
- **★ Scale numeric features.** Distance-based models (k-NN), models like [🖝 Regularized Regression](../part-05-supervised-learning/05-regularized-regression.md), and neural networks are sensitive to feature scale; tree-based models are not. Z-score standardization is the safe default. Min-max scaling is appropriate only when bounded output is needed and outliers have already been handled. See [🖝 Scaling and Imputation](../part-04-data-preparation/03-scaling-imputation.md).

---

### Phase 6: Use pipelines to orchestrate steps

- **Wrap all statistic-estimating steps and the model in a pipeline.** A scikit-learn `Pipeline` enforces fit/transform separation automatically, eliminates manual ordering errors, and makes the trained model portable to production. See [🖝 Data Pipelines](../part-06-reflection/02-data-pipelines.md).

---

## Cross-Cutting Principles

These principles apply regardless of which specific steps your project requires. Violating any one of them can silently corrupt a project.

**Keep raw data read-only and traceable.**
Your original input files should never be modified in place. Store raw data separately from processed data, and write all transformations as reproducible code that reads from raw and writes to a derived location. If something goes wrong upstream, you can always re-run the pipeline from scratch. If you have overwritten the raw data, you cannot. For projects where multiple derived datasets exist — different cleaning versions, different feature sets — use clearly named folders or a lightweight versioning tool so that a model artifact can always be traced back to the exact data it was trained on.

**Prevent target leakage.**
[🖝 Supervised Learning](../part-05-supervised-learning/01-supervised-learning.md) uses target variables, and a feature "leaks the target" when it encodes information that would not be available at prediction time. Examples: including a post-event indicator as a predictor, or constructing a ratio that implicitly incorporates the outcome. Unlike train/test leakage, target leakage produces no error or warning. The model trains and evaluates without complaint, and performance numbers look excellent right up to deployment, where the leaking feature simply does not exist. Before constructing any derived feature, ask: *would this value be known before the outcome is observed?* If not, drop it. See [🖝 Feature Engineering](../part-04-data-preparation/01-feature-engineering.md) for the feature construction decisions where this risk is highest, and [🖝 Overfitting and Generalization](../part-06-reflection/01-overfitting-and-generalization.md) for the related form of leakage introduced by fitting transformers on the full dataset.

**Fix random seeds.**
Any operation that involves randomness — the train/test split, shuffle steps inside cross-validation, and stochastic optimization — must be seeded with an explicit integer. Use `random_state=42` (or any fixed value; the specific number does not matter, consistency does). Without a fixed seed, results change on every run, making bugs nearly impossible to reproduce and progress nearly impossible to measure.

**Document every structural decision.**
When you drop rows, recode a variable, choose a particular imputation strategy, or decide to bin a continuous attribute, write down why in a comment or a notebook cell. The choices that seem obvious today will be opaque in six months, and they will be opaque immediately to a colleague picking up the project. A one-sentence justification is enough: "Rows with `age > 100` dropped as likely data entry errors (n=3)."

> **Note:** These principles are not data-science-specific. They are basic reproducibility hygiene. They matter in every quantitative field and in every production system. Getting them right early costs almost nothing; recovering from ignoring them can cost days.

---

## Summary

- Preparation steps fall into two categories: those that require no statistics (structural cleaning, encoding, most feature construction) and those that estimate statistics from data (outlier capping, imputation, scaling). The first group can be applied to the full dataset; the second must be fitted on the training set only, then applied identically to all splits.
- The ordering within statistic-estimating steps matters: cap outliers first, then impute missing values, then scale. Each step's output is the next step's input.
- Choose encoding from the attribute type: binary for two-category nominal, one-hot ($k - 1$ columns) for multi-category nominal, ordered integers for ordinal. Group high-cardinality columns before encoding.
- Scale only when the model requires it. Tree-based models are not sensitive to feature scale; distance-based and regularized models are.
- Keep raw data read-only; fix random seeds; document every structural decision; check every derived feature for target leakage before using it.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Scaling and Imputation](03-scaling-imputation.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Part V: 1st Pass — Supervised Learning -->](../part-05-supervised-learning/00-index.md)

Script v1.1 (2026-05-18) · FGN
