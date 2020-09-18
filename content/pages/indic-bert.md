---
title: "IndicBERT"
weight: 200
toc: true
---

IndicBERT is a multilingual ALBERT model trained on large-scale corpora, covering 12 major Indian languages.



#### Usage

The easiest way to use Indic BERT is through the Huggingface transformers library. It can be simply loaded like this:

```python
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('ai4bharat/indic-bert')
model = AutoModel.from_pretrained('ai4bharat/indic-bert')
```



#### Tutorials

If you want to quickly try experimenting with IndicBERT, we suggest checking out our tutorials and other fine-tuning notebooks that run on Google Colab:
* General Finetuning [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai4bharat/indic-bert/blob/master/notebooks/finetuning.ipynb)


#### Pretraining Details

IndicBERT is pre-trained with IndicNLP corpus which covers 12 Indian languages (including English): Assamese, Bengali, English, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu. The amount of pretraining data for each language is listed below:

| Language          | as     | bn     | en     | gu     | hi     | kn     |         |
| ----------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------- |
| **No. of Tokens** | 36.9M  | 815M   | 1.34B  | 724M   | 1.84B  | 712M   |         |
| **Language**      | **ml** | **mr** | **or** | **pa** | **ta** | **te** | **all** |
| **No. of Tokens** | 767M   | 560M   | 104M   | 814M   | 549M   | 671M   | 8.9B    |


In total, the pretraining corpus has a size of 120GB and contains 8.9B tokens.


#### Evaluation


#### Paper


* Kakwani, D., Kunchukuttan, A.,, Golla, S., N.C. G., Bhattacharyya, A., Khapra, M.M. and Kumar, P., 2020. IndicNLPSuite: Monolingual Corpora, Evaluation Benchmarks and Pre-trained Multilingual Language Models for Indian Languages. *Accepted by Findings of EMNLP 2020* [pdf](https://indicnlp.ai4bharat.org/papers/arxiv2020_indicnlp_corpus.pdf)

#### Downloads

* IndicBERT zip