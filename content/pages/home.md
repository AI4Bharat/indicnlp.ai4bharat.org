---
title: "IndicNLP"
weight: 0
url: /home
---
           
We are working towards building a better ecosystem for Indian languages while also keeping up with the recent advancements in NLP. To this end, we are releasing **IndicNLPSuite**, which is a collection of various resources and models for Indian languages:

* <a href="/corpora"><b>IndicCorp:</b></a> A lot of NLP models require a large amount of training data, which most of the Indian languages lack. In this project, we develop a large-scale Indic corpora by intesively crawling the web. The corpora that we build has a total of 8.9 billion tokens and covers 12 major Indian languages - making it the largest public corpus for most of the Indian languages.
* <a href="/indicft"><b>IndicFT:</b></a> fastText is a well-suited model for Indian languages because of their rich morphological structure. We pre-train and benchmark fastText embeddings on our corpora, producing embeddings that outperform the official fastText embeddings for Indian languages on a variety of tasks.
* <a href="/indic-bert"><b>IndicBERT:</b></a> To improve performance and coverage of Indian languages on a wide variety of tasks, we also develop and evaluate IndicBERT. IndicBERT is a multilingual ALBERT model (a lighter variant of BERT) pre-trained on 12 major Indian languages:  Assamese, Bengali, English, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu. It provides state-of-the-art performance on some of the tasks.
* <a href="/indic-glue"><b>IndicGLUE:</b></a> This is a benchmark containing various tasks to evaluate the natural language understanding capabilities of language models fpr Indian languages.

You can read more about the _IndicNLPSuite_ in this [paper](https://indicnlp.ai4bharat.org/papers/arxiv2020_indicnlp_corpus.pdf). This is a pre-print version of our upcoming paper at _Findings of EMNLP_. Camera-ready copy will be available soon. 

----

### Citing

If you are using any of the resources, please cite the following article: 

```
@inproceedings{kakwani2020indicnlpsuite,
    title={{IndicNLPSuite: Monolingual Corpora, Evaluation Benchmarks and Pre-trained Multilingual Language Models for Indian Languages}},
    author={Divyanshu Kakwani and Anoop Kunchukuttan and Satish Golla and Gokul N.C. and Avik Bhattacharyya and Mitesh M. Khapra and Pratyush Kumar},
    year={2020},
    booktitle={Findings of EMNLP},
}
``` 

If you are using IndicGLUE and additional evaluation datasets in your work, then we request you to use the following detailed citation text so that the original authors of the datasets also get credit for their work. As more authors contribute to this benchmark we will add their references also to the below text.


<div style=" font-size: .85em; line-height: 1.45; text-align:left; padding: 1rem;">
We use the IndicGLUE dataset <code>\cite{kakwani2020indicnlpsuite}</code> which is an evaluation benchmark containing datasets for NLU tasks in Indian languages. Some of these datasets were built from Wikipidea and IndicCorp <code>\cite{kakwani2020indicnlpsuite}</code>. In addition, it also contains other publicly available datasets for cross-lingual similarity <code>\cite{siripragrada-etal-2020-multilingual}</code>, named entity recognition <code>\cite{pan-etal-2017-cross}</code>, paraphrase detection <code>\cite{Kumar2016DPILFIRE2016OO}</code>, discourse analysis <code>\cite{Dhanwal2020AnAD}</code>, sentiment analysis <code>\cite{cicling/Akhtar16}</code>, <code>\cite{DBLP:conf/coling/Akhtar0EB16}</code>, <code>\cite{mukku-mamidi-2017-actsa}</code> and genre classification <code>\footnote{https://github.com/goru001/inltk}</code> <code>\footnote{https://www.kaggle.com/csoham/classification-bengali-news-articles-indicnlp}</code> <code>\footnote{https://github.com/NirantK/hindi2vec/releases/tag/bbc-hindi-v0.1}</code>. It also contains translations of the original WNLI <code>\cite{Levesque2011TheWS}</code> and COPA <code>\cite{Gordon2011SemEval2012T7}</code> datasets in 3 Indian languages.
</div>


The bibtex entries for the above sources is available [here](https://indicnlp.ai4bharat.org/papers/indic-glue.bib).


----

### IndicNLP Catalog

In an effort to help discoverability of Indian language resources, we have started a collaborative catalog of known NLP resources for Indic languages. 
Check out the <a href="https://github.com/AI4Bharat/indicnlp_catalog">IndicNLP Catalog</a> if you are looking for Indian NLP resources, and add to the catalog any resources you may know of or have created.



----

### License

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />
<p/>
<span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">IndicNLP Suite</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>. This license applies to datasets created as part of the project. For external datasets in the IndicGLUE benchmark, please look at the respective license terms.


The IndicBERT [code](https://github.com/AI4Bharat/indic-bert) (and [model](https://huggingface.co/ai4bharat/indic-bert)) are released under the MIT License.