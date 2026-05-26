> **Navigation:** [<-- Beyond Tabular Data](01-beyond-tabular-eda.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Statistical Significance -->](03-statistical-significance.md)

# Preparing Non-Tabular Data

**Requires:** [EDA: Beyond Tabular Data](../part-03-data-understanding/01-beyond-tabular-eda.md) · [Data Pipelines](04-data-pipelines.md)

**Motivation:** Your preprocessing pipeline handles a tabular feature matrix — impute, encode, scale, done. But what do you do when the input is a string of text, a sequence of sensor readings, or a folder of images? [Beyond Tabular Data](../part-03-data-understanding/01-beyond-tabular-eda.md) established that these formats exist and why they resist tabular treatment. This nugget asks the practical follow-up: how do you actually prepare them?

> You will see how each non-tabular data type requires a specific conversion step before any model can operate on it, how the fit-on-train discipline from [Data Pipelines](04-data-pipelines.md) carries through unchanged, and where sklearn pipelines extend naturally versus where you need different tooling.

## Table of Contents

- [Images and Video](#images-and-video)
- [Text Data](#text-data)
- [Time Series Data](#time-series-data)
- [Spatial Data](#spatial-data)

---

## Images and Video

Every ML model expects a numeric array as input. Images already are numeric arrays, but two issues prevent them from entering most models directly: inconsistent shapes across the dataset and raw pixel scales that interfere with optimization.

### Resizing and Shape Normalization

A model needs fixed-size inputs. If your dataset contains images of varying dimensions — common in real-world collections — every image must be resized to a common target shape before training. The target height and width are design choices, not learned parameters. They are set once and applied identically to training and test images, so no fit-on-train issue arises.

### Pixel Normalization

Raw pixel values sit in $[0, 255]$. Feeding these directly to a gradient-based model slows convergence and can destabilize training. Two standard approaches:

**Divide by 255.** Maps pixel values to $[0, 1]$. Simple and parameter-free — no statistics need to be fit.

**Standardize per channel.** Compute the channel-wise mean and standard deviation from the training images, then subtract the mean and divide by the standard deviation — exactly as `StandardScaler` does for numeric tabular features. These statistics must be fit on training images only and applied unchanged to the test set.

```python
train_mean = X_train_images.mean(axis=(0, 1, 2))
train_std  = X_train_images.std(axis=(0, 1, 2))

X_train_norm = (X_train_images - train_mean) / train_std
X_test_norm  = (X_test_images  - train_mean) / train_std
```

A $224 \times 224$ RGB image, flattened, produces a 150,528-dimensional feature vector. For small, constrained tasks this can work. For anything involving real image structure — detecting edges, objects, or shapes — a CNN exploiting spatial locality is the appropriate tool. Video follows the same normalization logic frame by frame; in practice, video preparation is handled by deep learning frameworks (PyTorch, TensorFlow) that apply the same fit-on-train discipline through their transform pipelines.

---

## Text Data

Text cannot enter a model as characters or words. It must become numbers. The preparation path depends on whether you use a bag-of-words representation or a pre-trained embedding model.

### Bag-of-Words and TF-IDF

The bag-of-words model represents each document as a vector of word counts, one dimension per word in a fixed vocabulary. sklearn's `CountVectorizer` implements this directly:

```python
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train_texts)
X_test_vec  = vectorizer.transform(X_test_texts)
```

The `fit` step builds the vocabulary from the training corpus: which words exist and at which positions. The `transform` step counts those words in each document. Any word not in the training vocabulary is ignored at transform time — this is the fit-on-train rule applied to text, and it is also the correct production behavior: new data will always contain words the model has never seen.

A `TfidfVectorizer` extends bag-of-words with *term frequency–inverse document frequency* weighting. Words that appear in nearly every document ("the," "is") contribute little to distinguishing documents and get down-weighted; words that appear in only a few documents get up-weighted. The IDF weights are computed from the training corpus only.

### Embeddings

Embedding models map each word or sentence to a dense, low-dimensional vector that encodes semantic similarity: "hospital" ends up closer to "clinic" than to "bicycle." Pre-trained models such as word2vec, GloVe, and sentence encoders from transformer-based architectures produce these vectors without requiring labeled training data.

The practical difference from bag-of-words: embedding models are typically loaded as pre-trained artifacts rather than fit on your corpus, so the fit-on-train rule applies mainly to any fine-tuning step or downstream classification head — not to the embedding extraction itself.

### Integrating into a Pipeline

Because sklearn text vectorizers follow the same `fit`/`transform` interface as scalers and imputers, they compose naturally into a `Pipeline`:

```python
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

text_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=5000)),
    ("clf",   LogisticRegression()),
])

text_pipeline.fit(X_train_texts, y_train)
predictions = text_pipeline.predict(X_test_texts)
```

The vocabulary and IDF weights are fit once on the training corpus and travel with the pipeline to production.

> **Discussion:** A team is building a complaint classifier from customer feedback forms. One engineer argues for TF-IDF bag-of-words on 10,000 labeled examples; another argues for a pre-trained sentence embedding model that needs no labeled data to produce representations. What factors would you weigh when choosing between them, and what could go wrong with each approach?

---

## Time Series Data

Time series preparation differs fundamentally from tabular preparation because rows are not exchangeable. The standard `train_test_split` shuffles rows — for time series, this is wrong.

### Temporal Train/Test Split

If the training fold contains observations from the end of the series and the test fold contains observations from the middle, the model has effectively seen the future during training. The correct split is strictly temporal: all training observations come before all test observations.

```python
split_idx = int(len(df) * 0.8)
train = df.iloc[:split_idx]
test  = df.iloc[split_idx:]
```

No `random_state`, no shuffling. The split is deterministic by position. For cross-validation, the same principle applies — each fold must use only past observations to predict future ones. sklearn provides `TimeSeriesSplit` for this purpose.

### Windowing

Most classical models expect a fixed-size feature vector, but a time series is a variable-length sequence. Windowing converts it: slide a window of length $k$ across the series, use the $k$ values within the window as features, and predict the value immediately after the window.

A window of the last 24 hourly readings becomes a 24-dimensional feature vector. The choice of $k$ encodes your assumption about how far back in time the current value depends — a question the ACF plot from EDA helps answer.

```python
def make_windows(series: np.ndarray, k: int):
    X, y = [], []
    for i in range(len(series) - k):
        X.append(series[i : i + k])
        y.append(series[i + k])
    return np.array(X), np.array(y)

X_train_w, y_train_w = make_windows(train_series, k=24)
X_test_w,  y_test_w  = make_windows(test_series,  k=24)
```

Any within-window normalization must be fit on training windows only. Specialized models — ARIMA, RNNs, LSTMs, sequence transformers — model temporal dependencies more directly and often skip explicit windowing. These are beyond the scope of this course, but the temporal split and windowing steps above are the foundation any approach needs.

---

## Spatial Data

Spatial data preparation focuses less on feature conversion — the measurements are already numeric — and more on the split strategy and coordinate handling.

### Spatial Train/Test Split

A random split assigns nearby, correlated measurements to both train and test. Because those observations are not independent, test-set performance will be optimistic: the model has effectively trained on measurements that look nearly identical to the ones it is evaluated on. A spatial split holds out an entire geographic region — all measurements from that region go to test, none to train. This better reflects how the model will generalize to new locations.

### Feature Engineering from Coordinates

Raw latitude and longitude can be used as features, but they often carry less signal than derived spatial features: distance to a reference point (a contamination source, a city center), membership in a spatial cluster, or a co-variate from a separate spatial dataset (elevation, population density). These derived features are computed after the spatial split, using training-set statistics for any normalization.

Before computing any distance-based features, confirm that all coordinates share a consistent coordinate reference system and projection. Mixing systems — degrees and meters, or different datums — produces meaningless distances.

The common thread across all four data types: whenever observations are not exchangeable because order or proximity carries information, a random split is wrong. Recognize the structure, then design the split to respect it.

---

## Summary

- Images require resizing to a common shape and pixel normalization; channel-wise mean and standard deviation for standardization must be computed from training images only, exactly as with tabular `StandardScaler`.
- Text must be converted to a numeric representation; bag-of-words (`CountVectorizer`, `TfidfVectorizer`) and embedding models both follow sklearn's `fit`/`transform` interface and compose into a `Pipeline`; vocabulary and IDF weights are fit on training documents only.
- Time series require a strictly temporal split (no shuffle) and windowing to convert the variable-length sequence into fixed-size feature vectors; `TimeSeriesSplit` applies the same principle to cross-validation.
- Spatial data requires a spatial split that holds out a geographic region; raw coordinates may be supplemented with derived spatial features, computed after the split using training-set statistics only.

As always: Happy learning, happy life! 🫶

---

> **Navigation:** [<-- Beyond Tabular Data](01-beyond-tabular-eda.md) | [Part Index](00-index.md) | [Main Index](../index.md) | [Statistical Significance -->](03-statistical-significance.md)