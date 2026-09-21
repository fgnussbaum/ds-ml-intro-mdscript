> **Navigation:** [<-- Stakeholder Communication](03-stakeholder-communication.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Interface Design and Integration -->](05-interface-design-integration.md)

---

# From Script to Production System

**Requires**: [CRISP-DM Retrospective: From Coursework to Real Projects](01-crisp-dm-retrospective.md) · [Academia vs. Business Data Science](../part-01-the-big-picture/05-academia-vs-business-ds.md)

**Motivation**: In [🖝 Academia vs. Business Data Science](../part-01-the-big-picture/05-academia-vs-business-ds.md) we said business data science is judged by the value it delivers. This usually means the model has to run somewhere other than your laptop, on live data. This no longer works via one-off scripts or Jupyter-like notebooks, which are fine for learning and exploration. What does the shift to production actually require?

> This nugget maps why notebook code is not product code, how data flows through a running system, and two basic patterns for calling a model once it is deployed.

## Table of Contents

- [The Notebook Is Not the Product](#the-notebook-is-not-the-product)
- [Data Infrastructure: Databases, Pipelines, APIs](#data-infrastructure-databases-pipelines-apis)
- [Model Serving: Calling Models in a Running System](#model-serving-calling-models-in-a-running-system)
- [Summary](#summary)

## The Notebook Is Not the Product

A notebook is a workbench:

- cells are ordered by the story of your exploration and you run them manually,
- program state accumulates invisibly (state = values of variables etc.),
- "it worked" means it worked once, just now, on the given data.

All these are features for discovery and a liability for production.
Production code has different obligations:

| Notebook | Production system |
|---|---|
| Run manually, top to bottom | Runs on a schedule or a trigger, unattended |
| Hidden, accumulated state | Reproducible from a clean start |
| You fix it live | Must handle bad input and errors |
| Fixed datasets (often just one) | New, unseen data continuously |
| "It ran" | Tested, versioned, monitored |

The gap is not about better algorithms: the model can be identical. It is about everything around the model - the "harness". Google's fourth [🔗 rule of machine learning](https://developers.google.com/machine-learning/guides/rules-of-ml) captures it:

> **Best practice:** Keep the first model simple and get the infrastructure right. A simple model on solid infrastructure beats a sophisticated one that only runs in your notebook.

Speaking of best practices, in [🖝 Data Preparation Best Practices](../part-04-data-preparation/06-prep-principles.md) you were urged to wrap preparation steps in a pipeline so they apply identically every time. Such pipelines are the seed of production code: They make preprocessing reproducible and portable.

Moving to production is mostly software engineering, not machine learning. This is why real projects need engineers alongside data scientists. _See [🖝 Working as a Team on a DS Project](../part-02-ds-projects/03-team-project-basics.md)_.

---

## Data Infrastructure: Databases, Pipelines, APIs

In a notebook, data typically is a CSV you load once. In production, data has to arrive, be shaped, and reach the model continuously. Three pieces recur:

- **Databases** store the data the system reads from and writes to, rather than files scattered on a disk.
- **Pipelines** move and transform data on a schedule or in response to events: pulling new records, cleaning them, computing features. This is your data-preparation code, promoted to run on its own.
- **APIs** are the interfaces through which systems exchange data, letting your system pull from a sensor feed or an external service and expose results to others.

The non-negotiable requirement tying these together: **data reaching the deployed model must be prepared exactly as the training data was**. If training standardized a feature using the training mean, production must apply that *same* stored mean, not recompute it from today's batch. Doing otherwise is a production form of preprocessing leakage that we discussed in [🖝 Data Splits](../part-04-data-preparation/04-data-splits.md). It can silently degrade predictions.

<!-- Figure: simple data-flow diagram, source (sensor/DB) to pipeline (clean + feature transform using stored parameters) to model to output store/consumer -->

---

## Model Serving: Calling Models in a Running System

Once the model and its pipeline are packaged, something has to *call* them on new data. This is **model serving**. It comes in two patterns:

- **Batch serving.** The model scores a whole set of records on a schedule. For example, score the day's transactions _every night_ and write the results to a database for people to read in the morning. Simple, efficient, and enough for many problems where an answer within hours is fine.

- **Real-time serving.** The model answers requests on demand, usually behind a **REST API**, which allows to post requests, which a server processes and returns a response.

For real-time serving, another system (client) sends all necessary input data in a request to a specific server **endpoint**. The server behind the API processes the request and returns a result in the response (e.g., the prediction). The shape of such an API call that reaches a `/predict` endpoint could look like:

```python
# A client sends features; the service returns a prediction.
POST /predict   {"temperature": 82.4, "pressure": 1.7}
# response:      {"fault_risk": 0.91}
```

Real-time-serving is best when decisions are needed fast, such as approving a transaction while the customer is at the checkout. However, it buys responsiveness at the cost of complexity: the service must stay available and respond fast enough. If a model's prediction takes longer than the client caller can wait, even an accurate model is unusable, compare [🖝 Choosing and Aligning Metrics](../part-06-reflection/04-aligning-metrics.md). Choose the simpler batch pattern unless the use case genuinely demands real time.

> **Discussion:** A more accurate model takes 800 milliseconds per prediction, and a simpler one only takes 20. The decision must be made in under 100 milliseconds. The simpler model is "worse" by every metric on your evaluation report. Which do you deploy, and what does that say about where a model's quality is actually decided?

---

## Summary

- Notebooks are for exploration - production code must run unattended, reproducibly, and handle unseen data and errors on its own.
- Production data often arrives as a continuous flow through databases, pipelines, and APIs.
- The deployed model must receive data prepared with the *same stored parameters* and transformations as have been used during model training. This is to prevent pre-processing leakage and model degradation.
- Model serving is either batch (scheduled scoring, simple, good enough for most cases) or real-time (a REST API answering on demand, needed when decisions cannot wait but costlier to run within a latency budget).
- Get the infrastructure / deployment pipeline right early.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [<-- Stakeholder Communication](03-stakeholder-communication.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Interface Design and Integration -->](05-interface-design-integration.md)

Script v1.8.2 (2026-09-21) · FGN
