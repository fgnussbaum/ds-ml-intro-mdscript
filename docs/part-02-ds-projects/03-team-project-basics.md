> **Navigation:** [<-- Finding Your Idea](02-finding-your-idea.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Reality-Checking Your Idea -->](04-reality-checking-your-idea.md)

---

# Working as a Team on a DS Project

**Requires**: [Finding Your Idea](02-finding-your-idea.md)

**Motivation**: You have a question and a group. The technical work ahead is the same whether you do the project alone or together. What changes is the coordination: who is responsible for what, how you avoid duplicating effort, and what you do when the project stalls or a decision needs to be made.

> You will see a simple way to assign responsibilities, how the CRISP-DM phases divide naturally across a small team, and a few habits that keep group projects from going quiet.

## Table of Contents

- [Roles in a Data-Science Project](#roles-in-a-data-science-project)
- [Dividing Work Across the CRISP-DM Phases](#dividing-work-across-the-crisp-dm-phases)
- [Keeping the Project Moving](#keeping-the-project-moving)
- [Summary](#summary)

## Roles in a Data-Science Project

Data science projects do not map cleanly to the formal roles you would find in a software engineering team. Think instead in terms of responsibilities that need to be covered at some point in every project.

**Domain expert.** The person who understands what the data represents. They catch when a result is physically implausible, translate the problem statement into concrete data questions, and validate whether outputs make sense. In an engineering group, this often applies to everyone — which is an advantage, not a complication.

**Technical lead.** The person who sets up the shared environment, manages the notebook or scripts, and takes point on the more demanding implementation steps. They keep the code runnable and reproducible.

**Communicator.** The person who writes up conclusions, structures the final summary, and ensures the documented decisions are coherent from start to finish. This role carries the narrative.

In a group of three or four, one person typically covers two of these. The important thing is that every responsibility is named explicitly rather than assumed.

> **Important:** Unowned responsibilities tend to not get done (properly).

---

## Dividing Work Across the CRISP-DM Phases

Not every phase produces the same amount of work, and some phases parallelize more naturally than others.

**Work together on:**

- Business understanding: the problem definition is a group decision. **Everyone needs to understand and agree on what you are trying to do**.
- Modeling: early modeling is best done together so that everyone understands the baseline before branches diverge.
- Evaluation: every team member should be able to explain the results and their limits.

**Phases that can be split:**

- Data understanding: different people can explore different columns or run different analyses, then reconvene and share findings.
- Data preparation: cleaning and feature engineering tasks are often separable once the overall strategy is agreed.
- Reporting: the communicator drafts, the others review.

> **Warning:** Splitting data work too early before there is a **shared understanding of the dataset** leads to cleaning decisions that contradict each other. Spend at least one discussion session exploring the data together before dividing the work further.

---

## Keeping the Project Moving

Group projects stall for predictable reasons:

- no one owns the next concrete step,
- sessions end without actionable decisions,
- blockers sit unaddressed because everyone assumes someone else will handle them.

Here are some habits that help to prevent such failure modes:

---

**Name actions, responsibilities.** At the end of every working session, name specific tasks along with the person who owns each of them.

- Bad: *"We will do the cleaning next time"*. This is not an action.
- Better: *"Anna checks for missing values in the temperature columns before Thursday"*.

WHO does WHAT by WHEN.

---

**Keep a shared decision log.** A simple document that records what you tried, what worked, and what you decided to stop doing. **This is not overhead**: it prevents relitigating decisions and repeating dead ends. It is also a direct input to your final documentation.

**Timebox blockers.** When someone is stuck, set a time limit before asking the group for help. Spending three hours on a bug that a teammate resolves in ten minutes is not persistence, it is a coordination failure. Agree in advance on a reasonable threshold — often 30 minutes is enough.

> **Discussion:** What makes it hard to say "I'm stuck" in a group? What would make it easier?

---

## Summary

- Assign responsibilities explicitly: domain knowledge, technical lead, communication. Unowned responsibilities tend not to get done well.
- Shared phases (business understanding, modeling, evaluation) are best done together. Data understanding and preparation can be split once the team has a common view of the dataset.
- Group projects stall when next steps are unnamed or not actionable. End every session with specific actions and their named owners. **WHO does WHAT by WHEN.**
- A shared decision log helps to prevent repeated dead ends and feeds directly into final documentation.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Finding Your Idea](02-finding-your-idea.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Reality-Checking Your Idea -->](04-reality-checking-your-idea.md)

Script v1.4 (2026-06-10) · FGN
