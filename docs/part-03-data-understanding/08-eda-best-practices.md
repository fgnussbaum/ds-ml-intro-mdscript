> **Navigation:** [<-- EDA: Correlations](07-eda-correlations.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Part IV: Data Preparation -->](../part-04-data-preparation/00-index.md)

---

# Data Understanding: Best Practices

**Motivation**: You have now built a quite complete EDA toolkit: loading data, checking structure, computing statistics, visualizing distributions, assessing quality, and examining correlations. Let's wrap everything up.

> Here, you'll find an EDA checklist consolidating the best practices from this part, a visualization reference table mapping analytical questions to the right plot type, and a set of pitfalls that cause charts to mislead. This gives you a practical workflow guide and steps to train your "critical eye" for data work.

## Table of Contents

- [EDA Checklist](#eda-checklist)
- [Visualizations Reference](#visualizations-reference)
- [Visualization Pitfalls](#visualization-pitfalls)
- [Summary](#summary)

## EDA Checklist

This nugget collects the key practices from Nuggets 3.1–3.7 into a single quick reference. Use it as a checklist when you begin EDA on any new dataset.

**Before you start**

- **Profile every column before writing transformation code.** Check name, type, range, and missing-value count for every variable. `df.info()` and `df.describe()` give you this in two lines. The mechanics are covered in [🖝 Datasets](../part-03-data-understanding/03-datasets.md) and [🖝 EDA: Descriptive Statistics](../part-03-data-understanding/04-eda-descriptive-stats.md).

**Distributions and quality**

- **Look at distributions, not just summary statistics.** Aggregates like mean or standard deviation collapse shape information. Use histograms and box plots to make skew, multimodality, and floor or ceiling effects visible. ([🖝 EDA: Distributions](../part-03-data-understanding/06-eda-distributions.md))
- **Treat unexpected distributions as signals.** A heavily right-skewed variable or a suspicious spike at one value often reflects how the data was gathered, not just the underlying phenomenon. Question the data-generating process before touching the data.
- **Identify outliers visually before deciding what to do with them.** Determine whether an outlier is a measurement artifact or a legitimate observation. Removal without investigation can delete real signal. ([🖝 EDA: Distributions](../part-03-data-understanding/06-eda-distributions.md))

**Missing values**

- **Examine missing-value patterns before handling them.** Quantity matters, but pattern matters more. Random missingness (MCAR) and systematic missingness (MAR, MNAR) call for different responses. Handling strategies are covered in Part IV. ([🖝 EDA: Data Quality](../part-03-data-understanding/05-eda-data-quality.md))

**Relationships**

- **Use a correlation matrix as a starting point, not a conclusion.** Pearson correlation quantifies linear association. It does not establish causation, and it misses non-linear relationships entirely. Follow up with scatter plots where the coefficient warrants closer examination. ([🖝 EDA: Correlations](../part-03-data-understanding/07-eda-correlations.md))

---

## Visualizations Reference

The table below summarizes the full EDA visualization toolkit built across Nuggets 3.6 and 3.7.

| Question | Plot |
|---|---|
| What values does this column contain? | Histogram or KDE |
| Where is the center and how spread is it? | Boxplot |
| How does this variable differ across groups? | Faceted histograms or side-by-side boxplots |
| Do these two variables move together linearly? | Scatter plot + Pearson $r$ |
| Is there a monotonic or non-linear relationship? | Scatter plot + Spearman $r$ |
| What is the pairwise structure of the whole dataset? | Pair plot + correlation heatmap |

---

## Visualization Pitfalls

Charts can make patterns appear that are not really there. Three habits cause most misleading visualizations. Learn to recognize them when you read others' results and avoid them in your own.

**Truncated axes.** Starting the y-axis at a value above zero makes small differences look large. Always check whether an axis starts at zero or has been cut to amplify a trend. If you need to truncate to show fine-grained variation, label the axis clearly and note the truncation.

**Cherry-picked ranges.** Zooming in on a time window or a data subset can make a flat trend look steep, or a volatile series look smooth. The full range is the honest baseline. A zoomed-in view is only legitimate when the full view is also presented.

**Dual axes.** Plotting two variables on the same chart with independent y-axes allows almost any two series to appear correlated, simply by choosing scales that make them line up visually. Treat dual-axis charts with suspicion unless the scales are fixed by definition. In most cases, two aligned single-axis charts are clearer and more honest.

> **Maintain integrity:** Before you report a result, ask: "Does this chart accurately represent the data, or does it exaggerate a trend?" Misleading visualizations regularly appear in public discourse, sometimes without deliberate intent. Understanding the mechanics of deception is what allows you to avoid it.

---

## Summary

- Profile every column, examine distributions and outlier patterns, inspect missing-value patterns, and check pairwise correlations before making any decisions about the data.
- Treat unexpected distributions as signals about the data-generating process, not just features to correct away.
- Three visualization pitfalls make weak patterns look real: truncated axes, cherry-picked ranges, and dual axes. Ask whether a chart is honest before reporting it.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- EDA: Correlations](07-eda-correlations.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Part IV: Data Preparation -->](../part-04-data-preparation/00-index.md)

Script v1.4.1 (2026-06-23) · FGN
