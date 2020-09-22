---
title: "IndicFT"
weight: 100
url: /indicft
---


fastText is a subword-aware word embedding model. It is particularly well-suited for Indian languages due to their highly agglutinative morphology. We train fastText models on our IndicNLP Corpora and evaluate them on a set of tasks to measure its performance.

Our fastText models are available for 11 Indian languages:  Assamese, Bengali, English, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu.


#### Usage

To use our fastText models, first [download them](#downloads). Next, install the fastText library:
```bash
pip3 install fasttext
```

and then load the models like this:

```python
import fasttext
model = fasttext.load_model(path_to_binary_file)
```

For tutorials on using this model, please refer to the official [fastText documentation](https://fasttext.cc/docs/en/support.html)


#### Downloads

| Language | as | pa | hi | bn | or | gu | mr | kn | te | ml | ta |
| -------- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| Vectors | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.as.vec) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.pa.vec) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.hi.vec) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.bn.vec) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.or.vec) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.gu.vec) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.mr.vec) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.kn.vec) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.te.vec) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.ml.vec) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.ta.vec) |
| Model | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.as.vec) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.pa.bin) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.hi.bin) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.bn.bin) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.or.bin) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.gu.bin) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.mr.bin) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.kn.bin) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.te.bin) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.ml.bin) | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/embedding-v2/indicnlp.v1.ta.bin) |


#### Evaluation


For a full result of evaluation, check our [paper](https://indicnlp.ai4bharat.org/papers/arxiv2020_indicnlp_corpus.pdf). Here, we show some of the evaluations.


##### Word Similarity


Language | fastText wiki | fastText wiki+CC | Indic fastText
------| -----|-----|----
pa | 0.467 | 0.384 | **0.445**
hi | 0.575 | 0.551 | **0.598**
gu | 0.507 | 0.521 | **0.600**
mr | 0.497 | **0.544** | 0.509 
te | 0.559 | 0.543 | **0.578**
ta | **0.439** | 0.438 | 0.422
Average| 0.507| 0.497| **0.525**


##### News Genre Classification

Language | fastText wiki | fastText wiki+CC | Indic fastText
------| -----|-----|----
pa | **97.12** | 95.53 | 96.47
bn | 96.57 | 97.57 | **97.71**
or | 94.80 | 96.20 | **98.43**
gu | 95.12 | 94.63 | **99.02**
mr | 96.44 | 97.07 | **99.37**
kn | 95.93 | 96.53 | **97.43**
te | 98.67 | 98.08 | **99.17**
ml | 89.02 | 89.18 | **92.83**
ta | 95.99 | 95.90 | **97.26**
Average | 95.52 | 95.63 | **97.52**
