> **Navigation:** [<-- Course Orientation](01-course-orientation.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [AI Ethics: A Primer -->](03-ethics-and-responsibility.md)

---

# What Is Artificial Intelligence?

**Motivation**: You are about to spend a semester learning about data science - building data-driven solutions ("AI"). Terms like AI, data science and machine learning are often used interchangeably, though they do not mean the same. Conflating them leads to vague thinking, misunderstandings, and poor design choices. So: What exactly is AI?

> In this nugget you will learn to distinguish key concepts in the field of AI and data science, get to know a mindset for approaching data-driven solutions. You'll also get to know key milestones that shaped the field of AI.

## Table of Contents

- [Key Concepts at a Glance](#key-concepts-at-a-glance)
- [A Design Hierarchy: From Rules to AI](#a-design-hierarchy-from-rules-to-ai)
- [A Brief History of the Field of AI](#a-brief-history-of-the-field-of-ai)
- [Summary](#summary)

## Key Concepts at a Glance

In a nutshell, an AI system takes inputs, performs mathematical computations (more or less black box), and produces outputs.

<p><center><img src="../media/selfmade/ai-input-blackbox-output.jpg" alt="AI system: inputs → model → outputs" width="740px"/></center></p>

What distinguishes different systems is *how* the computations are carried out. Here's an overview of three nested key concepts:

* **Artificial Intelligence (AI)**: Any computational system exhibiting behavior associated with intelligence: recognizing patterns, making decisions, generating language
* **Machine Learning (ML)**: A subset of AI. Systems that learn behavior from training data rather than explicitly programmed rules
* **Deep Learning (DL)**: A subset of ML. Using large, layered neural-network models; capable of learning from raw data such as images or text

**Data Science** is the applied discipline that combines ML with statistics, data engineering, and domain expertise to answer real questions from data.

> There is also **generative AI (GenAI)**, which uses deep learning techniques for generating text, code, images, videos, speech, etc. GenAI is extremely present in current debates. Non-experts are often inclided to think of GenAI as all "AI". During the course you'll see why this can be a dangerous conflation of concepts.

The next section explains how to approach problems which call for data-driven solutions.

---

## A Design Hierarchy: From Rules to AI

### Simplicity First. Always.
When building a data-driven solution, the first question to ask is not "Which model should I use?". It is rather: "How simple can I make this?".

**Why?** Simple solutions are easier to explain, easier to debug, and easier to trust. A model that no one can interpret is a liability the moment something goes wrong. Therefore, start as simple as the problem allows, and only add complexity when the simpler approach breaks down.

This is such an important principle that we'll revisit it later in [🖝 Start Simple](../part-06-reflection/02-start-simple.md). Here, let's have a first look at a design hierarchy.

### Rule-Based Systems

For well-bounded problems, the "simplicity first" principle means that explicit logic is hard to beat. That's why rules should be the first thing to try: A sensor reads above a threshold? Trigger an alarm. An email matching a known spam pattern? Flag it as spam.

> **Rule-based systems** solve a problem by following explicitly programmed if-then logic. Human experts encode decision criteria. The system applies them.

### Machine Learning only when Needed

Assume you want to decide from a photograph whether a technical component is cracked. You might try a rule: "flag it if more than *N* pixels exceed gray value threshold *X*." However, this gets problematic when images are also taken from slightly different angles, under different lighting, or with a shadow across the crack. The rule set grows, conflicts multiply, and maintenance piles up.

This is a common pattern. When the problem is too large or complex for hand-crafted rules, machine learning becomes the natural next step: let the system infer the logic from labeled examples instead of writing it by hand. In the task above, training data could consist of images of cracked and intact components.

ML is still subject to the simplicity principle:

> **Rule of thumb:** Among all models that perform well enough, prefer the one that is easiest to understand. Never add complexity you cannot justify.

ML models span a wide range of complexity: from simple decision trees to deep learning networks with hundreds of millions of parameters. More complexity is not always better.

### Data Science as a full discipline

A model alone rarely solves a real problem. You need the right data, a way to collect and clean it, a way to evaluate whether the model actually works, and a way to act on its outputs. **Data science** comprises the full pipeline.

> The model is one component. The work around it is most of the job.

When you combine statistics, engineering, and domain judgment along with ML methods, you are doing data science. In practice, you'll also encounter different terms for the "holistic" work we are talking about here (especially in job descriptions). No matter how large the effort for clearly distinguishing concepts, some blurring will always remain.

In this course you will use data-science and machine learning methods as _instruments_. Understanding what they do, when to use them, and how they can fail matters most.

Now, to understand why and how these methods ermerged, here's a brief look at the field's history.

---

## A Brief History of the Field of AI

The formal beginning of AI as a discipline is usually placed at the **Dartmouth Workshop of 1956**, where a group of researchers proposed, as a working conjecture, that every aspect of intelligence could be described precisely enough for a machine to simulate it. The ambition was enormous. Near-term progress was... well, mixed.

The decades that followed alternated between optimism and setback. In the 1950s and 1960s, early programs solved algebra problems and proved theorems, and some researchers predicted human-level AI within twenty years. Those predictions were wrong. Funding dried up in what became known as _AI winters_.

What eventually turned the field around was data and compute. Larger datasets and faster processors, especially graphics processing units, allowed learning algorithms to outperform hand-crafted rules on certain practical tasks. In the 2010s, deep neural networks began achieving human-level or better performance on specific benchmarks: image recognition, speech, language translation.

Key milestones worth knowing:

| Time | Description |
|---|---|
| 1950 | Alan Turing proposes the Turing Test as an operational substitute for the question "Can a machine think?" |
| 1956 | Dartmouth Workshop coins the term "artificial intelligence." |
| 1960s–1980s | Logic-based and rule-based systems; expert systems peak, then hit limits. |
| 1986 | Backpropagation algorithm revives neural network research. |
| 1990s–2000s | Statistical machine learning (SVMs, random forests) becomes dominant in practice. |
| 2012 | Deep convolutional networks win the ImageNet challenge by a large margin; the deep learning era begins. |
| 2017–present | Transformer architectures, large language models, generative AI. |

For your work, the practical upshot is this: you are inheriting a generation of tools that have been tested on serious problems. You do not need to understand their full history to use them well, but knowing it helps you recognize why certain design choices were made and where the limits are.

---

## Summary

- AI, ML, deep learning are nested concepts, not synonyms. The table in "Key Concepts at a Glance" is the reference.
- Start as simple as the problem allows: rule-based systems are transparent and fast. Escalate to ML only when rules become unmaintainable.
- Among solutions that perform well enough, prefer the one that is easiest to interpret: Complexity must be justified.
- AI has passed through cycles of optimism and setback. Increasing availability of data and compute cause the increasing success from the 2010s onward.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Course Orientation](01-course-orientation.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [AI Ethics: A Primer -->](03-ethics-and-responsibility.md)

Script v1.5 (2026-06-24) · FGN
