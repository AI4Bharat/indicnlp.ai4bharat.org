---
title: "IndicNLG Suite"
weight: 80
url: /indicnlg-suite
---

IndicNLG suite is a collection of datasets for benchmarking Natural Language Generation (NLG) for 11 Indic languages spanning five diverse NLG tasks. The datasets were created using a combination of crawling websites, machine translation, n-gram count and regular expression based cleaning . Overall, the suite contains about 8.5M examples across all languages and tasks and is the largest multilingual NLG dataset to date as well as the first of its kind for Indic languages. You can use these datasets to benchmark your own NLG systems.

<ul>
<li>Supported languages: Assamese, Bengali, Gujarati, Hindi, Marathi, Odiya, Punjabi, Kannada, Malayalam, Tamil, and Telugu. </li>
<li>Supported NLG tasks and datasets: Biography generation using Wikipedia infoboxes (WikiBio), news headline generation, sentence summarization, question generation and paraphrase generation. </li>
<li>Datasets are available in json file and HuggingFace format. </li>
</ul>

You can read more about IndicNLGSuite [in this paper](https://arxiv.org/abs/2203.05437). We have benchmarked our own monolingual and multilingual models based on <a href="../indic-bart">IndicBART</a> and found that our models perform at par with or are better than baseline models such as mT5. 

### Downloads

The datasets and models are available on [HuggingFace](https://huggingface.co)

| Task      | Dataset | Model |
| ----------- | ----------- | ------- |
| Biography Generation      | [IndicWikiBio](https://huggingface.co/datasets/ai4bharat/IndicWikiBio)      | Coming Soon |
| Headline Generation       | [IndicHeadlineGeneration](https://huggingface.co/datasets/ai4bharat/IndicHeadlineGeneration)        | Coming Soon |
| Sentence Summarization    | [IndicSentenceSummarization](https://huggingface.co/datasets/ai4bharat/IndicSentenceSummarization)        | Coming Soon  |
| Paraphrase Generation     | [IndicParaphrase](https://huggingface.co/datasets/ai4bharat/IndicParaphrase)        | Coming Soon  |
| Question Generation       | [IndicQuestionGeneration](https://huggingface.co/datasets/ai4bharat/IndicQuestionGeneration)        | Coming Soon  |

### IndicBART fine-tuning and decoding
- Follow the setup instructions [here](https://github.com/AI4Bharat/indic-bart/blob/main/README.md#installation).
    - We use the [YANMTT](https://github.com/prajdabre/yanmtt) toolkit for fine-tuning IndicBART.
- Extract the input and target text from the jsonl format files or HuggingFace format files.
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

### Citing

If you use IndicNLG Suite, please cite the [following paper](https://arxiv.org/abs/2203.05437):

```
@misc{kumar2022indicnlg,
      title={IndicNLG Suite: Multilingual Datasets for Diverse NLG Tasks in Indic Languages}, 
      author={Aman Kumar and Himani Shrotriya and Prachi Sahu and Raj Dabre and Ratish Puduppully and Anoop Kunchukuttan and Amogh Mishra and Mitesh M. Khapra and Pratyush Kumar},
      year={2022},
      eprint={2203.05437},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}   
```   

### License

**Datasets**

Different datasets are released under different licenses 

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />
<p/>
<span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type"><b>IndicHeadlineGeneration, IndicSentenceSummarization and IndicParaphrase</b></span> are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.


<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><b>IndicWikiBio and IndicQuestionGeneration</b> are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

**Models** 

All models are released under the MIT license.




