> **Navigation:** [<-- Ethics and Accountability in Production](07-ethics-accountability.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Your Advantage -->](09-your-advantage.md)

---

# Troubleshooting, Pitfalls, and When to Ask for Help

**Requires**: [CRISP-DM Retrospective: From Coursework to Real Projects](01-crisp-dm-retrospective.md) · [EDA: Data Quality](../part-03-data-understanding/05-eda-data-quality.md) · [Data Splits](../part-04-data-preparation/04-data-splits.md) · [Underfitting and Overfitting](../part-05-supervised-learning/04-under-overfitting.md) · [Choosing and Aligning Metrics](../part-06-reflection/04-aligning-metrics.md)

**Motivation**: Moving from development to production comes with several challenges. With experience, you'll develop ways to find causes reliably. Here, a collection of trouble-shooting "best practices" won't hurt.

> This nugget names common failure modes of data-science projects and outlines how to debug when something is not working, including when to bring in help.

## Table of Contents

- [Common Failure Modes in Data-Science Projects](#common-failure-modes-in-data-science-projects)
- [How to Approach a Project When Something Isn't Working](#how-to-approach-a-project-when-something-isnt-working)
- [Knowing Your Limits: When to Bring in a Specialist](#knowing-your-limits-when-to-bring-in-a-specialist)
- [Summary](#summary)

## Common Failure Modes in Data-Science Projects

Most project failures have been run into before, so it's good to draw on prior lessons. Here are some of the usual suspects to screen:

| Symptom | Likely cause | Where you met it |
|---|---|---|
| Great in dev, poor in production | Data leakage or shift | [🖝 Model Drift and Monitoring](../part-09-projects-in-practice/06-model-drift-monitoring.md), [🖝 Data Splits](../part-04-data-preparation/04-data-splits.md) |
| Good on training data, poor on test | Overfitting | [🖝 Underfitting and Overfitting](../part-05-supervised-learning/04-under-overfitting.md) |
| High metric, unhappy stakeholders | Metric misaligned with the goal | [🖝 Choosing and Aligning Metrics](../part-06-reflection/04-aligning-metrics.md) |
| Nonsensical or unstable predictions | Data quality: errors, missing values, bias | [🖝 EDA: Data Quality](../part-03-data-understanding/05-eda-data-quality.md) |
| Model no better than guessing | Wrong framing, or no signal in the data | [🖝 Baselines and the Good-Enough Bar](../part-06-reflection/03-baselines.md) |

Only some of these are modeling problems, generally data-science project failures split two-way [(Nussbaum, 2025)](../references.md#nussbaum2025planpitch):

- technical causes (leakage, overfitting, unstable models, ...)
- business-side causes (unclear goals, development disconnected from users, and misunderstood AI capabilities).

A technically flawless model solving the wrong problem is still a failed project. Models built on misframed questions can be avoided by not rushing through the Business Understanding and Data Understanding phases.

---

## How to Approach a Project When Something Isn't Working

Random tweaking is the slowest way to fix a problem. Use a structured pass instead:

1. **Reproduce the problem.** Confirm the problem is real and consistent before chasing it. Fix your random seeds so behavior is stable across runs.
2. **Check the data first.** Given that data work dominates real projects, the data is often the culprit. Before touching the model: Re-run quality checks and look hard for leakage, drift, and label problems.
3. **Re-check the framing.** Always step back to Business Understanding. Are you optimizing the right metric for the actual goal? Sometimes the model is fine and the question was wrong.
4. **Change one thing at a time.** This is the principle from [🖝 Start Simple](../part-06-reflection/02-start-simple.md). If you alter multiple things at once, you don't know what caused the result to change.

Most real debugging is disciplined elimination. Let [🖝 CRISP-DM](../part-01-the-big-picture/04-crisp-dm.md) guide you (see also [🖝 CRISP-DM Retrospective: From Coursework to Real Projects](../part-09-projects-in-practice/01-crisp-dm-retrospective.md)).

> **Tip:** When stuck, timebox your own analysis before asking for help, compare what keeps team projects moving in [🖝 Working as a Team on a DS Project](../part-02-ds-projects/03-team-project-basics.md). It's always a trade-off: Three hours alone on something a colleague resolves in ten minutes is probably a coordination failure.

---

## Knowing Your Limits: When to Bring in a Specialist

Part of professional competence is recognizing where yours ends. Trust and credibility are built partly by admitting what you do not know rather than bluffing past it [(Nussbaum, 2023)](../references.md#nussbaum2023communication). Others will appreciate honesty about, especially when paired with a good work mindset (e.g., open for learning, growth-driven, etc.).

Bring in help when:

- **The problem is research-grade.** No reference solution exists and progress needs techniques no one on the team has, so it is not just mechanical delivery from the perspective of the team's compentencies, see also [🖝 Academia vs. Business Data Science](../part-01-the-big-picture/05-academia-vs-business-ds.md).
- **The stakes are ethical or legal.** Fairness in a high-stakes decision or a compliance question deserves the right specialist, see [🖝 Ethics and Accountability in Production](../part-09-projects-in-practice/07-ethics-accountability.md).
- **The blocker is outside your discipline.** Production infrastructure, data engineering at scale, and hardened deployment are their own crafts. This is why real projects are staffed by mixed teams.

The skill this course builds is not knowing every method. It is knowing the *process* well enough to work a new problem methodically, and to tell the difference between a gap you can close by learning vs. one that needs another expert.

> **Discussion:** Admitting "I can't solve this alone" builds long-term credibility. In the moment, it may feel like it costs some standing. You might feel you need to provde yourself, especially early in a career. How do you weigh honesty about your limits against the pressure to appear capable? How do you protect your integrity from start?

---

## Summary

- Failure modes repeat:
    - leakage, overfitting, metric misalignment, and data-quality problems on the technical side
    - unclear goals and disconnection from users on the business side.
- A technically sound model solving the wrong problem is still a failure.
- Debug by structured elimination, not random tweaking: reproduce, check the data, change one thing at a time, re-check the framing.
- Rushing through Business and Data Understanding can be costly.
- Knowing your limits is a professional skill.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Ethics and Accountability in Production](07-ethics-accountability.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Your Advantage -->](09-your-advantage.md)

Script v1.8.2 (2026-09-21) · FGN
