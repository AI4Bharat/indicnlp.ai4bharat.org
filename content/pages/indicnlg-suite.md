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


You can read more about IndicNLGSuite [in this paper](). We have benchmarked our own monolingual and multilingual models based on <a href="../indic-bart">IndicBART</a> and found that our models perform at par with or are better than baseline models such as mT5. 

### IndicBART fine-tuning and decoding
- Follow the setup instructions [here](https://github.com/AI4Bharat/indic-bart/blob/main/README.md#installation).
    - We use the [YANMTT](https://github.com/prajdabre/yanmtt) toolkit for fine-tuning IndicBART.
- Extract the input and target text from the [json files]() or [HuggingFace format files]().
    - For question generation, concatenate the question and context into a single line.
    - Convert the scripts in the extracted files into Devanagari using the [Indic Script Converter](https://github.com/AI4Bharat/indic-bart/blob/main/indic_scriptmap.py).
- [Here](https://github.com/AI4Bharat/indic-bart/blob/main/README.md#fine-tuning-command-1) is a command for fine-tuning IndicBART for summarization. 
    - The correct input and output file paths should be provided.
    - Use appropriate hyperparameters according the paper.
- Decode the test set using the fine-tuned model after modifying [this](https://github.com/AI4Bharat/indic-bart/blob/main/README.md#decoding-command-1) command.
    - Map the output to the original script using the script converter.
- <b>Alternatively</b>: IndicBART is uploaded to HuggingFace hub [here](https://huggingface.co/ai4bharat/IndicBART).
    - Modify the HuggingFace [summarization](https://github.com/huggingface/transformers/tree/master/examples/pytorch/summarization) script to use the IndicBART model.
    - This script can use the json as well as HuggingFace format files.
    - Ensure that script mapping is done before training and after decoding.


### Downloads
- IndicWikiBio: [json](), [huggingface](https://huggingface.co/datasets/ai4bharat/IndicWikiBio)
- IndicHeadlineGeneration: [json](), [huggingface](https://huggingface.co/datasets/ai4bharat/IndicHeadlineGeneration)
- IndicSentenceSummarization: [json](), [huggingface](https://huggingface.co/datasets/ai4bharat/IndicSentenceSummarization)
- IndicParaphrase: [json](), [huggingface](https://huggingface.co/datasets/ai4bharat/IndicParaphrase)
- IndicQuestionGeneration: [json](), [huggingface](https://huggingface.co/datasets/ai4bharat/IndicQuestionGeneration)


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


