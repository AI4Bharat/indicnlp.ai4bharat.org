---
title: "IndicWav2Vec"
weight: 200
toc: true
url: /indicwav2vec
---
  

As part of IndicWav2Vec we create lastest publicly available corpora for 40 languages from 4 different language families. We also trained state-of-the-art ASR models for 9 Indian languages. 

All the resources (i) pretraining data (ii) pre-trained models (iii) fine-tuned models (iv) language models are made publicly available.

### Code

All the code and script for data processing, pretraining and fine-tuning can be found in our GitHub repository [here](https://github.com/AI4Bharat/IndicWav2Vec)

### Downloads

#### Pretraing Data

The pretraining data used for training IndicWav2Vec can be found [here]()

The language wise subsets can be found in the table

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
| malayalam | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/malayalam.txt) | urdu     | [download](https://storage.googleapis.com/indicwav2vec-public/pretraining-data/urdu.txt) |

#### Pretrained Models

- IndicWav2Vec BASE can be downloaded from [here]()
- IndicWav2Vec LARGE can be downloaded from [here]()

#### Fine-tuned Models

Language wise fine-tuned models can be found in the table

| Language  | Url          |
|-----------|--------------|
| bengali   | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/bengali_large.pt) |
| gujarati  | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/gujarati_large.pt) |
| hindi     | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/hindi_large.pt) |
| marathi   | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/marathi_large.pt) |
| nepali    | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/nepali_large.pt) |
| odia      | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/odia_large.pt) |
| sinhala   | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/sinhala_large.pt) |
| tamil     | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/tamil_large.pt) |
| telugu    | [download](https://storage.googleapis.com/indicwav2vec-public/fine-tuning-ckpts/telugu_large.pt) |

<!-- #### Language Models

-  -->



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

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />
<p/>
<span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">IndicWav2Vec</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>. This license applies to datasets created as part of the project.

