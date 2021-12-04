---
title: "IndicWav2Vec"
weight: 200
toc: true
url: /indicwav2vec
---
  
IndicWav2Vec is a multilingual speech model pretrained on 40 Indian langauges. This model represents the largest diversity of Indian languages in the pool of multilingual speech models. We fine-tune this model for downstream ASR for 9 languages and obtain state-of-the-art results on 3 public benchmarks, namely MUCS, MSR and OpenSLR. 

As part of IndicWav2Vec we create largest publicly available corpora for 40 languages from 4 different language families. We also trained state-of-the-art ASR models for 9 Indian languages. 

All the resources (i) pretraining data (ii) pre-trained models (iii) fine-tuned models (iv) language models are made publicly available.

### Code

All the code and scripts for data processing, pretraining and fine-tuning can be found in our GitHub repository [here](https://github.com/AI4Bharat/IndicWav2Vec)

### Downloads

#### Pretraining Data

The YouTube Video IDs we used for creating the pretraining data can be found [here](https://github.com/AI4Bharat/IndicWav2Vec/tree/main/data_prep_scripts/urls)

The pipeline for data processing can be found [here](https://github.com/AI4Bharat/IndicWav2Vec/tree/main/data_prep_scripts)

<!-- The language-wise subsets can be found in the table

| Language  |      Url     | Language |      Url     |
|-----------|:------------:|----------|:------------:|
| assamese  | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/assamese.txt) | manipuri | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/manipuri.txt) |
| bengali   | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/bengali.txt) | marathi  | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/marathi.txt) |
| bodo      | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/bodo.txt) | nepali   | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/nepali.txt) |
| dogri     | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/dogri.txt) | odia     | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/odia.txt) |
| gujarati  | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/gujarati.txt) | punjabi  | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/punjabi.txt) |
| hindi     | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/hindi.txt) | sanskrit | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/sanskrit.txt) |
| kannada   | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/kannada.txt) | santhali | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/santhali.txt) |
| kashmiri  | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/kashmiri.txt) | sindhi   | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/sindhi.txt) |
| konkani   | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/konkani.txt) | tamil    | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/tamil.txt) |
| maithili  | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/maithili.txt) | telugu   | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/telugu.txt) |
| malayalam | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/malayalam.txt) | urdu     | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/urdu.txt) | -->

#### Pretrained Models

- IndicWav2Vec BASE can be downloaded from [here](https://storage.googleapis.com/indicwav2vec-public/pretraining-ckpts/indicwav2vec-base.pt)
- IndicWav2Vec LARGE can be downloaded from [here](https://storage.googleapis.com/indicwav2vec-public/pretraining-ckpts/indicwav2vec-large.pt)

#### Fine-tuned Models

Language-wise fine-tuned models can be found in the table

| Language  |      Url     |
|-----------|:------------:|
| bengali   | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/bengali_large.pt) |
| gujarati  | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/gujarati_large.pt) |
| hindi     | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/hindi_large.pt) |
| marathi   | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/marathi_large.pt) |
| nepali    | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/nepali_large.pt) |
| odia      | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/odia_large.pt) |
| sinhala   | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/sinhala_large.pt) |
| tamil     | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/tamil_large.pt) |
| telugu    | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/telugu_large.pt) |

#### Language Models

Language-wise KenLM langauge models can be found in the table

| Language  |      Url     |
|-----------|:------------:|
| bengali   | [download](https://storage.googleapis.com/indicwav2vec-public/language-models/bengali.zip) |
| gujarati  | [download](https://storage.googleapis.com/indicwav2vec-public/language-models/guharati.zip) |
| hindi     | [download](https://storage.googleapis.com/indicwav2vec-public/language-models/hindi.zip) |
| marathi   | [download](https://storage.googleapis.com/indicwav2vec-public/language-models/marathi.zip) |
| nepali    | [download](https://storage.googleapis.com/indicwav2vec-public/language-models/nepali.zip) |
| odia      | [download](https://storage.googleapis.com/indicwav2vec-public/language-models/odia.zip) |
| tamil     | [download](https://storage.googleapis.com/indicwav2vec-public/language-models/tamil.zip) |
| telugu    | [download](https://storage.googleapis.com/indicwav2vec-public/language-models/telugu.zip) |



<!-- ### Change Log
- 06 July 2021, v0.2.1 data with metadata of source and Labse Alignment Score (LAS) was made available [here](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/samanantar_v0.2_las.zip) -->


### Contributors

- Tahir Javed, <sub>([IITM](https://www.iitm.ac.in), [AI4Bharat](https://ai4bharat.org))</sub>
- Sumanth Doddapaneni, <sub>([AI4Bharat](https://ai4bharat.org), [RBCDSAI](https://rbcdsai.iitm.ac.in))</sub>
- Abhigyan Raman, <sub>([AI4Bharat](https://ai4bharat.org))</sub>
- Kaushal Bhogale, <sub>([AI4Bharat](https://ai4bharat.org))</sub>
- Gowtham Ramesh, <sub>([AI4Bharat](https://ai4bharat.org), [RBCDSAI](https://rbcdsai.iitm.ac.in))</sub>
- Anoop Kunchukuttan, <sub>([Microsoft](https://www.microsoft.com/en-in/), [AI4Bharat](https://ai4bharat.org))</sub>
- Pratyush Kumar, <sub>([Microsoft](https://www.microsoft.com/en-in/), [AI4Bharat](https://ai4bharat.org))</sub>
- Mitesh Khapra, <sub>([IITM](https://www.iitm.ac.in), [AI4Bharat](https://ai4bharat.org), [RBCDSAI](https://rbcdsai.iitm.ac.in))</sub>


### Citing

If you are using any of the resources, please cite the following article: 

```
@misc{javed2021building,
      title={Towards Building ASR Systems for the Next Billion Users}, 
      author={Tahir Javed and Sumanth Doddapaneni and Abhigyan Raman and Kaushal Santosh Bhogale and Gowtham Ramesh and Anoop Kunchukuttan and Pratyush Kumar and Mitesh M. Khapra},
      year={2021},
      eprint={2111.03945},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
``` 

### License

<!-- <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /> -->

<span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">The pretraining data</span> is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">Attribution-ShareAlike 4.0 International</a> license.

The YouTube videos for the respective IDs are licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc/4.0/">Attribution-NonCommercial 4.0 International</a> license.

IndicWav2Vec is MIT-licensed. The license applies to all pretrained, fine-tuned and language models as well.
