---
title: "IndicCorp"
weight: 10
url: /corpora
---

IndicCorp has been developed by discovering and scraping thousands of web sources - primarily news, magazines and books, over a duration of several months.

IndicCorp is one of the largest publicly-available corpora for Indian languages. It has also been used to train our released models which have obtained state-of-the-art performance on many tasks.

### Corpus Format

The corpus is a single large text file containing one sentence per line. The [publicly released version](#downloads) is randomly shuffled, untokenized and deduplicated. 

### Downloads


| Language | \# News Articles* | Sentences     | Tokens        | Link     |
| -------- | ----------------- | ------------- | ------------- | -------- |
| as       | 0.60M             | 1.39M   |  32.6M  | [link](https://ai4b-my.sharepoint.com/:u:/g/personal/sumanthdoddapaneni_ai4bharat_org/ETfz3fB3uKdCrfYY5h0K4QwBwuqeSQ17w6nMc1dlOda_eg?e=6nDbkl) |
| bn       | 3.83M             | 39.9M | 836M  | [link](https://ai4b-my.sharepoint.com/:u:/g/personal/sumanthdoddapaneni_ai4bharat_org/EXlcZP77M2BLrVsFcpebcVEBDldXgCKh334weoWRbLRh4A?e=uGNaaF) |
| en       | 3.49M             | 54.3M | 1.22B | [link](https://storage.googleapis.com/ai4bharat-public-indic-nlp-corpora/indiccorp/en.tar.xz) |
| gu       | 2.63M             | 41.1M | 719M  | [link](https://ai4b-my.sharepoint.com/:u:/g/personal/sumanthdoddapaneni_ai4bharat_org/EawfDxTNnYZFvmH_Gzcc-PsB1EhVUrj-yPfdFSvc8zrOaA?e=wpe4iS) |
| hi       | 4.95M             | 63.1M |  1.86B | [link](https://ai4b-my.sharepoint.com/:u:/g/personal/sumanthdoddapaneni_ai4bharat_org/EQ-iFqR25dpBsTvM5gtiq4gBKJEUjdOL7UaR7Qyq4BppXg?e=cM85WM) |
| kn       | 3.76M             | 53.3M | 713M  | [link](https://ai4b-my.sharepoint.com/:u:/g/personal/sumanthdoddapaneni_ai4bharat_org/EZGVhzgIYi1EhOLAGFzWoI0BqnHi8Iz8TlLmOGMcJK93Ww?e=vfoCme) |
| ml       | 4.75M             | 50.2M |  721M  | [link](https://ai4b-my.sharepoint.com/:u:/g/personal/sumanthdoddapaneni_ai4bharat_org/EQYtgDqJKtpLnoCVPvKvSvcBhh2mmeiqZhO58aRwS6UCVA?e=CbcQna) |
| mr       | 2.31M             | 34.0M | 551M  | [link](https://ai4b-my.sharepoint.com/:u:/g/personal/sumanthdoddapaneni_ai4bharat_org/EU01E9LfSMJKlJQYObwLwRIBHD6gSet4uKbQwoTGqcb4YA?e=NNiPdh) |
| or       | 0.69M             | 6.94M   | 107M   | [link](https://ai4b-my.sharepoint.com/:u:/g/personal/sumanthdoddapaneni_ai4bharat_org/ESMQWhhrUaJBlh1qiEcyrYcBno-0cVJyHjHzO8m1h2P0UA?e=toRScw) |
| pa       | 2.64M             | 29.2M |  773M  | [link](https://ai4b-my.sharepoint.com/:u:/g/personal/sumanthdoddapaneni_ai4bharat_org/Ea_Am4EafJhPgCzAxm39BGEBGQbaVLQxShDr-bYOkuM2Vg?e=1DiReE) |
| ta       | 4.41M             |  31.5M   |  582M  | [link](https://ai4b-my.sharepoint.com/:u:/g/personal/sumanthdoddapaneni_ai4bharat_org/ESWg98k00UZHv9ZikQH7ARsBQ1PPGIvV59FjOG3I6v9YVQ?e=lf4Idp) |
| te       | 3.98M             | 47.9M   |  674M  | [link](https://ai4b-my.sharepoint.com/:u:/g/personal/sumanthdoddapaneni_ai4bharat_org/EShEqp0xf2dKoxLhRpre-s0BFsaPhgFTFrotIRj3-vfdHA?e=q8xCac) |

\* Excluding articles obtained from the OSCAR corpus

### Processing Corpus

For processing the corpus into other forms (tokenized, transliterated etc.), you can use the [indicnlp library](https://github.com/anoopkunchukuttan/indic_nlp_library).  As an example, the following code snippet can be used to tokenize the corpus:

```python
from indicnlp.tokenize.indic_tokenize import trivial_tokenize
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory

lang = 'kn'
input_path = 'kn'
output_path = 'kn.tok.txt'

normalizer_factory = IndicNormalizerFactory()
normalizer = normalizer_factory.get_normalizer(lang)

def process_sent(sent):
    normalized = normalizer.normalize(sent)
    processed = ' '.join(trivial_tokenize(normalized, lang))
    return processed

with open(input_path, 'r', encoding='utf-8') as in_fp,\
	 open(output_path, 'w', encoding='utf-8') as out_fp:
    for line in in_fp.readlines():
        sent = line.rstrip('\n')
        toksent = process_sent(sent)
        out_fp.write(toksent)
        out_fp.write('\n')


```

### Citing

If you are using IndicGLUE, please cite the following article: 

```
@inproceedings{kakwani2020indicnlpsuite,
    title={{IndicNLPSuite: Monolingual Corpora, Evaluation Benchmarks and Pre-trained Multilingual Language Models for Indian Languages}},
    author={Divyanshu Kakwani and Anoop Kunchukuttan and Satish Golla and Gokul N.C. and Avik Bhattacharyya and Mitesh M. Khapra and Pratyush Kumar},
    year={2020},
    booktitle={Findings of EMNLP},
}
``` 

----

### License

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />
<p/>
<span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">IndicCorp</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>. 

