> **Navigation:** [<-- What Is Artificial Intelligence?](02-intro-ai.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [CRISP-DM -->](04-crisp-dm.md)

---

# AI Ethics: A Primer

**Requires**: [What Is Artificial Intelligence?](02-intro-ai.md)

Building AI systems well includes building them *responsibly*. A model can score well on every benchmark and still cause harm in deployment. **We don't want that.** So, what does it mean to build AI responsibly? And what does society, and increasingly the law, expect from those who do?

> In this nugget you will encounter three challenges that run through all of AI practice: misaligned objectives, anthropomorphism, and algorithmic bias. You will also get a first look at the EU AI Act — the world's first comprehensive AI regulation — and what its risk classification means for the systems you build.

## Table of Contents

- [The Stakes: AI Systems Act on the World](#the-stakes-ai-systems-act-on-the-world)
- [Key Challenges](#key-challenges)
- [The Regulatory Landscape](#the-regulatory-landscape)
- [Summary](#summary)

## The Stakes: AI Systems Act on the World

A sorting algorithm with a bug produces slightly out-of-order data. An AI triage system with a bug sends the wrong patient to the back of the queue. The system may pass every test and yet produce real harm.

> **Discussion**: What could be wrong when all tests pass and systems still cause unintended harm once deployed?

The asymmetry discussed here is not new to software engineering. But AI systems introduce it at scale and in contexts that are difficult to supervise manually: hiring, lending, medical diagnosis, content moderation, criminal sentencing. They often do so without explanations a human could audit.

> Building a system that acts on the world on behalf of a stated goal is **not** a neutral act.

In the sequel, we'll identify three places where things go wrong and closes with how the law is beginning to respond.

---

## Key Challenges

### Value Alignment

Every machine learning model optimizes for something: a loss function, a metric, a score. The alignment problem is the gap between *what we wrote down and how it is interpreted* and *what we actually care about*.

- A sensor system optimized to minimize false alarms may learn to suppress all alerts.
- A production system optimized to maximize yield may quietly ignore safety thresholds.

In both cases, the model did exactly what it was told. The problem is that what it was told was not quite what was wanted. The examples given here are not edge cases. In fact, the danger for misalignment is a systematic side effect of optimization:

> Whenever you define a **proxy metric** (surrogate to measure the actual goal), you create an opportunity for the model to satisfy the proxy while failing the goal.

This is why great care must be taken as to _what_ gets optimized. We humans sometimes have trouble enough to align our values. With AI models running increasingly many processes, it does not get easier. The higher the stakes of the application, the more costly are failures.

### Anthropomorphism (Projecting Human Characteristics into AI)

In 1966, Joseph Weizenbaum created ELIZA: a chatbot that reflected users' words back at them using simple pattern matching. Weizenbaum was disturbed by how quickly users formed emotional attachments to it and began treating its outputs as meaningful advice. ELIZA had no understanding of anything.

The same dynamic is present today with large language models. Fluent, confident prose triggers a cognitive shortcut: we assume competence behind the language. But a language model has no model of truth and no stake in the outcome. It produces text that fits the statistical patterns of its training data. Sometimes that text is accurate. Sometimes it is not. The model cannot tell the difference.

For practitioners, this has a concrete implication: testing whether output "sounds right" is not the same as testing whether it *is* right. Users will over-trust outputs. Developers are not immune. 

> Anthropomorphism is just one category of human biases. We have many more when interacting with AI systems. I listed some of them here: [✪ Biases when working with chatbots](https://fgnussbaum.com/ai-digital/collaborating-with-chatbots/).

Our human biases do not only affect our work with chatbots, large language models, or in fact any AI model. Some of these biases also translate into biases in AI models themselves.

### Algorithmic Bias and Accountability

Machine learning models learn from historical data, and historical data reflects the world that generated it, including its inequities. A hiring model trained on historical promotion decisions accurately reflects past patterns. But those patterns may encode discrimination, and the model will perpetuate it at scale. TODO: anecdotes.

The **accountability** question compounds this: when an AI system causes harm, who is responsible? The developer? The organization that deployed it? The regulator? Today these questions are rarely answered cleanly, and the absence of clear accountability is itself a risk: It creates incentives to deploy without sufficient scrutiny. Dangerous indeed, especially when particular, monopolistic interests dominate.

> **Discussion:** A flawed hiring tool incorrectly screens out qualified candidates for years before the problem is discovered. Who bears responsibility: the developer who built the model, the organization that deployed it, or the regulator that allowed it?

---

## The Regulatory Landscape

The [🔗 **EU AI Act**](https://artificialintelligenceact.eu/) (entered into force August 2024) is the world's first comprehensive legal framework for AI. Its core idea is a **risk-based classification**: the obligations placed on a system scale with the harm it could cause.

| Risk tier | Examples | Obligations |
|-----------|----------|-------------|
| **Unacceptable** (prohibited) | Social scoring by governments, real-time biometric surveillance in public spaces, subliminal manipulation | Banned outright |
| **High risk** | Hiring tools, credit scoring, medical devices, critical infrastructure, law enforcement, education systems | Conformity assessment, human oversight, transparency to affected persons, registration |
| **Limited risk** | Chatbots, deepfake generators | Must disclose that users are interacting with AI |
| **Minimal risk** | Spam filters, recommendation engines for non-consequential use | No specific obligations |

The AI act is sometimes criticized, naturally for any kind of regulation. The AI act is certainly not perfect. But take a look at this list: It directly reflects and protects some of the liberal values that the EU is based on. That's worth a lot.

For practitioners, the question is: *where does your system sit?*
- A quality-control model on a production line may be minimal risk in one context and high risk in another depending on what it controls.
- A hiring screening tool is high risk regardless of how accurate it is.

Additionally, certain transparency obligations apply broadly across risk tiers:
- any AI system interacting with a human must identify itself as AI, and
- AI-generated content that could deceive ("deep fakes") must be labeled as such.

The EU AI Act is a living regulation with phased implementation timelines. What matters for now is the underlying logic: risk scales with consequence, and consequence creates obligation.

We return to these questions in [🖝 Ethics and Accountability in Production](../part-09-projects-in-practice/08-ethics-accountability.md) once you have the technical vocabulary to reason about failure modes and model documentation concretely.

---

## Summary

- Deployed AI systems act on the world at scale in contexts that are difficult to audit manually. Good benchmark performance does not guarantee responsible deployment.
- The alignment problem: proxy metrics create structural opportunities for a model to satisfy the measure while failing the actual goal.
- Anthropomorphism: Leads users to over-trust fluent outputs. Fluency is not accuracy.
- Algorithmic bias in AI: models reflect their training data, including its inequities. Accountability for resulting harm remains poorly defined in both law and practice.
- The EU AI Act classifies systems by risk tier. High-risk systems face substantial design, documentation, and oversight obligations.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- What Is Artificial Intelligence?](02-intro-ai.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [CRISP-DM -->](04-crisp-dm.md)

Script v1.3 (2026-06-09) · FGN
