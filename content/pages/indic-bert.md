---
title: "IndicBERT"
weight: 200
toc: true
url: /indic-bert
---
<a href="https://huggingface.co/ai4bharat/indic-bert"><img alt="Doc" src="https://img.shields.io/static/v1?url=https%3A%2F%2Fhuggingface.co%2Fai4bharat%2Findic-bert&label=Huggingface&color=green&message=indic-bert&logo=huggingface"></a>
  
<br>

IndicBERT is a multilingual ALBERT model trained on large-scale corpora, covering 12 major Indian languages: Assamese, Bengali, English, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu. IndicBERT has much less parameters than other public models like mBERT and XLM-R while it still manages to give state of the art of performance on several tasks.

#### Download Model

The model can be downloaded [here](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/models/indic-bert-v1.tar.gz). Both tf checkpoints and pytorch binaries are included in the archive. Alternatively, you can also download it from [Huggingface](https://huggingface.co/ai4bharat/indic-bert).

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

IndicBERT is pre-trained with IndicNLP corpus which covers 12 Indian languages (including English) The amount of pretraining data for each language is listed below:

| Language          | as     | bn     | en     | gu     | hi     | kn     |         |
| ----------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------- |
| **No. of Tokens** | 36.9M  | 815M   | 1.34B  | 724M   | 1.84B  | 712M   |         |
| **Language**      | **ml** | **mr** | **or** | **pa** | **ta** | **te** | **all** |
| **No. of Tokens** | 767M   | 560M   | 104M   | 814M   | 549M   | 671M   | 8.9B    |


In total, the pretraining corpus has a size of 120GB and contains 8.9B tokens.


#### Evaluation

We evaluate IndicBERT model on a set of tasks as described in the [IndicGLUE page](/indic-glue). Here are the results that we obtain:

##### IndicGLUE

Task | mBERT | XLM-R | IndicBERT |
-----| ----- | ----- | ------ |
News Article Headline Prediction | 89.58 | 95.52 | **95.87** |
Wikipedia Section Title Prediction| **73.66** | 66.33 | 73.31 |
Cloze-style multiple-choice QA | 39.16 | 27.98 | **41.87** |
Article Genre Classification | 90.63 | 97.03 | **97.34** |
Named Entity Recognition (F1-score) | **73.24** | 65.93 | 64.47 | 
Cross-Lingual Sentence Retrieval Task | 21.46 | 13.74 | **27.12** |
Average | 64.62 | 61.09 | **66.66** |

##### Additional Tasks


Task | Task Type | mBERT | XLM-R | IndicBERT |
-----| ----- | ----- | ------ | ----- |
BBC News Classification | Genre Classification | 60.55 | **75.52** | 74.60 |
IIT Product Reviews | Sentiment Analysis | 74.57 | **78.97** | 71.32 |
IITP Movie Reviews | Sentiment Analaysis | 56.77 | **61.61** | 59.03 |
Soham News Article | Genre Classification | 80.23 | **87.6** | 78.45 |
Midas Discourse | Discourse Analysis | 71.20 | **79.94** | 78.44 |
iNLTK Headlines Classification | Genre Classification | 87.95 | 93.38 | **94.52** |
ACTSA Sentiment Analysis | Sentiment Analysis | 48.53 | 59.33 | **61.18** |
Winograd NLI | Natural Language Inference | 56.34 | 55.87 | **56.34** |
Choice of Plausible Alternative (COPA) | Natural Language Inference | 54.92 | 51.13 | **58.33** |
Amrita Exact Paraphrase | Paraphrase Detection | **93.81** | 93.02 | 93.75 |
Amrita Rough Paraphrase | Paraphrase Detection | 83.38 | 82.20 | **84.33** |
Average |  |  69.84 | **74.42** | 73.66 |


\* Note: all models have been restricted to a max_seq_length of 128.



#### Paper


* Kakwani, D., Kunchukuttan, A., Golla, S., N.C. G., Bhattacharyya, A., Khapra, M.M. and Kumar, P., 2020. IndicNLPSuite: Monolingual Corpora, Evaluation Benchmarks and Pre-trained Multilingual Language Models for Indian Languages. *Accepted by Findings of EMNLP 2020* [pdf](https://indicnlp.ai4bharat.org/papers/arxiv2020_indicnlp_corpus.pdf)


