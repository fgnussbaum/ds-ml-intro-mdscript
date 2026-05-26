> **Navigation:** [Part Index](00-index.md) | [Main Index](../index.md) | [Data Types and Measurement Scales -->](02-data-types.md)

---

# Why Data Work Dominates

**Requires**: [CRISP-DM](../part-01-the-big-picture/04-crisp-dm.md)

**Motivation**: You have seen the CRISP-DM map, which places Data Understanding and Data Preparation as two of its central phases. You may have assumed that modeling would take up most of your time on a real project. This nugget challenges that assumption: what if data work is not a preliminary step you get through quickly, but the dominant activity — by a wide margin?

> You will understand why data preparation typically consumes roughly 80% of real project time and learn to recognize the common failure modes that poor data quality introduces — from silent model errors to sampling bias — so that you enter projects with accurate expectations.

## Table of Contents

- [The 80/20 Reality of Real Projects](#the-8020-reality-of-real-projects)
- [What Can Go Wrong with Bad Data](#what-can-go-wrong-with-bad-data)
- [Setting Your Expectations](#setting-your-expectations)
- [Summary](#summary)

## The 80/20 Reality of Real Projects

You may have come into this course expecting to spend most of your time building models. Sorry to tell you: That is rarely how real projects go.

> In practice, roughly 80% of technical work during projects goes into finding, understanding, cleaning data and building robust data pipelines for it. The remaining 20% covers modelling and evaluation.

Surveys (TODO source) consistently report the same pattern, and it aligns with what the [🖝 CRISP-DM](../part-01-the-big-picture/04-crisp-dm.md) shows: Data Understanding (this part) and Data Preparation (part IV) together usually span the largest share of project lifecycles.

Several forces drive this:

- **Data is never ready.** More often than not real datasets arrive with missing values or attributes,inconsistent formats and coding, and undocumented conventions. Add sensors malfunctions, misunderstood survey questions, and subobtimal automation. There's always work left.
- **Domain understanding takes time.** Before you can clean a column, you need to know what it represents. A reading of $-999$ might mean "sensor offline," not a real measurement. You cannot know this without reading the documentation or talking to someone who ran the experiment.
- **Early decisions compound.** How you handle missing values in the first cleaning step shapes every downstream operation. Getting it wrong creates silent errors that carry forward through modelling and evaluation.

> **Discussion:** If you do laboratory work: How much time do you spend collecting and cleaning data versus actually analyzing it?

---

## What Can Go Wrong with Bad Data

Poor data quality rarely announces itself. The model trains, a number comes out, and only later, sometimes in deployment, does the problem surface. Here are the most common failure modes.

- **Target variable misrepresented.** A mislabeled target variable, a systematic sensor bias, or a dataset that does not represent the population you care about will yield a model that is confidently wrong. Training and validation scores may look fine because the flaw is present in both sets equally.
- **Data shifts cause silent model failures.** Models trained on one data distribution degrade when that distribution shifts. If your training data comes from one time period or one operating condition, the model may produce worse outputs on new data without raising any error, just quietly getting things wrong.
- **Development-deployment pipeline mismatch.** Preprocessing steps applied during training must be replicated exactly at inference time. If scaling parameters, encoding decisions, or missing-value handling are not saved and reapplied correctly, the model receives inputs it was never trained on.
- **Sampling bias.** If the data collection process systematically over- or under-represents certain groups or conditions, every conclusion inherits that bias. Survey data is particularly vulnerable: only people who choose to respond shape the distribution.

> **Tip**: When you suspect a quality problem, ask: "Who collected this data, and under what conditions?" The answer often points to the failure mode.

---

## Setting Your Expectations

Data work is slow and sometimes difficult.
This should be clarifying, not discouraging:
Data scientists who are good at this work are valuable precisely because it is hard and most people underestimate it.

The skills you will build give you a foundation for every modelling task that follows: understanding attribute types, running exploratory data analysis (EDA), cleaning, encoding, and splitting data. 

> A model trained on well-understood data is more likely to produce results you can trust and defend. A model trained on poorly understood data easily becomes a liability.

Think of this as the core of the craft. The CRISP-DM cycle places Data Understanding and Data Preparation at the center for good reason.

In the following nuggets you will build the concrete vocabulary and habits that make this work systematic rather than ad hoc. Enjoy!

---

## Summary

- Data preparation typically accounts for roughly 80% of real project time.
- Real datasets arrive with missing values, sentinel values, inconsistent coding, and undocumented conventions.
- Bad data quality can produce wrong conclusions, silent model failures, deployment surprises, and sampling-biased results.
- Early cleaning decisions compound: a mistake made in data preparation shapes every downstream step.
- Mastering data work is the core competency that makes modelling results trustworthy and defensible.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [Part Index](00-index.md) | [Main Index](../index.md) | [Data Types and Measurement Scales -->](02-data-types.md)

Script v1.2 (2026-05-26) · FGN
