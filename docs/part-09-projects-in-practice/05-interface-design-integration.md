> **Navigation:** [<-- From Script to Production System](04-script-to-production.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Model Drift and Monitoring -->](06-model-drift-monitoring.md)

---

# Interface Design and Integration

**Requires**: [From Script to Production System](04-script-to-production.md)

**Motivation**: In the API example from [🖝 From Script to Production System](../part-09-projects-in-practice/04-script-to-production.md), the deployed model returns `{"fault_risk": 0.91}`. While this number is informative, it does not represent a decision. Prediction often need to be made actionable first: Think of the maintenance technician who has to decide whether to stop the line based on the predicted fault risk. So it depends: Who is on the receiving end, and what do they need?

> This nugget covers the interface and integration phase: identifying who consumes the output, turning raw predictions into actionable displays for people, and embedding the model into larger workflows for systems.

## Table of Contents

- [Output Consumer Types: End Users, Downstream Systems](#output-consumer-types-end-users-downstream-systems)
- [For End Users: UI and Decision-Support Tools](#for-end-users-ui-and-decision-support-tools)
- [System Integration: Embedding Models in Workflows](#system-integration-embedding-models-in-workflows)
- [Summary](#summary)

## Output Consumer Types: End Users, Downstream Systems

Design depends on who receives the model's output. Let's differentiate between two types of consumers:

- **End users** are people (technicians, doctors, etc.). They need output framed as a decision, with enough context to trust and act on it.
- **Downstream systems** are other software (billing systems, dashboard backends, any kind of service). They need a structured, predictable value that conforms to an agreed contract, and nothing more.

Continuing our example, the same fault-risk score serves both, but needs to "dress up" differently:

- To the maintenance system it is a number that trips an alert above a threshold.
- To the technician it is "high risk: inspect bearing 3 before next shift".

The distinction between consumers is why in our version of the [🖝 CRISP-DM](../part-01-the-big-picture/04-crisp-dm.md) map, (user) interface design and integration is promoted as its own concern. A model that works but is never wired into how people or systems actually operate delivers no value. Getting the consumer wrong is expensive.

In the following two sections, we focus on each of the two consumer types.

---

## For End Users: UI and Decision-Support Tools

Human consumers want to close potential gaps between predictions and actions that need to be derived. The communication principle that findings must be translated into concrete, actionable steps applies directly at the interface [(Nussbaum, 2023)](../references.md#nussbaum2023communication).
All of the following can contribute to making predictions actionable:

- **Turn predicted scores into actual recommendations.** Apply a "tuned" decision threshold and present the resulting action. Showing the raw numbers is an optional addition for those who want it.
- **Give the "why".** Attach the explanation, a top feature or a short reason from [🖝 Explainability](../part-06-reflection/05-explainability.md), so the user can sanity-check the output against their own judgment.
- **Show confidence and its limits.** A prediction offered with no sense of certainty invites either blind trust or blanket dismissal.

UI is not just about actionable insights, but also about seamless integration into workflows, so:

> **Fit the existing workflow.** The best interface adds a signal where people already look. This means avoiding new tools (or integrating into existing ones).

It also all depends on the deeper design choice whether the system should **decide itself** or only **support a decision**. Many data-science systems are decision-support tools that keep a human in the loop. Sometimes this is safer - and it helps to clarify accountability for AI-aided decisions: The higher the stakes, the stronger the case for keeping a person in control of the final call.

---

## System Integration: Embedding Models in Workflows

For system consumers, the model is one component inside a larger process. Integration is about making it "well-behaved": THis is usually achieved through the same API pattern you saw for real-time serving in [🖝 From Script to Production System](../part-09-projects-in-practice/04-script-to-production.md): The application that wraps the model queries the model with features and receives a prediction as a step within its own logic.

What matters for this:

- **A stable interface contract.** Connected systems depend on an exact and consistent shape of inputs and outputs. Especially when iterating throughout a development project, careless changes to an interface can break things downstream.
- **Graceful failure.** The model service might sometimes be slow or unavailable. It is best practice to develop the surrounding workflow with adequate fallbacks. This could be a default action, but certainly not crashing the whole process.

These requirements require development discipline. It is a mindset shift from "my model" to "one part of a system that has to keep working". This is squarely software engineering, and it is where the engineers on a project team earn their place. Your responsibility as the data scientist is to make the model's behavior, its inputs, outputs, and failure modes, predictable enough to integrate.

> **Discussion:** A decision-support tool shows a recommendation *and* the reason behind it. Over months, users stop reading the reason and just click "accept". Has the interface succeeded because it is trusted, or failed because it has quietly become an autonomous decider with a human rubber-stamp?

---

## Summary

- Identify the consumer first as the same prediction is dressed differently for each:
    - end users need output framed as a decision with context
    - downstream systems need a structured value on a stable contract.
- For people, turn scores into recommendations, show confidence, attach an explanation, and fit the existing workflow. Prefer decision-support that keeps a human in the loop over autonomous deciding, especially as stakes rise (this of course depends on a fair judgement of the model's capabilities).
- For systems, usually integrate through an API with a stable input/output contract and graceful failure- The model must be well-behaved component rather than a single point of collapse.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- From Script to Production System](04-script-to-production.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Model Drift and Monitoring -->](06-model-drift-monitoring.md)

Script v1.8.2 (2026-09-21) · FGN
