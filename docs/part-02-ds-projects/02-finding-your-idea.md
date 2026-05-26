> **Navigation:** [<-- Why a Project?](01-why-a-project.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Working as a Team on a DS Project -->](03-team-project-basics.md)

---

# Finding Your Idea

**Requires**: [Why a Project?](01-why-a-project.md)

**Motivation**: You know why a project is worth doing. The harder question can sometimes be: What should it be? Worry not; you probably have more potential ideas than you realize.

> This nugget gives you a set of prompts to surface candidate problems from your own background, a template to sharpen each one into a concrete, workable question, and a short list of examples to calibrate what a completed project looks like.

## Table of Contents

- [Where to Look for Problems](#where-to-look-for-problems)
- [From Problem to a Workable Question](#from-problem-to-a-workable-question)
- [Committing to One Idea as a Group](#committing-to-one-idea-as-a-group)
- [Summary](#summary)

## Where to Look for Problems

Good ideas rarely arrive fully formed. They start as a vague sense that something could be better understood, made faster, or done more reliably.

> The place to start is not "What could a model do?" but "Where does something feel difficult or uncertain?"

Here are three entry points. For each one, ask yourself the accompanying questions and write down anything that seems plausible. **Do not filter yet.**

> Write down 2-3 problem candidates before moving on. Do not evaluate them yet.

### Solve a problem for yourself
- What do you do repeatedly in your work that is slow, error-prone, or relies on judgment you cannot easily articulate?
- Is there a quantity you estimate by hand? A decision you make from experience, but would struggle to write down as rules?

*Who benefits?* You do — and people in similar roles.

### Help someone else or the community
Someone else's workflow problem often makes an excellent project because the question is already real: someone cares about the answer.

- Ask a colleague, friend, or family member what they spend time on that feels repetitive or uncertain.

*Who benefits?* Name them specifically. If you cannot, the problem may not be concrete enough yet.

### Follow a curiosity
Look at data you already have — calibration records, measurement logs, sensor archives, a spreadsheet you have kept for years — and ask: What structure might be here that is worth examining systematically?

*Who benefits?* Anyone who uses or depends on that data.

### A few example ideas

Here are some exemplary, still vague problem statements as may be typical when the idea first surfaces. Though the following examples are mostly engineering-specific, you are WELCOME to figure out anything that you are interested in yourself.

- "The spectra look different depending on material, but we have never examined why."
- "Our sensor seems to degrade, but we have no systematic way to tell when it is about to fail."
- "Yield varies batch to batch and nobody is sure what drives it."

---

## From Problem to a Workable Question

Once you have candidate problems, the next step is to check how they can be framed as a data science question. The framing matters because it determines what "done" looks like and which tools apply.

### Step 1: Recognize What Kind of Question It Is

Scan the first column below (ignore the last column, it's just for look-up later). Which business question sounds like yours?

| Business question | Verb | Core methods |
|--------|---|---|
| How much or how many? | **estimate** | Regression |
| Which category does this belong to? | **classify** | Classification |
| What will happen over time? | **forecast** | Time series |
| Who or what is similar? | **group** | Clustering |
| What is unusual or wrong? | **detect** | Anomaly detection |
| What should I show or suggest? | **recommend** | Recommender systems |
| What is most relevant or risky? | **rank** | Learning to rank, scoring |
| What drives this outcome? | **explain** | Causal inference, interpretability |
| What is the underlying structure? | **reduce** | Dimensionality reduction, embeddings |

If a row resonates, note the verb and use it in the next step. Try to find the best fit. Everything can be refined later.

### Step 2: Frame It as a Sentence

Complete the sentence: **"I want to [VERB] [WHAT] from [DATA]."**

- **WHAT** is what you want to know, produce, or uncover (derived from your problem statement).
- **DATA** is the data you have or could collect.

Here are the three example ideas from the previous section with the template applied:

| Vague problem | Translated question | Type |
|---|---|---|
| "The spectra look different depending on material, but we have never examined why." | "I want to **group** unlabelled spectra into material categories from their measured features." | Group |
| "Our sensor seems to degrade, but we have no systematic way to tell when it is about to fail." | "I want to **detect** imminent failures in a sensor component from its usage patterns." | Detect |
| "Yield varies batch to batch and nobody is sure what drives it." | "I want to **estimate** batch yield from process temperature and pressure logs." | Estimate |

If you can fill in WHAT and DATA with concrete things (like the bold pieces in the table), you have a workable question. If you cannot, the problem needs more specificity, not more ambition.

The framing template provided here is a translation tool. It may not be perfect for all ideas you have. In doubt: adjust wording slightly. Carry two or three sharpened questions into the next section.

<!--This nugget here is really mostly for generating ideas.-->

---

## Committing to One Idea as a Group

Each team member now has two or three sharpened candidate questions. The next task is to select one.

This is a coordination problem, not a technical one. The goal is to find a question the whole group can invest in, where accessible data already exists, and where the framing is concrete enough to get started.

A workable selection process:

1. Each person presents their candidates using the sentence template. One sentence per idea, plus who benefits.
2. After everyone has presented, mark the ideas that already have a known data source behind them. Ideas without a clear data source are harder to move forward at this stage.
3. Discuss genuine interest and feasibility. You are looking for overlap: a question that at least two people find interesting and where the group believes data is accessible.
4. When there is no clear winner, choose the idea with the most concrete data source, not the most ambitious question.

Once your group commits to a question, it is the group's question, regardless of who proposed it.

> You will not know for certain whether the idea is feasible at this point. That is fine: [🖝 Reality-Checking Your Idea](../part-02-ds-projects/04-reality-checking-your-idea.md) is exactly for that. Commit now, verify next.

---

## Summary

- Start with the problem, not the solution: ask where something is difficult or uncertain before asking what a model could do.
- Three reliable sources: your own workflow, problems you observe in others, and data you already have.
- Write several candidates before filtering; name who benefits for each.
- Scan the problem-type table by business question to recognize which kind of question yours is, then frame it as "I want to [VERB] [WHAT] from [DATA]."
- For group selection: mark ideas with known data sources, look for shared interest, and when in doubt pick the most concrete option over the most ambitious one.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Why a Project?](01-why-a-project.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Working as a Team on a DS Project -->](03-team-project-basics.md)

Script v1.2 (2026-05-26) · FGN
