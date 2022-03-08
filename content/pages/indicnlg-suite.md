---
title: "IndicNLG Suite"
weight: 80
url: /indicnlg-suite
---

IndicNLG suite is a collection of datasets for benchmarking Natural Language Generation (NLG) for 11 Indic languages spanning five diverse NLG tasks. The datasets were created using a combination of crawling websites, machine translation, n-gram count and regular expression based cleaning . Overall, the suite contains about 8.5M examples across all languages and tasks and is the largest NLG dataset to date as well as the first of it's kind of Indic languages. You can use these datasets to benchmark your own NLG systems.

<ul>
<li>Supported languages: Assamese, Bengali, Gujarati, Hindi, Marathi, Odiya, Punjabi, Kannada, Malayalam, Tamil, Telugu and English. </li>
<li>Supported NLG tasks and datasets: Biography generation using Wikipedia infoboxes (WikiBio), news headline generation, sentence summarization, question generation and paraphrase generation. </li>
<li>Datasets are available in json file and HuggingFace format. </li>
</ul>


You can read more about IndicNLGSuite [in this paper](). We have benchmarked our own monolingual and multilingual models based on <a href="../indic-bart">IndicBART</a> and found that our models perform at par with or are better than baseline models such as mT5. If you ant to fine-tune IndicBart then look <a href="https://github.com/AI4Bharat/indic-bart#finetuning-indicbart-for-summarization">here</a> for an example for fine-tuning summarization models. Minor changes to the training script should enable fine-tuning the model for other tasks.

### Downloads



### Contributors 
- Aman Kumar
- Prachi Sahu
- Himani Shrotriya
- Raj Dabre 
- Ratish Puduppully 
- Anoop Kunchukuttan 
- Amogh Mishra
- Mitesh M. Khapra  
- Pratyush Kumar

### Paper

If you use IndicNLG Suite, please cite the [following paper]():

```
@misc{
    }    
```   


### License


