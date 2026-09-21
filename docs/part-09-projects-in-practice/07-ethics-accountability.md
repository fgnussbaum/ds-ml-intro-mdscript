> **Navigation:** [<-- Model Drift and Monitoring](06-model-drift-monitoring.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Troubleshooting, Pitfalls, and When to Ask for Help -->](08-troubleshooting-pitfalls.md)

---

# Ethics and Accountability in Production

**Requires**: [AI Ethics: A Primer](../part-01-the-big-picture/03-ethics-and-responsibility.md) · [From Script to Production System](04-script-to-production.md)

**Motivation**: Right at the start of this course, [🖝 AI Ethics: A Primer](../part-01-the-big-picture/03-ethics-and-responsibility.md) raised alignment, bias, and the question of who is responsible when an AI system causes harm. Let's return to these questions now that you can reason about failure modes concretely. This allows ethics to become engineering practice.

> Here you'll see what changes when ethical questions move from theory to a deployed model, how model cards make accountability a concrete habit, and how to check fairness in decisions that affect people's lives.

## Table of Contents

- [Recap:- AI Ethics Touchpoints in this Course](#recap--ai-ethics-touchpoints-in-this-course)
- [Accountability: Naming Who Is Responsible](#accountability-naming-who-is-responsible)
- [Algorithmic Bias: Fairness in High-Stakes Decisions](#algorithmic-bias-fairness-in-high-stakes-decisions)
- [Summary](#summary)

## Recap:- AI Ethics Touchpoints in this Course

Let's revisit the ethical challenges from [🖝 AI Ethics: A Primer](../part-01-the-big-picture/03-ethics-and-responsibility.md) and relate them to what we covered so far:

- The **alignment problem**: In [🖝 Choosing and Aligning Metrics](../part-06-reflection/04-aligning-metrics.md), you saw that metrics are always proxies that can drift from the goal. Models can silently drift from their intent too, as we just discussed in [🖝 Model Drift and Monitoring](../part-09-projects-in-practice/06-model-drift-monitoring.md).
- **Anthropomorphism**: Fluent, confident output invites over-trust whether or not a person is in the loop. This is why [🖝 Interface Design and Integration](../part-09-projects-in-practice/05-interface-design-integration.md) argues for keeping a human in the loop on consequential calls, rather than treating a fluent output as a decision already made.
- **Accountability**: For deployed systems, someone becomes responsible for what the system does. In deployment a bad prediction can deny a loan, miss a diagnosis, or flag the wrong person. _See [🖝 CRISP-DM Retrospective: From Coursework to Real Projects](../part-09-projects-in-practice/01-crisp-dm-retrospective.md)._
- **Algorithmic bias**: Training data reflects the inequities of the world that produced it, as the resume-screening study in [🖝 AI Ethics: A Primer](../part-01-the-big-picture/03-ethics-and-responsibility.md) showed. The Fairness section below turns that risk into something you can actually check for a given model.

We'll now take an extended look at the last two bullets.

---

## Accountability: Naming Who Is Responsible

**Accountability** is satisfied when a specific person or role, not "the team" and not the model itself, owns the consequences of what a deployed system does: who monitors it, who can pull it back, and who is responsible when it causes harm. That role has to exist before deployment, and it has to be visible to the people the system affects.

A **model card**, see [(Mitchell et al., 2019)](../references.md#mitchell2019), is a tool that makes accountability concrete and durable. It is a short, standard record that travels with a deployed model and states plainly for what the models is, and for what it is _not_. Model cards typically cover:

- **Ownership**: the named person or role accountable for the model, who monitors it, who can pause or roll it back, and who to escalate to when it "misbehaves".
- **Intended use** and, in the same breath, out-of-scope uses the model must not be put to.
- **Training data**: what it was, when it was collected, and its known gaps or biases.
- **Performance**, reported not just overall but broken down across relevant subgroups.
- **Limitations and failure modes**: where it is known to be unreliable.

This is the deployment-scale version of a habit you already practiced. The decision log from [🖝 Working as a Team on a DS Project](../part-02-ds-projects/03-team-project-basics.md) recorded *why* each choice was made, not just what. A model card does the same for a system that outlives its authors, and it directly answers the accountability gap raised in the opening ethics nugget: when no one has written down who is responsible and what the model is for, "who is accountable?" has no answer, and that vacuum is itself a risk.

A model card also happens to be the practical answer to the EU AI Act's documentation and transparency obligations for high-risk systems, see [🖝 AI Ethics: A Primer](../part-01-the-big-picture/03-ethics-and-responsibility.md).

> **Note:** Writing the card is also a test. THe models is most likely not ready to deploy if you cannot state the intended use, performance for relevant subgroups, and failure modes.

In this course we discussed mostly classic/traditionell data-science models. Beyond, **agentic AI** systems become increasingly prevalent. They take multi-step actions rather than only producing predictions. This clearly poses accountability challenges.

> **Discussion:** Accountability with agentic AI: When an agent sends an email, executes a trade, or edits code on its own, who is accountable? A split between the deployer of the agentic system (who is responsible for inherent safety mechanisms), and the user who issued the instruction (prompt) may make sense. How to resolve this cleanly?

From the perspective of when something goes wrong, it is always the same principle: A named person/role must answer for what the system does, however autonomous the system is.

---

## Algorithmic Bias: Fairness in High-Stakes Decisions

A model can have excellent overall accuracy while being systematically worse for one group. This entails unfairness that is a critical ethical failure. [🖝 Choosing and Aligning Metrics](../part-06-reflection/04-aligning-metrics.md) showed that an aggregate metric can hide errors concentrated in "minorities": just the dynamic behind the resume-screening study in [🖝 AI Ethics: A Primer](../part-01-the-big-picture/03-ethics-and-responsibility.md).

Here are two principles for checking fairness:

- **Ensuring protected attributes**: Protected attributes are characteristics that decisions should not unjustly depend on: for example, gender, ethnicity, age, or disability.
- **Checking disparate impact**: For fairness, outcomes should not differ across groups defined by a protected attribute. Even if there is no intent to "discriminate", the model might pick up discriminating patterns from historical data.

Viable practical defenses include:

- measure performance *per subgroup*, not just in aggregate, and report it on the model card.
- Consider to withheld protected features from models so they may not discriminate on them.
- Where decisions affect people, add **fairness-aware metrics** introduced in [🖝 Choosing and Aligning Metrics](../part-06-reflection/04-aligning-metrics.md) as extra dimensions alongside the primary metric.
- Keep a human in the loop for consequential calls, as argued in [🖝 Interface Design and Integration](../part-09-projects-in-practice/05-interface-design-integration.md).

Fairness definitions can conflict with each other. Therefore, as a professional, you need to pay attention, being aware of your responsibility. Document/raise findings rather than shippiong disparities in silence.

> **Discussion:** A model is more accurate overall when it uses a feature that turns out to be a close proxy for a protected attribute. Removing the feature lowers accuracy for everyone but shrinks the gap between groups. Who should decide that trade-off? Data scientiests, affected people, which other stakeholders? On what grounds?

---

## Summary

- Accountability means a named person or role owns a system's consequences.
- A model card records ownership alongside intended and out-of-scope use, training data and its gaps, performance of relevant subgroup, and limitations.
- For Fairness considerations, know which attributes should be protected.
- Measure performance of relevant subgroup (disparate impact), use fairness-aware metrics, and know when decisions demand to keep humans in the loop.
- Fairness has no single formula and definitions can conflict. Keep a sharp eye for fairness aspects. When you discover potential issues, raise them and work together with stakeholders to address them.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Model Drift and Monitoring](06-model-drift-monitoring.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Troubleshooting, Pitfalls, and When to Ask for Help -->](08-troubleshooting-pitfalls.md)

Script v1.8.2 (2026-09-21) · FGN
