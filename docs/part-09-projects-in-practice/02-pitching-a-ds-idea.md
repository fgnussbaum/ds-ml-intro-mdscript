> **Navigation:** [<-- CRISP-DM Retrospective: From Coursework to Real Projects](01-crisp-dm-retrospective.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Stakeholder Communication -->](03-stakeholder-communication.md)

---

# Pitching a Data-Science Idea

**Requires**: [CRISP-DM Retrospective: From Coursework to Real Projects](01-crisp-dm-retrospective.md) · [Reality-Checking Your Idea](../part-02-ds-projects/04-reality-checking-your-idea.md)

**Motivation**: Back in part II, we reality-checked ideas quickly and roughly to decide what was worth pursuing. In organizational contexts, a single personal conviction is not enough: someone controls the budget, the data access, and the time of people. So you need to get commitments. How do you turn a promising idea into something decision-makers will actually fund?

> This nugget covers the "Pitch act". It involves presenting arguments in some structured way. Many organizations and settings use a "business case" for this. That's way in this nugget, you'll find a simple four-part structure for building one, alongside tips for presenting it.

## Table of Contents

- [Why the Pitch and Business Cases Exists](#why-the-pitch-and-business-cases-exists)
- [Structure of a Business Case](#structure-of-a-business-case)
- [Pitching for Support: Audience Awareness and Common Objections](#pitching-for-support-audience-awareness-and-common-objections)
- [Summary](#summary)

## Why the Pitch and Business Cases Exists

A large majority of data-science projects never make it into production, often not due to model failures, but because the work was disconnected from real needs [(Nussbaum, 2025)](../references.md#nussbaum2025planpitch). A formal pitch like a **business case** guards against this type of disconnection. It forces you to state what problem you are solving, what it is worth, and what you need. Therefore, the pitch/business case acts as a filter whether an idea is ready (yet).

This is the same as in [🖝 Reality-Checking Your Idea](../part-02-ds-projects/04-reality-checking-your-idea.md), just scaled up.
The question is no just whether something is doable, but whether it is worth committing potentially significant resources to it. This requires a solid business understanding and value estimates that are certain enough, realistic, and promising [(Nussbaum, 2025)](../references.md#nussbaum2025planpitch).

---

## Structure of a Business Case

Depending on the organization or setting, a business case or pitch can take different forms. Some organizations have their own templates for business cases. The goal is always the same: convince people who control resources to "buy in". For this purpose, a business case usually answers four questions:

| Part | Question it answers |
|---|---|
| **Problem** | What issue are we solving, for whom, and why does it matter now? |
| **Value** | What is the expected benefit, in numbers, minus the expected cost? |
| **Feasibility** | Can we actually build it with the data, skills, and time available? |
| **Ask** | What exactly do you need approved/granted (e.g., budget, people, data access)? |

- **Problem** as you practiced in [🖝 Finding Your Idea](../part-02-ds-projects/02-finding-your-idea.md): a concrete question stated in one sentence, tied to a real pain point.
- **Value** is the part coursework rarely touches. You might estimate the gain per prediction (labor saved, revenue gained, errors avoided) times the number of predictions, then subtract development and running costs. You already have half the machinery: in [🖝 Choosing and Aligning Metrics](../part-06-reflection/04-aligning-metrics.md) you saw how false-positive and false-negative costs translate a metric into money. A pitch adds the value side of that ledger. **Keep the model simple and the assumptions explicit**: a calculation stakeholders can follow beats a precise one they cannot. <!-- Source: statistic on share of data-science projects that never reach production, and on share of enterprises reporting financial return from AI, both cited in Nussbaum (2025) -->
- **Feasibility** draws on the reality check plus any small experiment you ran, like small baseline models. Backed estimates are worth more than non-substantial promises.
- **Ask** is where technical pitches are often weak: They explain the solution in loving detail and forget to state plainly what decision they want.

There are many more frameworks for building a argument surrounding these narrative beats, like the 3-minute pitch. You'll find plenty of resources when you want to prepare a presentation for a pitch.

---

## Pitching for Support: Audience Awareness and Common Objections

Whereas a business case is just a document, an actual pitch is a performance. Its first rule is to know who is listening: The people granting resources usually do not have technical training. Therefore, how technical aspects get communicated deserves deliberate attention.

A key technique is to lead with an **emotional hook**. This is a well-chosen story or a single vivid example of the problem. It is supposed to address the audience emotionally, which lands better than a table of figures outright. You need to earn attention first before you can present numbers.

> The business case is your factual foundation. Storytelling is what gets people to engage with it.

In the next nugget [🖝 Stakeholder Communication](../part-09-projects-in-practice/03-stakeholder-communication.md), we'll explore a few additional communication best practices [(Nussbaum, 2023)](../references.md#nussbaum2023communication): lead with the core message, provide context first, and translate findings into concrete actions.

Especially for a pitch, it is helpful to anticipate objections so you can preempt them or deal with them when raised. For example, stakeholders may expect the system to be flawless, or question some of your assumptions. Begin able to address objections helps defusing them and builds credibility [(Nussbaum, 2023)](../references.md#nussbaum2023aimyths).

> **Tip:** Invite a supportive stakeholder into the pitch. When someone other than you vouches for the idea, approval gets easier.

> **Discussion:** You have two ways to present the same project: (1) a precise, caveated value estimate, or (2) a simplified one built on stated assumptions that hide some uncertainty. Which serves the pitch and decision outcome better, and to which degree does it depend on who is in the room?

---

## Summary

- A business case exists to justify committing real resources and to align stakeholders before large investments. Writing it honestly is also a filter on the idea.
- A good default four-part structure: problem (the concrete question), value (benefit minus cost), feasibility (evidence you can build it), and ask (the specific decision you need).
- The value estimate reuses the cost thinking from metric alignment and adds the benefit side. Keep it simple and explicit.
- Pitching is audience-first: lead with the core message, use an emotional hook to earn attention. Pre-empt objections.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- CRISP-DM Retrospective: From Coursework to Real Projects](01-crisp-dm-retrospective.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Stakeholder Communication -->](03-stakeholder-communication.md)

Script v1.8.2 (2026-09-21) · FGN
