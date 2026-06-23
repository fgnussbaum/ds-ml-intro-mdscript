> **Navigation:** [<-- Regression: Interpretation and Assumptions](03-regression-depth.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Support Vector Machines -->](05-support-vector-machines.md)

---

# Statistical Significance

**Requires**: [Linear Regression](../part-05-supervised-learning/02-linear-regression.md)

**Motivation**: Your regression model says that a one-point increase in self-rated health corresponds to a 0.4-point increase in happiness. But is that relationship real, or could it have appeared by chance in this particular sample of a few thousand respondents? A model metric like $R^2$ tells you how well the model fits the data. A significance test tells you whether the fitted pattern is likely to persist in new data, or whether it is an artifact of sampling noise.

> In this optional nugget you will learn what a p-value means, how Type I and Type II errors arise in a regression context, and when statistical significance translates — and when it does not translate — to practical usefulness.

> **Context:** This nugget covers **regression** — specifically, how to assess whether the coefficients your model learned are trustworthy. The same hypothesis-testing framework applies to classification settings, but the connection to regression coefficients is the most direct.

## Table of Contents

- [p-Values and the Null Hypothesis](#p-values-and-the-null-hypothesis)
- [Type I and Type II Errors in a Regression Context](#type-i-and-type-ii-errors-in-a-regression-context)
- [When Is a Regression Result Meaningful?](#when-is-a-regression-result-meaningful)
- [Summary](#summary)

## p-Values and the Null Hypothesis

For any regression coefficient $w_j$, you can ask: "What if the true effect were zero? How likely is it that I would observe a coefficient this large just by chance in a random sample?"

This is the **null hypothesis** $H_0$: $w_j = 0$ — the feature has no relationship with the target in the population. The **p-value** is the probability of observing a coefficient at least as extreme as $w_j$ if $H_0$ were true.

A small p-value means: it would be very unlikely to see this result if there were truly no effect. By convention, a threshold $\alpha = 0.05$ is used. If the p-value is below 0.05, you **reject** $H_0$ and call the effect statistically significant. If it is above 0.05, you **fail to reject** $H_0$ — you cannot conclude there is an effect, but you also have not proved there is none.

Most regression frameworks report p-values for each coefficient automatically. Python's `statsmodels` includes them in the regression summary table. Scikit-learn's `LinearRegression` does not compute them by default — use `statsmodels` when you need significance tests.

> **Note:** "Reject $H_0$ at $\alpha = 0.05$" is a decision rule, not a probability that the effect is real. It means: "If there were no effect, I would see a result this extreme in at most 5% of random samples." It says nothing about whether the effect is large or practically important.

---

## Type I and Type II Errors in a Regression Context

The hypothesis testing framework exposes two ways to be wrong:

| Decision | $H_0$ true (no effect exists) | $H_0$ false (effect exists) |
|---|---|---|
| Reject $H_0$ | **Type I error** | Correct |
| Fail to reject $H_0$ | Correct | **Type II error** |

**Type I error** (rate $\alpha$): you conclude an effect exists when it does not. Setting $\alpha = 0.05$ bounds this error rate at 5% — but only if you run a single test. Running many tests on the same data without correction inflates the Type I error rate.

**Type II error** (rate $\beta$): you miss a real effect. The probability of avoiding this error is called **power** ($1 - \beta$). Power increases with sample size: larger samples make it easier to detect real effects.

Sample size matters in both directions. With 200,000 respondents, tiny and practically meaningless effects become statistically significant. With 30 observations, even large effects may not reach significance. This is why statistical significance must always be read alongside sample size and the size of the estimated effect.

---

## When Is a Regression Result Meaningful?

Statistical significance is not the same as practical importance. Three questions to ask together:

**1. Is the effect statistically significant?** A p-value below $\alpha$ tells you the pattern is unlikely to be random noise.

**2. How large is the effect?** The coefficient magnitude and its confidence interval. A statistically significant coefficient of 0.01 (happiness increases by 0.01 points per year of education) may be too small to act on.

**3. Does the effect matter in context?** A 0.4-point increase in happiness per health-rating point may be meaningful for public health policy. It may not be enough to justify an expensive individual intervention.

> **Tip:** In exploratory data science work, rather than chasing significance thresholds, focus on the coefficient with its confidence interval. The p-value is a property of the data and sample size. The coefficient and its range are properties of the phenomenon you are studying.

> **Discussion:** A data scientist reports: "Income is a statistically significant predictor of happiness (p < 0.001, $R^2 = 0.02$)", based on a survey of 200,000 people. Is this an important finding? What additional information would you need to assess its practical value?

---

## Summary

- The null hypothesis ($H_0$) assumes no effect. The p-value measures how unlikely the observed result would be if $H_0$ were true.
- A p-value below $\alpha = 0.05$ means the effect is statistically significant: unlikely to be sampling noise.
- Type I error (false positive) is bounded by $\alpha$. Type II error (missing a real effect) decreases as sample size grows.
- Statistical significance does not equal practical importance. Always assess effect size and domain relevance alongside the p-value.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Regression: Interpretation and Assumptions](03-regression-depth.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Support Vector Machines -->](05-support-vector-machines.md)

Script v1.4.1 (2026-06-23) · FGN
