---
title: "IndicBART"
weight: 60
url: /indic-bart
---

IndicBART is a multilingual,  sequence-to-sequence pre-trained model focusing on Indic languages and English. It currently supports 11 Indian languages and is based on the mBART architecture. You can use IndicBART model to build natural language generation applications for Indian languages by finetuning the model with supervised training data for tasks like machine translation, summarization, question generation, etc. Some salient features of the IndicBART are:

- Supported languages: Assamese, Bengali, Gujarati, Hindi, Marathi, Odiya, Punjabi, Kannada, Malayalam, Tamil, Telugu and English. Not all of these languages are supported by mBART50 and mT5.
- The model is much smaller than the mBART and mT5(-base) models, so less computationally expensive for finetuning and decoding.
- Trained on large Indic language corpora (452 million sentences and 9 billion tokens) which also includes Indian English content. 

You can read more about IndicBART [in this paper](https://arxiv.org/abs/2109.02903).

### Model Repository

You can download the model and find instructions for model finetuning and decoding in this [IndicBART github repo](https://github.com/AI4Bharat/indic-bart). 

### Contributors 

- Raj Dabre 
- Himani Shrotriya
- Anoop Kunchukuttan 
- Ratish Puduppully 
- Mitesh M. Khapra  
- Pratyush Kumar

### Paper


If you use IndicBART, please cite the [following paper](https://arxiv.org/abs/2109.02903):

```
@inproceedings{dabre2021indicbart,
      title={IndicBART: A Pre-trained Model for Natural Language Generation of Indic Languages}, 
      author={Raj Dabre and Himani Shrotriya and Anoop Kunchukuttan and Ratish Puduppully and Mitesh M. Khapra and Pratyush Kumar},
      year={2022},
      booktitle={Findings of the Association for Computational Linguistics (to appear)},
    }    
```   


### License

The model is available under the MIT License.
