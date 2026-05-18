> **Navigation:** [<-- Regularized Regression](05-regularized-regression.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Classification Tasks -->](07-classification-tasks.md)

---

# Hyperparameter Optimization

**Requires**: [Train/Test Split](02-train-test-split.md) · [Regularized Regression](05-regularized-regression.md)

**Motivation**: [🖝 Regularized Regression](../part-05-supervised-learning/05-regularized-regression.md) introduced a "knob" that controls how strongly the model is penalized for large weights. Turn it too low and the model may still overfit. Turn it too high and weights shrink so aggressively that genuine signal is lost. Training cannot set this knob automatically: the optimizer would simply drive regularization toward zero to recover plain regression. Settings the optimizer cannot determine from training data are called **hyperparameters**, and choosing them is its own problem.

> In this nugget you will learn what distinguishes hyperparameters from learned parameters, why you need a separate held-out set to evaluate them, and how grid search automates the tuning process.

## Table of Contents

- [What Are Hyperparameters?](#what-are-hyperparameters)
- [The Validation Set](#the-validation-set)
- [Grid Search and Beyond](#grid-search-and-beyond)
- [Summary](#summary)

## What Are Hyperparameters?

Every model has two kinds of parameters.

**Learned parameters** are adjusted during training to minimize the loss: the weights $\mathbf{w}$ in linear and regularized regression are examples. The optimizer handles these automatically.

**Hyperparameters** are fixed before training and remain outside the optimizer's reach. The regularization strength $\lambda$ in Ridge and Lasso is the example we have seen so far: it controls how strongly the penalty term pulls weights toward zero, but training cannot determine its value.

> If you let the optimizer select $\lambda$, it would simply drive it toward zero, removing the penalty entirely and recovering plain linear regression.

*Similar patterns of hyperparameters appear in other model families. A decision tree has a `max_depth` knob that limits how many splits it can make; a random forest has `n_estimators`. We return to these in [🖝 Decision Trees](../part-05-supervised-learning/09-decision-trees.md) and [🖝 Random Forests](../part-05-supervised-learning/10-random-forests.md).*

---

## The Validation Set

The test set was introduced in [🖝 Train/Test Split](../part-05-supervised-learning/02-train-test-split.md) as a held-out set reserved for final evaluation. It must not influence any training decision, including hyperparameter choice.

> **A pitfall**: If you evaluated many candidate values of $\lambda$ on the test set and kept the best, you would effectively select the value that happened to look good on those specific examples. The test score would _no_ longer be a fair estimate of generalization.

The solution is a third split, the **validation set**. All data is now divided into three subsets:
- **Training/Train set**: to fit model weights,
- **Validation/Val set**: to compare hyperparameter candidates,
- **Test set**: touched only once, after the final model is chosen, to produce the number you report.

For small datasets, holding out a fixed validation slice wastes data. **Cross-validation** is the standard remedy: It splits training data into $k$ folds, each fold taking a turn as the validation set. This gives a more stable estimate at the cost of fitting the model $k$ times. You'll revisit cross-validation in [🖝 Overfitting and Generalization](../part-06-reflection/01-overfitting-and-generalization.md).

---

## Grid Search and Beyond

With a validation strategy in place, hyperparameter tuning becomes a search problem: evaluate candidate settings, compare validation scores, keep the best.

### Grid Search

> You can try all of the following in the **Regularized Regression** demo from my [✪ interactive data-science demos](https://github.com/fgnussbaum/ds-ml-interactive-demos) repository.

**Grid search** defines an explicit set of candidate values and evaluates every one, using cross-validation to score each. To see it in action, consider predicting disease progression from certain clinical variables (age, sex, BMI, blood pressure, etc.) using the [sklearn diabetes dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html).

For the systematic search for the best regularization parameters, we reformulate the loss as 

$$(1-\alpha)\cdot\text{MSE}(\mathbf{w}) + \alpha\cdot\|\mathbf{w}\|,\quad \alpha\in[0,1).$$
Here, $\alpha$ now acts as the _weight_ of the penalty term. Crucially, $\alpha$ is a bounded reparameterization of the $\lambda \in [0, \infty)$ that we used in [🖝 Regularized Regression](../part-05-supervised-learning/05-regularized-regression.md). This allows us to sweep the regularization strength $\alpha$ from 0 to 1 for both Ridge and Lasso. The trade-off is the same: $\alpha=0$ is unregularized, $\alpha=1$ would mean only regularization.

Here are the RMSE error curves for train/val sets of the diabetes dataset. Only the range $\alpha\in[0, 0.1]$ is shown with a fine **grid step size** of $10^{-3}$:

<p><center><img src="../media/demos-screenshots/diabetes-error-curves.jpg" alt="Error curves (train/val data) for alpha in [0,1] for Ridge/Lasso" width="500px"/></center></p>

Observe that the training error (blue) increases as $\alpha$ increases. This is because more regularization give the model less opportunity to fit the training data closely. The validation error curve respectively shows a sweet spot where regularization improves generalization the most.

> Remember: Generalization is the main goal.

Grid search finds this sweet spot for $\alpha$ automatically. However, efficiency greatly depends on finding the right step size and sometimes the right sub-interval of $\alpha$-values where to look more closely.

Next, the coefficient paths reveal what is happening inside the model as $\alpha$ varies.

<p><center><img src="../media/demos-screenshots/diabetes-coefficient-pathsL1L2.jpg" alt="coefficient paths of L2 (left) and L1 (right) across alpha ranges" width="500px"/></center></p>

Ridge (L2, left) shrinks all coefficients gradually toward zero without eliminating any. Lasso (L1, right) drives several coefficients to exactly zero at higher $\alpha$ values, selecting a sparse subset of features. This matches the theoretical behavior that we discussed in [🖝 Regularized Regression](../part-05-supervised-learning/05-regularized-regression.md).

### Practical tips and alternatives

When tuning hyperparameters, there is a danger to spend too much time trying candidates in a region where the effect is negligible. Two strategies can help for grid search:
- **Coarse-to-fine**: starting with a coarse grid first, then iteratively refining to finer grids (smaller step size) in regions of interest
- using a **logarithmic grid**.

Here's some example code:

```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

param_grid = {"alpha": [0.01, 0.1, 1.0, 10.0]}
search = GridSearchCV(Ridge(), param_grid, cv=5)  # cv: 5 folds for cross-validation
search.fit(X_train, y_train)
print(search.best_params_)
```

Grid search is exhaustive and predictable, but the number of evaluations grows exponentially in the number of hyperparameters. Instead you can also do **Random search**, which samples combinations randomly from a defined range instead of enumerating every point. This is often competitive with grid search at a fraction of the cost, because not all hyperparameters affect performance equally.

"Smart" random sampling could even be used to avoid wasting evaluations in regions that matter little. It's possible to build sophisticated strategies based on this insight. If you are curious, check out our paper [🔭 Efficient Regularization Parameter Selection](https://www.ijcai.org/proceedings/2019/0330.pdf) (2019). However, my honest recommendation in practice is this: [🖝 Start Simple](../part-06-reflection/03-start-simple.md).

---

## Summary

- Hyperparameters are settings fixed before training that the optimizer cannot tune automatically.
- Evaluating hyperparameter candidates on the test set inflates performance estimates. This is why a separate validation set is required (alternatively cross-validation).
- Grid search exhaustively evaluates a defined candidate set. For scale-sensitive parameters like regularization strength you may want to start with a coarse or logarithmic grid.
- Random search samples randomly from a range and is often equally effective at lower cost, especially when many hyperparameters are involved.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Regularized Regression](05-regularized-regression.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Classification Tasks -->](07-classification-tasks.md)

Script v1.1 (2026-05-18) · FGN
