---
title: "Aksharantar"
weight: 20
toc: true
url: /aksharantar
---
  

Aksharantar is the largest publicly available transliteration dataset for 20 Indic languages. The corpus has 26M Indic language-English transliteration pairs.
<!--  -->
<!-- Samanantar is the largest publicly available parallel corpora collection for Indic languages: Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu. The corpus has 49.6M sentence pairs between English to Indian Languages. -->
<!--  -->
<!-- ### Update 04-11-2021
Samanantar v0.3 along with LaBSE scores metadata is available for download. Go to [Downloads](#downloads) -->

### Dataset Format

<!-- The [publicly released version](#downloads) is randomly shuffled, untokenized, and deduplicated. -->
The [publicly released version](https://github.com/SushaneP/indicnlp.ai4bharat.org/edit/master/content/pages/aksharantar.md#downloads) is randomly shuffled, untokenized and deduplicated.

## Downloads
<!-- 
### STS Benchmark

The Semantic Textual Similarity (STS) benchmark can be downloaded from [here](https://storage.googleapis.com/samanantar-public/human_annotations.tsv) -->

### Indic-English

<!-- The entire dataset can be downloaded from [here](https://storage.googleapis.com/samanantar-public/data/all-without-supara.zip) -->
<!-- 
The entire dataset can be downloaded from [Samanantar v0.3](https://storage.googleapis.com/samanantar-public/V0.3/source_wise_splits.zip).  -->
- The Aksharantar dataset can be downloaded as a single zip file from the [Aksharantar Hugging Face repository](https://huggingface.co/datasets/ai4bharat/Aksharantar/tree/main).
- Each language-pair corpus in the Aksharantar dataset is split into training, validation and test subsets. Each subset is a JSONL file consisting of individual data instances comprising a unique identifier, native word, English word, transliteration source and a score (if applicable).
- Individual language-pair download links are provided in the [data split](https://github.com/SushaneP/indicnlp.ai4bharat.org/edit/master/content/pages/aksharantar.md#data-split) below.

<!-- The folder has 3 directories with separate sub-directories for each source:
- Existing - All existing data compiled before Aksharantar
- Mined - Mined as part of Aksharantar
- Manually annotated -->

### Benchmarks

<!-- The testsets used to benchmark IndicTrans can be found [here](https://storage.googleapis.com/samanantar-public/benchmarks.zip) -->
Language-pair testsets ({lang_test}) were used to benchmark the IndicXlit model.

<!-- 
### Mirror Links

- Please use this mirror [Google Drive]() link to download the Aksharantar dataset.
 -->

### Data Split

The language-wise splits for Aksharantar is shown in the table with total number of word pairs (in millions). Individual download links for each language-pair are as against the hyperlink.

<!-- | Language Pair | Link |
| -------- | -------- |
| as-en <sub>(A MB)</sub> | [0.217M]() |
| bn-en <sub>(B MB)</sub> | [1.337M]() |
| brx-en <sub>(B2 MB)</sub> | [0.044M]() |
| gu-en <sub>(C MB)</sub> | [1.236M]() |
| hi-en <sub>(D MB)</sub> | [1.522M]() |
| kn-en <sub>(E MB)</sub> | [3.01M]() |
| ks-en <sub>(E2 MB)</sub> | [0.064M]() |
| kok-en <sub>(E2 MB)</sub> | [0.702M]() |
| mai-en <sub>(E3 MB)</sub> | [0.37M]() |
| ml-en <sub>(F MB)</sub> | [4.195M]() |
| mni-en <sub>(F2 MB)</sub> | [0.016M]() |
| mr-en <sub>(G MB)</sub> | [1.594M]() |
| ne-en <sub>(G2 MB)</sub> | [2.458M]() |
| or-en <sub>(H MB)</sub> | [0.398M]() |
| pa-en <sub>(I MB)</sub> | [0.611M]() |
| san-en <sub>(I2 MB)</sub> | [1.881M]() |
| sd-en <sub>(I3 MB)</sub> | [0.082M]() |
| si-en <sub>(I4 MB)</sub> | [0.037M]() |
| ta-en <sub>(J MB)</sub> | [3.301M]() |
| te-en <sub>(K MB)</sub> | [2.521M]() |
| ur-en <sub>(K2 MB)</sub> | [0.748M]() | -->

| Subset | [as-en <sub>(4.72 MB)</sub>](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/asm.zip) | [bn-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/ben.zip) <sub>(31.5 MB)</sub> | [brx-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/brx.zip) <sub>(0.933 MB)</sub> | [gu-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/guj.zip) <sub>(29.5 MB)</sub> | [hi-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/hin.zip) <sub>(31.4 MB)</sub> | [kn-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/kan.zip) <sub>(83.7 MB)</sub> | [ks-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/kas.zip) <sub>(1.1 MB)</sub> | [kok-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/kok.zip) <sub>(16.6 MB)</sub> | [mai-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/mai.zip) <sub>(6.74 MB)</sub> | [ml-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/mal.zip) <sub>(125 MB)</sub> | [mni-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/mni.zip) <sub>(0.313 MB)</sub> | [mr-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/mar.zip) <sub>(39.9 MB)</sub> | [ne-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/nep.zip) <sub>(67 MB)</sub> | [or-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/ori.zip) <sub>(9.09 MB)</sub> | [pa-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/pan.zip) <sub>(12.1 MB)</sub> | [sa-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/san.zip) <sub>(56 MB)</sub> | [sd-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/sid.zip) <sub>(1.37 MB)</sub> | [ta-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/tam.zip) <sub>(92.7 MB)</sub> | [te-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/tel.zip) <sub>(69.1 MB)</sub> | [ur-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/urd.zip) <sub>(17 MB)</sub> |
|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| Training | 179K | 1231K | 36K | 1143K | 1299K | 2907K | 47K | 613K | 283K | 4101K | 10K | 1453K | 2397K | 346K | 515K | 1813K | 60K | 3231K | 2430K | 699K |
| Validation | 4K | 11K | 3K | 12K | 6K | 7K | 4K | 4K | 4K | 8K | 3K | 8K | 3K | 3K | 9K | 3K | 8K | 9K | 8K | 12K |
| Test | 5531 | 5009 | 4136 | 7768 | 5693 | 6396 | 7707 | 5093 | 5512 | 6911 | 4925 | 6573 | 4133 | 4256 | 4316 | 5334 | - | 4682 | 4567 | 4463 |

<!-- 
 -->
<!-- #### Indic-Indic

The entire Indic-Indic data can be downloaded from [here](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/indic2indic.zip)


Language wise splits for Indic-Indic data can be downloaded from the table below. Each link contains the number of sentence pairs in millions.

|    | as | bn | gu | hi | kn | ml | mr | or | pa | ta | te |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| as |    |[0.36M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-bn.zip)  |  [0.14M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-gu.zip)  |  [0.16M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-hi.zip)  |  [0.19M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-kn.zip)  |  [0.23M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-ml.zip)  |  [0.16M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-mr.zip)  |  [0.07M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-or.zip)  |  [0.11M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-pa.zip)  |  [0.22M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-ta.zip)  |  [0.21M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-te.zip)  | 
| bn |  [0.36M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-bn.zip)  |   |  [1.58M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-gu.zip)  |  [2.53M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-hi.zip)  |  [2.14M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-kn.zip)  |  [2.88M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-ml.zip)  |  [1.83M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-mr.zip)  |  [0.59M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-or.zip)  |  [1.11M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-pa.zip)  |  [2.44M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-ta.zip)  |  [2.35M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-te.zip)  | 
| gu |  [0.14M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-gu.zip)  |  [1.58M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-gu.zip)  |   | [1.86M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-hi.zip)  |  [2.07M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-kn.zip)  |  [2.36M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-ml.zip)  |  [1.76M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-mr.zip)  |  [0.53M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-or.zip)  |  [1.13M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-pa.zip)  |  [2.07M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-ta.zip)  |  [2.31M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-te.zip)  | 
| hi |  [0.16M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-hi.zip)  |  [2.53M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-hi.zip)  |  [1.86M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/gu-hi.zip)  |    |  [2.14M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-kn.zip)  |  [2.72M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-ml.zip)  |  [1.99M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-mr.zip)  |  [0.66M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-or.zip)  |  [1.44M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-pa.zip)  |  [2.48M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-ta.zip)  |  [2.42M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-te.zip) |
| kn |  [0.19M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-kn.zip)  |  [2.14M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-kn.zip)  |  [2.07M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/gu-kn.zip)  |  [2.14M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-kn.zip)  |    |  [2.89M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/kn-ml.zip)  |  [1.82M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/kn-mr.zip)  |  [0.54M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/kn-or.zip)  | [1.12M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/kn-pa.zip)   |  [2.52M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/kn-ta.zip)  |  [2.81M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/kn-te.zip) |
| ml |  [0.23M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-ml.zip)  |  [2.88M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-ml.zip)  |  [2.36M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/gu-ml.zip)  |  [2.72M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-ml.zip)  |  [2.89M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/kn-ml.zip)  |    |  [1.82M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ml-mr.zip)  |  [0.56M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ml-or.zip)  |  [1.11M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ml-pa.zip)  |  [2.60M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ml-ta.zip)  |  [2.68M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ml-te.zip) |
| mr |  [0.16M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-mr.zip)  |  [1.83M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-mr.zip)  |  [1.76M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/gu-mr.zip)  |  [1.99M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-mr.zip)  |  [1.82M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/kn-mr.zip)  |  [1.82M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ml-mr.zip)  |   | [0.58M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/mr-or.zip)  |  [1.06M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/mr-pa.zip)  |  [21.12M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/mr-ta.zip)  |  [2.23M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/mr-te.zip) |
| or |  [0.07M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-or.zip)  |  [0.59M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-or.zip)  |  [0.53M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/gu-or.zip)  |  [0.66M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-or.zip)  |  [0.54M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/kn-or.zip)  |  [0.56M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ml-or.zip)  |  [0.58M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/mr-or.zip)  |    |  [0.50M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/or-pa.zip)  |  [1.09M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/or-ta.zip)  |  [1.12M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/or-te.zip) |
| pa |  [0.11M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-pa.zip)  |  [1.11M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-pa.zip)  |  [1.13M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/gu-pa.zip)  |  [1.44M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-pa.zip)  |  [1.12M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/kn-pa.zip)  |  [1.11M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ml-pa.zip)  |  [1.06M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/mr-pa.zip)  |  [0.50M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/or-pa.zip)  |    |  [1.75M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/pa-ta.zip)  |  [1.76M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/pa-te.zip) |
| ta |  [0.22M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-ta.zip)  |  [2.44M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-ta.zip)  |  [2.07M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/gu-ta.zip)  |  [2.48M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-ta.zip)  |  [2.52M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/kn-ta.zip)  |  [2.60M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ml-ta.zip)  |  [2.12M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/mr-ta.zip)  | [1.09M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/or-ta.zip)   |  [1.75M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/pa-ta.zip)  |    |  [2.61M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ta-te.zip) |
| te |  [0.21M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-te.zip)  |  [2.35M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-te.zip)  |  [2.31M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/gu-te.zip)  |  [2.42M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-te.zip)  |  [2.81M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/kn-te.zip)  |  [2.68M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ml-te.zip)  |  [2.23M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/mr-te.zip)  | [1.12M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/or-te.zip)   |  [1.76M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/pa-te.zip)  |  [2.61M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ta-te.zip)  |   | -->


### Change Log
<!-- - 06 July 2021, v0.2.1 data with metadata of source and Labse Alignment Score (LAS) was made available [here](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/samanantar_v0.2_las.zip)
- 09 June 2021, The Semantic Textual Similarity (STS) benchmark is now available for download
- 05 June 2021, The benchmarking testsets are now available for download
- 15 May 2021, The language wise splits are now available for download
- 02 May 2021, Indic-Indic v0.2 data has been updated with super strict overlap removal
- 30 April 2021, v0.2 uses super strict overlap removal of validation and test data with train data -->
- 07 May 2022 - The Aksharantar dataset is now available for download.
<!-- - 05 May 2022 - The language-wise splits are now available for download. -->


### Contributors

- Yash Madhani <sub>([AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in))</sub>
- Sushane Parthan <sub>([AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in))</sub>
- Priyanka Bedekar <sub>([AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in))</sub>
- Ruchi Khapra <sub>([AI4Bharat](https://ai4bharat.org))</sub>
- Anoop Kunchukuttan <sub>([AI4Bharat](https://ai4bharat.org), [Microsoft](https://www.microsoft.com/en-in/))</sub>
- Pratyush Kumar <sub>([AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in), [Microsoft](https://www.microsoft.com/en-in/))</sub>
- Mitesh Shantadevi Khapra <sub>([AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in))</sub>


### Citing

If you are using any of the resources, please cite the following article: 
<!-- 
```
@misc{ramesh2021samanantar,
      title={Samanantar: The Largest Publicly Available Parallel Corpora Collection for 11 Indic Languages}, 
      author={Gowtham Ramesh and Sumanth Doddapaneni and Aravinth Bheemaraj and Mayank Jobanputra and Raghavan AK and Ajitesh Sharma and Sujit Sahoo and Harshita Diddee and Mahalakshmi J and Divyanshu Kakwani and Navneet Kumar and Aswin Pradeep and Srihari Nagaraj and Kumar Deepak and Vivek Raghavan and Anoop Kunchukuttan and Pratyush Kumar and Mitesh Shantadevi Khapra},
      year={2021},
      eprint={2104.05596},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```  -->
<!-- 
The bibtex entries for the existing data sources is available [here](https://indicnlp.ai4bharat.org/papers/samanantar-existing-data.bib) -->

### License

<!-- <a rel="license" float="left" href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" width="100" />
  <img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png" style="border-style: none;" alt="CC-BY" width="100" href="http://creativecommons.org/publicdomain/zero/1.0/"/>
</a>
<br/> -->
<a rel="license" float="left" href="https://creativecommons.org/about/cclicenses/">
  <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" width="100"/>
  <img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png" style="border-style: none;" alt="CC-BY" width="100"/>
</a>

<br>
<br>


This data is released under the following licensing scheme:

- We do not own any of the text from which this data has been extracted.
- We license the actual packaging of the mined data under the [Creative Commons CC0 license (“no rights reserved”)](http://creativecommons.org/publicdomain/zero/1.0), and the Aksharantar benchmark and all manually transliterated data under the [Creative Commons CC-BY license (“no rights reserved”)](https://creativecommons.org/licenses/by/4.0/).
- To the extent possible under law, <a rel="dct:publisher" href="https://indicnlp.ai4bharat.org/samanantar/"> <span property="dct:title">AI4Bharat</span></a> has waived all copyright and related or neighboring rights to <span property="dct:title">Aksharantar</span>.
- This work is published from: India.
