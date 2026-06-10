> **Navigation:** [<-- CRISP-DM](04-crisp-dm.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Part II: Data-Science Projects -->](../part-02-ds-projects/00-index.md)

---

# Academia vs. Business Data Science

**Requires**: [CRISP-DM](04-crisp-dm.md)

**Motivation**: The CRISP-DM phaes Business Understanding and Deployment go beyond fitting a model. But who is responsible for those phases? Here, academic and business data science are usually distinct. Both produce valid results, but they define success and scope differently. This shapes everything from the data that is used to the criteria by which you decide you are done.

> In this nugget you'll contrast academic and business data science. You'll understand how real-world data differs from the clean benchmark datasets used in most tutorials, and see where this course sits on that spectrum.

## Table of Contents

- [Different Goals and Success Criteria](#different-goals-and-success-criteria)
- [Toy Datasets vs. Real-World Data](#toy-datasets-vs-real-world-data)
- [Where This Course Sits](#where-this-course-sits)
- [Summary](#summary)

## Different Goals and Success Criteria

In a research paper, success often means a new method outperforms previous methods on a benchmark dataset. The benchmark is fixed, the metric is pre-agreed, and "better" is a precise number. The work is done when you can report the improvement. Business works differently:

> In a business or engineering context, success means the project produces **value** for someone.

Value might be reduced maintenance cost, fewer missed faults, faster quality control, or a decision made with higher confidence. The metric is not pre-agreed: It has to be negotiated with stakeholders. These stakeholders usually think in terms of hours saved or defects per batch, not "F1 scores" (a classification metric that we'll encounter later). A model with a good score in whatever your metric might be excellent for one use case and worthless for another.

This difference has a practical consequence:

> A data scientist in industry needs to own the full process, including Business Understanding and Deployment. A researcher publishing a new algorithm can stop after Evaluation (the inner loop).

Unfortunately, the academic world has a strong incentive to report positive results. Methods that demonstrate improvements get published much easier than insights that demonstrate something does not work. In business, there is no such filter. Projects fail, datasets turn out to be unusable, questions turn out to be unanswerable with the available data, and the honest response is to stop and say so.

> Recognizing when to stop is a professional skill in data science.

---

## Toy Datasets vs. Real-World Data

Many canonical teaching datasets in machine learning (like the _iris flowers_ or the _MNIST_ handwritten digits) are clean, complete, well-labelled, and small enough to fit in memory. They are ideal for learning a new algorithm because the data is not the problem.

Real-world data is different in almost every dimension. Here are some trends:

| Property | Benchmark / toy datasets | Real-world data |
|---|---|---|
| Missing values | Rare or absent | Common, often systematic |
| Labelling | Complete, often expert-verified | Partial, noisy, sometimes incorrect |
| Size | Hundreds to thousands of rows | Millions of rows, or too few |
| Cleanliness | High | Variable (often poor) |
| Bias | Often documented | Often unknown or undocumented |
| Relevance to question | Built-in | Must be verified |

In an engineering context, you can add to the real-world challenges: sensor drift over time, calibration artefacts, measurement noise, data collected on one instrument that is then applied to a slightly different one.

> Your domain knowledge is immensely valuable  for recognizing these issues. A data scientist without that background will often miss them or misattribute them to the wrong cause.

The 80/20 rule-of-thumb states that roughly 80% of project time goes to data work and only 20% to modeling (see also: [🖝 Why Data Work Dominates](../part-03-data-understanding/01-why-data-work.md)). It is a direct consequence of this gap between toy and real data. You will likely experience this once you work on real data.

---

## Where This Course Sits

This course is positioned on the business and engineering side of the spectrum, for practical reasons.

> You are more likely to spend your career solving a specific problem with real data rather than winning a benchmark competition.

The skills that transfer are:

- scoping a question that is actually answerable,
- understanding what your data can and cannot support,
- building a model that is honest about its performance, and
- communicating results to people who may not understand the technical ground work, but who need to act on the results.

At the same time, this course does not skip the inner-loop methods. You will learn regression, classification, clustering, and deep learning. The difference is that you learn them as tools within the CRISP-DM cycle, not as algorithms in isolation.

For this course, I'd like to encourage you to work on a personal project alongside. The idea is to have a small but complete engineering data-science project. You define a question, assess the data, build a model, evaluate it honestly, and present the result.

The benchmark-style shortcut is not the goal: We don't simply want to download a clean dataset and score a model against a preset metric. We'll try to move beyond. This is harder than standard tutorials. It is also closer to real work. We'll discuss how to find and initiate personal projects in [🖝 Part II: Personal Data-Science Projects](../part-02-ds-projects/00-index.md).

---

## Summary

- Academic data science optimizes for benchmark improvement and publication. Business data science optimizes for real-world value with real stakeholders and negotiated success criteria.
- A single metric value means nothing without context: the use case determines what counts as good enough.
- Real-world data is messy in ways toy datasets are not: missing values, label noise, sensor artefacts, undocumented bias.
- Data work typically dominates project time. Modelling is a smaller fraction than most tutorials suggest.
- This course trains the full CRISP-DM cycle, a personal  mini-project is encouraged alongside for best learning outcomes.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- CRISP-DM](04-crisp-dm.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Part II: Data-Science Projects -->](../part-02-ds-projects/00-index.md)

Script v1.4 (2026-06-10) · FGN
