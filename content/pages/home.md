---
title: "IndicNLP"
weight: 0
url: /home
---

We are working towards building a better ecosystem for Indian languages.  To this end, we are building various resources and models for Indian languages:

* <a href="/corpora"><b>IndicCorp:</b></a> A lot of NLP models require a large amount of training data, which most of the Indian languages lack. In this project, we develop a large-scale Indic corpora by intesively crawling the web. The corpora that we build has a total of 8.9 billion tokens and covers 12 major Indian languages - making it the largest public corpus for most of the Indian languages.
* <a href="/indicft"><b>IndicFT:</b></a> fastText is a well-suited model for Indian languages because of their rich morphological structure. We pre-train and benchmark fastText embeddings on our corpora, producing embeddings that outperform the official fastText embeddings for Indian languages on a variety of tasks.
* <a href="/indic-bert"><b>IndicBERT:</b></a> To improve performance and coverage of Indian languages on a wide variety of tasks, we also develop and evaluate IndicBERT. IndicBERT is a multilingual ALBERT model (a lighter variant of BERT) pre-trained on 12 major Indian languages:  Assamese, Bengali, English, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu. It provides state-of-the-art performance on some of the tasks.
* <a href="/indic-bart"><b>IndicBART:</b></a> IndicBART is a multilingual, sequence-to-sequence pre-trained model focusing on Indic languages and English. It currently supports 12 languages and is based on the mBART architecture.
* <a href="/indic-glue"><b>IndicGLUE:</b></a> This is a benchmark containing various tasks to evaluate the natural language understanding capabilities of language models for Indian languages.
* <a href="/indicnlg-suite"><b>IndicNLG Suite:</b></a> This is a benchmark containing various tasks to evaluate the natural language generation capabilities of language models for Indian languages.
* <a href="/samanantar"><b>Samanantar:</b></a> Samanantar is the largest publicly available parallel corpora collection for Indic languages : Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu. The corpus has 49.6M sentence pairs between English to Indian Languages.
* <a href="/indic-trans"><b>IndicTrans:</b></a> IndicTrans is a Transformer-XL model trained on samanantar dataset. Two models are available which can translate from Indic to English and English to Indic. The model can perform translations for 11 lanaguages: Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu.

----

### IndicNLP Catalog

In an effort to help discoverability of Indian language resources, we have started a collaborative catalog of known NLP resources for Indic languages. 
Check out the <a href="https://github.com/AI4Bharat/indicnlp_catalog">IndicNLP Catalog</a> if you are looking for Indian NLP resources, and add to the catalog any resources you may know of or have created.



