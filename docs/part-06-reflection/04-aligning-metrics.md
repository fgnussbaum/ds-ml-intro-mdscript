> **Navigation:** [<-- Baselines and the Good-Enough Bar](03-baselines.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Explainability -->](05-explainability.md)

---

# Choosing and Aligning Metrics

**Requires**: [Baselines and the Good-Enough Bar](03-baselines.md) · [Classification Evaluation](../part-05-supervised-learning/08-classification-evaluation.md)

**Motivation**: The [🖝 Baselines and the Good-Enough Bar](../part-06-reflection/03-baselines.md) nugget just showed that domain requirements must be translated into a metric before training begins. But which metric, and what makes it the right choice? Since metrics are optimization targets, they are no "neutral" measurements: A model optimized for accuracy on an imbalanced dataset learns to predict the majority class for nearly everything, and a model optimized for average call-handling speed learns to hang up on difficult callers. In both cases, the metric is looking good **but the goal is not achieved**.

> Here, you'll learn why metric choice is one of the highest-leverage decisions in any ML project, how to frame error costs in your specific domain, and how to recognize when a technically correct metric conflicts with the business goal or produces ethically problematic outcomes.

> **Interactive demo note:** In the **Classification game** demo from my [✪ interactive data-science demos](https://github.com/fgnussbaum/ds-ml-interactive-demos) repository, you can test your reading skills and calibration of metrics, as well as practice several machine learning principles, including _start simple_ and _one change at a time_.

## Table of Contents

- [Metrics as Optimization Targets](#metrics-as-optimization-targets)
- [From Standard Metrics to Real Costs](#from-standard-metrics-to-real-costs)
- [When Metric, Business Goal, and Ethics Diverge](#when-metric-business-goal-and-ethics-diverge)
- [Summary](#summary)

## Metrics as Optimization Targets

Most training algorithms optimize the model parameters to maximize (or minimize) a loss function. The loss function can be seen as a specific metric. As a result, the model gets better at exactly what it is measured on. If the metric is a good proxy for what you actually want, the model improves along the right dimension. If the metric is a poor proxy, you get a model that performs on the metric while failing the goal.

The economist Charles Goodhart observed this dynamic in a broader social context:

> **[🔗 Goodhard's Law](https://en.wikipedia.org/wiki/Goodhart%27s_law):** When a measure becomes a target, it ceases to be a good measure.

In machine learning, this is encoded in the optimization procedure. Choosing the right metric is therefore more than a technical detail.
Let's review metrics for the task types we have considered so far. As a quick reference.

**Regression metrics.** [🖝 Linear Regression](../part-05-supervised-learning/02-linear-regression.md) introduced MSE and MAE. Here, we add a third metric:

| Metric | What it emphasizes | When to use it |
|--------|-------------------|----------------|
| Mean Squared Error (MSE) | Large errors penalized quadratically | When large errors are disproportionately costly |
| Mean Absolute Error (MAE) | All errors weighted equally | When error magnitude matters but outliers should not dominate |
| Mean Absolute Percentage Error (MAPE) | Relative error | When errors should be proportional to the target magnitude |

**Classification metrics.** [🖝 Classification Evaluation](../part-05-supervised-learning/08-classification-evaluation.md) introduced precision, recall, and F1 with a focus on mechanics. Here the focus shifts to alignment. Each metric encodes an implicit assumption about error costs.

| Metric | What it measures | Implicit cost assumption |
|--------|-----------------|--------------------------|
| Accuracy | Fraction of correct predictions | All errors cost the same; classes are balanced |
| Precision | Of predicted positives, fraction correct | False alarms are more costly than misses |
| Recall | Of actual positives, fraction found | Missed cases are more costly than false alarms |
| F1 | Harmonic mean of precision and recall | Both error types matter with potentially imbalanced classes |

Choosing a metric is choosing which of these cost assumptions best fits your problem. The next section makes that choice explicit and, where possible, quantitative.

---

## From Standard Metrics to Real Costs

Standard classification metrics encode implicit cost assumptions. Accuracy treats every misclassification equally. F1 weights false positives and false negatives symmetrically. In most real applications, these assumptions do not hold.

When you work on a problem, you have to ask: Is one of the error types more damaging in your domain?

| Domain | Critical error | Primary metric |
|--------|---------------|----------------|
| Equipment fault detection | FN (missed fault) | Recall |
| Medical screening | FN (missed case) | Recall |
| Spam filtering  | FP (blocked real email) | Precision |
| Fraud detection | FN (missed fraud) | Recall |
| Balanced binary classification | Equal | F1 or Accuracy |
| Imbalanced binary classification | Depends | F1 |

When costs can be quantified, for example as a Euro amount, a patient outcome, or a regulatory penalty, then the assumption can usually be made explicit.

There is no "patent solution" for this. Here, we just provide a simple mathematical cost model.
Let $C_{FP}$ be the cost of one false positive and $C_{FN}$ the cost of one false negative. At false-positve and false-negative rates $\rho_{FP}$ and $\rho_{FN}$, the expected cost per prediction is:

$$\hat{C} = \rho_{FP} \cdot C_{FP} + \rho_{FN} \cdot C_{FN}$$

Minimizing $\hat{C}$ optimizes costs. The optimal classification threshold depends on the ratio $C_{FN} / C_{FP}$: when missed cases cost ten times as much as false alarms, the threshold should shift toward predicting positive more aggressively, accepting more false alarms to avoid more misses.

> **Try it out:** In [✪ interactive data-science demos](https://github.com/fgnussbaum/ds-ml-interactive-demos), the "classification game demo" lets you set $C_{FP}$ and $C_{FN}$ and observe how this guides modeling choices. Try extreme cost ratios to see how precision and recall trade off against total cost.

What cost model you use for business metrics really depends on your application and how rigorous you need to calculate numbers to satisfy business requirements.

For business cases or pitching project for stakeholders, you'll also include something like the value you get from each prediction. This is usually not discussed in academic literature.

In my [✪ Plan. Pitch. Perform.](https://www.researchgate.net/publication/392654581_Plan_Pitch_Perform_From_Data_Science_Idea_to_Funded_Project) paper, I published a few additional real cost metrics, based on my industry experience. But even this is rather specific. Practical work requires taking the domain and business context into account. We also only touched modeling real costs for (binary) classification here. However, for any kind of data science problem, similar considerations apply.

---

## When Metric, Business Goal, and Ethics Diverge

We already emphasized it: A  metric that accurately measures what it claims to measure may still fail to align with the actual goal. Three levels of misalignment deserve explicit attention.

### Metric and business goal

Does improving the metric translate to a better outcome in practice?

A model with lower mean average error may still be operationally useless if its worst-case errors occur precisely in the high-stakes cases. A model with high F1 may require a deployment infrastructure that makes the latency too high for real-time use.

> **Important:** The metric is a proxy for business value, and proxies can miss.

### Metric and task

Does the metric capture what the task requires?

A model evaluated on accuracy alone may ignore systematic failures on the minority class. A model evaluated on mean squared error may produce predictions that are accurate on average but occasionally catastrophically wrong.

> **Important:** The metric must be sensitive to the failure modes that matter.

### Metric and ethics

Optimizing any metric can produce outcomes that are systematically unfair to particular groups. This happens because:

- The training data may underrepresent some groups, causing the model to be less accurate for them even though overall accuracy is high.
- A metric like accuracy treats all errors equally, even when errors are concentrated in a specific group.

For example, models optimizing for recall in risk-scoring contexts (credit scoring, insurance pricing) may produce systematically higher false positive rates for disadvantaged groups, giving them worse scores than the data actually justifies.

Fairness-aware metrics that [🔗 equalize odds](https://en.wikipedia.org/wiki/Equalized_odds), ensure demographic parity or calibrate otherwise for subgroups exist to detect and correct this kind of divergence. They usually do not replace the primary metric. However:

> **Important:** Fairness-aware metrics must be examined as additional dimensions whenever the model's decisions affect people's lives.

The importance of AI ethics was introduced in [🖝 AI Ethics: A Primer](../part-01-the-big-picture/03-ethics-and-responsibility.md). Choosing a metric is where ethical framing becomes a concrete engineering decision.

> **Discussion:** A model predicts whether a patient should receive a specialist referral. The development team optimized for overall accuracy. After deployment, a clinical audit shows that patients from a particular region are referred at a much lower rate than baseline clinical practice would suggest, while patients from wealthier regions are referred at a higher rate. What does this finding suggest about the metric choice? What would you do before the next deployment?

---

## Summary

- Metrics are optimization targets: the model gets better at exactly what it is measured on. Choosing the wrong metric produces a model that achieves the metric while failing the goal.
- False positives and false negatives have different costs in different domains.
- Match the primary metric to the error type that is most costly in your application: recall when misses are costly, precision when false alarms are costly, F1 when both matter and classes are imbalanced.
- Alignment of metrics must be checked at three levels: with business goals, with task, and with ethics. Optimizing a technically correct metric can still produce systematically unfair outcomes if the metric does not account for disparate impact across groups.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Baselines and the Good-Enough Bar](03-baselines.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Explainability -->](05-explainability.md)

Script v1.5 (2026-06-24) · FGN
