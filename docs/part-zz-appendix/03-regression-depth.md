> **Navigation:** [<-- Preparing Non-Tabular Data](02-beyond-tabular-prep.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Statistical Significance -->](04-statistical-significance.md)

---

# Regression: Interpretation and Assumptions

**Requires**: [Linear Regression](../part-05-supervised-learning/02-linear-regression.md)

**Motivation**: Your regression model on the ESS dataset gives $R^2 = 0.18$. You know that number measures something, but what exactly? A statsmodels summary also reports heteroscedasticity flags and coefficient p-values that are easy to skip. These are not footnotes. $R^2$ can overstate fit when predictors are added carelessly, violated assumptions can silently bias coefficient estimates, and unread residual plots hide systematic errors that RMSE alone will not catch.

> In this optional nugget you will learn what $R^2$ truly measures and when it misleads, how to interpret regression coefficients in multi-variable models, the classical assumptions that linear regression relies on, and how to diagnose violations with residual plots.

> **Context:** This nugget extends [🖝 Linear Regression](../part-05-supervised-learning/02-linear-regression.md). You should be comfortable with fitting a multi-variable model and reading MSE and RMSE before working through this material.

TBD: Rework

## Table of Contents

- [R²: What the Number Really Means](#r²-what-the-number-really-means)
- [Reading Regression Coefficients](#reading-regression-coefficients)
- [Assumptions of Linear Regression](#assumptions-of-linear-regression)
- [Residual Diagnostics](#residual-diagnostics)
- [Summary](#summary)

## R²: What the Number Really Means

$R^2$ is defined as:

$$R^2 = 1 - \frac{\text{SS}_\text{res}}{\text{SS}_\text{tot}}$$

where $\text{SS}_\text{res} = \sum(y_i - \hat{y}_i)^2$ is the residual sum of squares — the variance the model could not explain — and $\text{SS}_\text{tot} = \sum(y_i - \bar{y})^2$ is the total variance in the target relative to the training mean.

When $R^2 = 0.18$ on the ESS happiness model: the model explains 18% of the variance in happiness. The remaining 82% is unexplained. That is not the same as saying the model is useless — happiness is genuinely noisy, and partial explanation can still be valuable — but it requires comparing against baselines and domain expectations before drawing conclusions.

### Three ways R² can mislead

**Adding predictors always increases R² on the training set.** Every new variable, even a random one, explains a small slice of training-set noise. Training-set $R^2$ therefore overstates quality when comparing models with different numbers of features.

**Adjusted R²** corrects for this:

$$\bar{R}^2 = 1 - (1 - R^2)\frac{n-1}{n-k-1}$$

where $n$ is the number of training samples and $k$ is the number of predictors. Adjusted $R^2$ penalizes for complexity and can decrease when a new predictor contributes less signal than it costs. Use adjusted $R^2$ when comparing models that differ in the number of features.

**Test-set R² can be negative.** $R^2$ is defined relative to the training-set mean $\bar{y}$. If the model's predictions on the test set are worse than simply predicting $\bar{y}$, test-set $R^2$ goes below zero. This is a clear signal of overfitting or a distribution shift between train and test.

**R² says nothing about whether residuals are well-behaved.** Two datasets can have identical $R^2$ values while one has systematic patterns in its residuals that the model has entirely missed — Anscombe's quartet is the canonical demonstration (Anscombe, 1973). $R^2$ is always read alongside residual diagnostics, not in isolation.

---

## Reading Regression Coefficients

In a multi-variable model:

$$h_w(\mathbf{x}) = w_0 + w_1 x_1 + w_2 x_2 + \cdots + w_n x_n$$

each coefficient $w_j$ means: holding all other predictors constant, a one-unit increase in $x_j$ is associated with a $w_j$ change in the predicted target. The phrase "holding all other predictors constant" is the critical qualifier — it distinguishes a regression coefficient from a simple correlation.

In the ESS model, if health ($x_1$) has coefficient 0.4 and social contact frequency ($x_2$) has coefficient 0.1, it means: among people with the same social contact frequency, a one-unit difference in health corresponds to 0.4 more predicted happiness points.

### Direction, magnitude, and scale

A positive coefficient means the predictor moves with the target; a negative coefficient means it moves against it. Coefficient magnitudes are on the scale of the input feature, so raw magnitudes are not comparable across features unless inputs are standardized first. After standardization, the magnitude of each coefficient becomes the number of standard deviations by which the prediction changes per standard deviation of the predictor.

### Multicollinearity

If two predictors are strongly correlated with each other, the model can distribute their joint effect across both coefficients in many equivalent ways. The individual coefficients become unstable: small changes in the data can flip their signs or inflate their magnitudes. This is **multicollinearity**. The model's overall predictions can remain accurate, but individual coefficient interpretation becomes unreliable.

A practical signal: adding or removing one correlated predictor causes large swings in another predictor's coefficient. Variance Inflation Factor (VIF) formalizes this — a VIF above 5–10 for a predictor signals problematic collinearity. Ridge regression (L2 regularization) shrinks unstable coefficients and is a practical remedy; this is one of the core motivations for [🖝 Regularized Regression](../part-05-supervised-learning/05-regularized-regression.md).

---

## Assumptions of Linear Regression

The ordinary least-squares estimator is optimal under five classical assumptions. Violations do not necessarily make the model unusable, but they affect what you can reliably claim about the coefficients and significance tests.

**1. Linearity.** The relationship between each feature and the target is linear. If the true relationship is curved, the model will systematically underpredict in some ranges and overpredict in others. Check with scatter plots of each predictor against the target and with the residual vs. fitted plot.

**2. Independence of errors.** The residual for one observation does not depend on the residual for another. This is violated by time series (consecutive observations are correlated) and by clustered data (e.g., students within the same school share unmeasured influences). When errors are correlated, standard errors underestimate variability and significance tests become anti-conservative.

**3. Homoscedasticity.** The variance of residuals is constant across all levels of the fitted value. The opposite, **heteroscedasticity**, means residuals fan out or compress as the fitted value changes. A model predicting income might have small, tight errors for low earners and large, scattered errors for high earners. Heteroscedasticity does not bias coefficient estimates, but it inflates or deflates standard errors, making significance tests unreliable.

**4. Normality of residuals.** Residuals are approximately normally distributed around zero. This matters for confidence intervals and p-values. With large samples, the central limit theorem provides robustness. With small samples, strong non-normality distorts significance tests.

**5. No perfect multicollinearity.** No predictor can be expressed as an exact linear combination of others. Perfect collinearity makes the least-squares system unsolvable. Near-perfect collinearity is the practical concern, addressed in the previous section.

---

## Residual Diagnostics

Residual plots are the standard tool for checking whether assumptions hold. Scikit-learn does not produce them; use `statsmodels` or construct them manually from the residuals array (`y_test - model.predict(X_test)`).

### Residual vs. fitted plot

Plot residuals $y_i - \hat{y}_i$ on the y-axis against fitted values $\hat{y}_i$ on the x-axis. Under correct assumptions, residuals should scatter randomly around zero with constant spread and no pattern. A curved band indicates non-linearity. A funnel shape — residuals spreading wider as the fitted value increases — indicates heteroscedasticity.

[Figure: Two side-by-side residual vs. fitted plots. Left: random scatter around zero with constant spread — assumptions satisfied. Right: fan-shaped spread increasing with fitted value — heteroscedasticity present.]

### Scale-location plot

Plot the square root of the absolute standardized residuals against fitted values. A roughly flat loess line confirms homoscedasticity. An upward slope confirms heteroscedasticity.

### Q-Q plot of residuals

Plot the quantiles of the standardized residuals against the quantiles of a standard normal distribution. Points falling on the diagonal confirm approximate normality. Heavy tails — points curving away from the diagonal at both ends — signal a distribution heavier than normal.

### What to do about violations

Heteroscedasticity can often be reduced by transforming the target (e.g., log-transforming income, which has a right-skewed distribution). Non-linearity may call for polynomial features or a tree-based model. Correlated errors in time-series data require specialized methods outside the scope of this course.

---

## Summary

- $R^2$ measures the fraction of target variance explained. It always increases with more predictors on the training set; use adjusted $R^2$ when comparing models of different sizes.
- Test-set $R^2$ can be negative when a model is worse than predicting the training mean — a reliable sign of overfitting or distribution shift.
- Regression coefficients carry a "holding all else constant" interpretation. Multicollinearity destabilizes individual coefficients even when overall predictions remain accurate.
- Linear regression rests on five assumptions: linearity, independence of errors, homoscedasticity, normality of residuals, and no perfect multicollinearity.
- Residual vs. fitted, scale-location, and Q-Q plots are the standard diagnostic tools. Always inspect them before reporting model results.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Preparing Non-Tabular Data](02-beyond-tabular-prep.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Statistical Significance -->](04-statistical-significance.md)

Script v1.5 (2026-06-24) · FGN
