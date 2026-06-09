> **Navigation:** [Part Index](00-index.md) | [Main Index](../index.md) | [Preparing Non-Tabular Data -->](02-beyond-tabular-prep.md)

---

# Beyond Tabular Data

**Motivation**: Everything you have learned so far assumes the data fits in a table: one row per record, one column per attribute, no meaningful ordering among rows. But a photograph is not a row, a heartbeat trace is not a column, and a text document has no fixed schema. This nugget asks: When does the tabular assumption break down, and what changes when it does?

> You will learn to recognize the structural properties of images, video, text, time series, and spatial data, understand why each format requires tools beyond standard tabular workflows. For each type you'll see what the EDA mindset looks like when applied to the respective type of data.

## Table of Contents

- [When Tabular Isn't Enough](#when-tabular-isnt-enough)
- [Images and Video](#images-and-video)
- [Text](#text)
- [Time Series Data](#time-series-data)
- [Spatial Data](#spatial-data)
- [Summary](#summary)

## When Tabular Isn't Enough

Every technique in this course so far has assumed a specific shape for your data: a two-dimensional table where each row is one record and each column is one attribute with a fixed type and no particular ordering among rows. This structure is called **tabular data**, and it is by far the most common format in business and scientific datasets.
Nevertheless, a large share of real-world data is not tabular.
- An image is not one row in a table.
- A time series is not just a column of numbers: the ordering of those numbers carries information, and ignoring it loses most of the signal.
- A text document has no fixed schema at all.
- Geographic measurements are entangled: a soil sample near a contaminated site is not independent of the one taken five meters away.

What breaks down is not the EDA mindset. Asking about distributions, outliers, and missingness is still exactly right. What breaks down is the tooling: standard scikit-learn pipelines, one-hot encoding, and correlation matrices do not carry over without modification. Each data type imposes its own structure, and that structure determines what "distribution," "outlier," and "missingness" mean in practice.

This nugget just serves for orientation. The course focuses on tabular data: What follows is a map of the territory beyond it.

---

## Images and Video

An image is a multidimensional array of pixel values. A grayscale image of height $H$ and width $W$ has shape $(H, W)$. A color image adds a channel dimension: shape $(H, W, C)$, where $C = 3$ for RGB. Even a modest $256 \times 256$ image has $196\,608$ raw features. Flattening that into a table row and feeding it to a logistic regression is technically possible but almost never effective: pixel indices carry no spatial meaning when spatial structure is destroyed.

Video adds a time dimension: shape $(T, H, W, C)$, where $T$ is the number of frames. The temporal ordering of frames matters as much as the spatial structure within each frame.

The reason **convolutional neural networks (CNNs)** exist is precisely to exploit spatial locality: a filter that detects an edge works the same way regardless of where in the image that edge appears. You do not need to understand CNNs to work in data science, but you should know why raw-pixel tabular methods fail.

**EDA considerations:**

- **Image size distribution.** Are all images the same resolution, or is there variance? Large size differences will require a resizing decision before any model can use the data.
- **Class balance.** If labels are attached (e.g., tumor vs. healthy tissue), check whether categories are evenly represented. Imbalance is just as problematic for image classifiers as for tabular ones.
- **Visual spot-check.** Sample a few dozen images and inspect them manually. Look for corrupted files (black frames, partial loads), mislabeled samples, and near-duplicate images that could inflate accuracy metrics.
- **Pixel value distributions.** Plot histograms of pixel values per channel. Values clustered near 0 or 255 (very dark or blown-out images) can signal scanner artifacts or poor data quality.
- **For video:** Check the distribution of clip lengths and frame rates. Clips of very different durations may require truncation or padding, and mixed frame rates complicate temporal analysis.

---

## Text

Text is unstructured. A document is a variable-length sequence of tokens with no fixed schema, no numeric values, and no guaranteed size. Before any tabular method can touch it, text must be converted into a numeric representation.

The simplest approach is the **bag-of-words** model: count how often each word from a fixed vocabulary appears in a document, producing a very long, very sparse vector. This discards word order but preserves word frequency, which is often enough for classification tasks. Modern approaches use **embeddings**, which map words or entire sentences into dense vectors that capture semantic similarity — "hospital" ends up closer to "clinic" than to "bicycle." The field that specializes in text representation and understanding is **natural language processing (NLP)**.

**EDA considerations:**

- **Document length distribution.** Plot the distribution of word counts or character counts across documents. Very short documents may lack enough signal; very long documents may dominate a bag-of-words vocabulary.
- **Class balance.** For classification tasks, check whether categories are evenly represented across the corpus.
- **Token frequency.** Inspect the most and least frequent tokens. The most frequent are often stop words ("the," "and") that add noise without contributing discriminative signal; the least frequent are often rare or misspelled terms that pad the vocabulary.
- **Vocabulary growth curve.** Plot vocabulary size as a function of corpus size. A vocabulary that grows almost linearly signals many rare, one-off terms — a regime where bag-of-words models struggle and embeddings have an advantage.
- **Empty or near-empty documents.** Check for documents that are blank or contain only punctuation. These are structural missingness.
- **Language and encoding anomalies.** For web-scraped or multilingual corpora, check whether all documents are in the expected language and character encoding. Mixed encodings produce garbage tokens.

---

## Time Series Data

A time series records observations of one or more variables at successive time points: daily temperatures, hourly power consumption, weekly sales, a patient's heart rate during surgery. The defining structural property is that **order matters**. A standard tabular ML model treats rows as exchangeable — shuffle them, and nothing changes. For a time series, shuffling destroys the signal.

The dependence structure is called **autocorrelation**: observations close together in time tend to be more similar than observations far apart. Tomorrow's temperature depends on today's in a way that yesterday's temperature does not depend on tomorrow's. Ignoring this structure leads to models that look good in cross-validation but fail in production, because the standard random Data Splits is not appropriate for time-ordered data.

Specialized tools include classical methods such as ARIMA and its variants, and neural approaches such as recurrent networks (RNNs, LSTMs) and sequence transformers.

**EDA considerations:**

- **Plot the full series.** A time plot — values against time — is the first and most important step. Look for trend (long-term direction), seasonality (repeating cycles), and structural breaks (sudden shifts in level or variance).
- **Missing timestamps and irregular sampling.** Check whether the series has gaps or whether the sampling interval is irregular. Both have direct implications for which models are applicable and how windows should be constructed.
- **Autocorrelation function (ACF).** Plot autocorrelation at successive lags to understand how far back in time a value is correlated with its own past. This directly informs window size choices in downstream preparation.
- **Outliers in temporal context.** A value that looks unremarkable globally may be a clear anomaly relative to its immediate neighbors. Examine potential outliers alongside their temporal neighborhood, not just against the global distribution.
- **Stationarity.** A stationary series has roughly constant mean and variance over time. A trending or variance-shifting series is non-stationary and requires different modeling assumptions. A simple time plot often reveals this immediately.
- **For panel data (multiple series).** If you have many related series (e.g., sales across many products), check whether patterns are consistent across series or whether some series are structurally anomalous.

---

## Spatial Data

Spatial data comes from measurements tied to geographic coordinates: soil samples, sensor readings across a city grid, satellite imagery bands, census block estimates. The structural property that distinguishes it from tabular data is **spatial autocorrelation**: nearby locations tend to have more similar values than distant ones. This is Tobler's first law of geography: "everything is related to everything else, but near things are more related than distant things."

A model that ignores this structure will underestimate uncertainty and produce misleading confidence intervals. A random Data Splits risks placing spatially correlated observations on both sides of the split boundary, making evaluation look better than it is.

Spatial analysis uses tools from **geographic information systems (GIS)**, geostatistics (kriging, spatial regression), and increasingly deep learning on graph-structured data.

**EDA considerations:**

- **Map the sample locations.** Plot measurement locations on a map before anything else. Look for clustering (data concentrated in a few areas), coverage gaps (unsampled regions), and whether coverage matches the intended study area.
- **Spatial distribution of the outcome.** Map the target variable. Visual hotspots — high-value clusters or sharp spatial boundaries — indicate structure the model must account for.
- **Spatial autocorrelation diagnostics.** Compute Moran's I or plot a variogram to quantify how quickly spatial similarity decays with distance. This guides the choice between a simple non-spatial model and a geostatistical one.
- **Missing spatial regions.** Gaps in coverage mean the model will extrapolate to locations unlike anything in the training data. Flag these before reporting results.
- **Coordinate reference systems.** Check that all data uses a consistent coordinate system and projection. Mixing coordinate systems (degrees vs. meters, or different datums) produces incorrect distances and areas.

*See also: [🖝 Preparing Non-Tabular Data](../part-zz-appendix/02-beyond-tabular-prep.md) for how each of these data types is converted into a feature matrix and what the fit-on-train rule looks like in practice.*

---

## Summary

- Tabular data assumes a fixed schema, one row per record, and no meaningful ordering among rows. Images, video, text, time series, and spatial data all violate at least one of these assumptions.
- The EDA mindset (distributions, outliers, missingness, class balance) applies to all data types; only the specific questions and tools change.
- For images and text, EDA focuses on size distributions, class balance, and vocabulary or pixel quality; for time series, on trend, seasonality, autocorrelation, and stationarity; for spatial data, on coverage, spatial autocorrelation, and coordinate consistency.
- Recognizing a data type's structural properties is the prerequisite for choosing the right preparation method and evaluation strategy.

As always: Happy learning, happy life! 🫶


---

> **Navigation:** [Part Index](00-index.md) | [Main Index](../index.md) | [Preparing Non-Tabular Data -->](02-beyond-tabular-prep.md)

Script v1.3 (2026-06-09) · FGN
