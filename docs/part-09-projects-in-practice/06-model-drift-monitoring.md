> **Navigation:** [<-- Interface Design and Integration](05-interface-design-integration.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Ethics and Accountability in Production -->](07-ethics-accountability.md)

---

# Model Drift and Monitoring

**Requires**: [From Script to Production System](04-script-to-production.md) · [Generalization](../part-06-reflection/01-generalization.md) · [Choosing and Aligning Metrics](../part-06-reflection/04-aligning-metrics.md)

**Motivation**: In [🖝 Generalization](../part-06-reflection/01-generalization.md) we discussed that a held-out test set estimates how a model performs on unseen data. However, that estimate only holds as long as future data looks like the data you tested on. In production, this assumption often breaks over time: Sensors age, customers change, the world moves on. A model that once scored well can quietly rot. How do you notice before it costs you?

> This nugget covers the operating phase after deployment: data and concept drift as reasons why models degrade, and what to monitor and when to retrain.

## Table of Contents

- [Why Models Degrade: Data Drift and Concept Drift](#why-models-degrade-data-drift-and-concept-drift)
- [Monitoring in Practice: What to Track and When to Retrain](#monitoring-in-practice-what-to-track-and-when-to-retrain)
- [Summary](#summary)

## Why Models Degrade: Data Drift and Concept Drift

A model learns a relationship from a snapshot of the "world". When the world stops matching that snapshot, performance decays. This is **drift**, and it comes in essentially two forms:

- **Data drift** (also called covariate shift): the input distribution changes, even though the underlying relationship still holds. Examples include a vibration sensor slowly de-calibrates, so its readings creep away from the range the model trained on. The model is now extrapolating into territory it was never trained/validated on.
- **Concept drift**: the relationship between inputs and target itself changes. The same inputs now imply a different outcome. Examples include evolving spam or phishing tactics, where yesterday's signals may no longer hold. Another example might be shifting customer behavior after a price change.

We foreshadowed both in [🖝 Academia vs. Business Data Science](../part-01-the-big-picture/05-academia-vs-business-ds.md): real-world data brings sensor drift, calibration artifacts, and undocumented change, precisely the messiness toy datasets lack. Drift is that messiness arriving *after* deployment, on a system people already depend on.

Also note the connection to [🖝 AI Ethics: A Primer](../part-01-the-big-picture/03-ethics-and-responsibility.md) where we discussed alignment: A system optimized and validated once can drift away from the goal it was built for without anyone noticing.

> **Key fact:** Drift is not a bug you can fix once. It is a permanent condition of operating in a changing world. The goal is to detect it in time.

The challenge of drifting models is that they produce no error: degradation happens *silently*. Unaware of drift conditions, a model might return the same confident predictions as ever, even when they become increasingly wrong. Without proper guards, everything downstream keeps trusting these predictions.

The defense is monitoring, where you **evaluate against fresh data**. The old frozen test set no longer qualifies since it represents a stale state of data.

---

## Monitoring in Practice: What to Track and When to Retrain

So we need to monitor models in production. How this should done, depends largely on the application domain. Google's eigth [🔗 rule of machine learning](https://developers.google.com/machine-learning/guides/rules-of-ml) puts it this way:

> **Best practice:** Know the freshness requirements of your system.

Some models tolerate months of staleness, some experience decay in days. To notice drift, it is useful to track three layers:

- **Inputs.** Watch the distribution of incoming features against the training distribution. A shift here is a *leading* indicator of data drift. It needs no labels, so you can see it immediately.
- **Outputs.** Watch the distribution of predictions. If a fault detector suddenly flags three times as many faults, something changed, in the world or in the pipeline.
- **Performance.** When true outcomes eventually arrive (e.g., was the part really defect?), compute the performance metric using the real values [🖝 Choosing and Aligning Metrics](../part-06-reflection/04-aligning-metrics.md). This gives a ground truth measure of decay, even though it is usually delayed.

Now these methods can be used to detect drift. Depending on the insights, updating the model will sometimes be required. Depending on what you find is necessary, there are three typical triggers for maintainenance (sometimes combined into a single maintenance strategy):

| Trigger | Retrain when... |
|---|---|
| Scheduled | A fixed interval passes (e.g., monthly), matched to freshness needs |
| Drift-based | Input or output distributions cross a set threshold |
| Performance-based | The tracked metric drops below the good-enough bar ([🖝 Baselines and the Good-Enough Bar](../part-06-reflection/03-baselines.md)) |

> **Discussion:** Assuming that true outcomes for your predictions only arrive months later, you cannot measure real accuracy in real time. Input drift gives an early warning but not proof of harm. On that incomplete signal alone, when is it responsible to update/retrain a model that still seems to *report* excellent numbers?

When retraining is done, it is just another pass through the CRISP-DM inner loop on fresher data. Note that automatic retraining is possible but not free: In contrast to a common misconception that AI systems *always* improve on their own [(Nussbaum, 2023)](../references.md#nussbaum2023aimyths), when in reality maintenance is often deliberate human-designed work, even if it is carried out by automated schedules in the end.

---

## Summary

- Models degrade because the world drifts from the data they learned on. Data drift changes the inputs; concept drift changes the input-to-target relationship.
- The dangerous failures are silent: a drifting model returns confident, increasingly wrong predictions with no error.
- Monitor three layers:
    - input distributions (immediate, label-free, leading indicator)
    - output distributions
    - the real performance metric (delayed but definitive).
- Retrain on a schedule, on a drift trigger, on a performance drop, or a combination.
- Pitfall: Evaluating only against the frozen test set hides drift completely. Evaluation on fresh data is needed.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Interface Design and Integration](05-interface-design-integration.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Ethics and Accountability in Production -->](07-ethics-accountability.md)

Script v1.8.2 (2026-09-21) · FGN
