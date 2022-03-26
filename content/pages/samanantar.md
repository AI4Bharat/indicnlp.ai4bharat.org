---
title: "Samanantar"
weight: 20
toc: true
url: /samanantar
---
  

Samanantar is the largest publicly available parallel corpora collection for Indic languages: Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu. The corpus has 49.6M sentence pairs between English to Indian Languages.

### Update 04-11-2021
Samanantar v0.3 along with LaBSE scores metadata is available for download. Go to [Downloads](#downloads)

### Dataset Format

The [publicly released version](#downloads) is randomly shuffled, untokenized, and deduplicated.

## Downloads

### Benchmarks

The testsets used to benchmark IndicTrans can be found [here](https://storage.googleapis.com/samanantar-public/benchmarks.zip)

### STS Benchmark

The Semantic Textual Similarity (STS) benchmark can be downloaded from [here](https://storage.googleapis.com/samanantar-public/human_annotations.tsv)

### En-Indic

<!-- The entire dataset can be downloaded from [here](https://storage.googleapis.com/samanantar-public/data/all-without-supara.zip) -->

The entire dataset can be downloaded from [Samanantar v0.3](https://storage.googleapis.com/samanantar-public/V0.3/source_wise_splits.zip). 

The folder has 2 directories 
- existing - all existing data compiled before samanantar 
- created - mined as part of samanantar
- We have separate sub-dir for each source 

### Mirror Links

- Please use this mirror [gdrive](https://drive.google.com/file/d/1xrD9bL78mbxpp-DdOw1EHhz1nzin_6dX/view?usp=sharing) link to download the v0.3 data 


The language wise splits for **Samanantar v0.2** can be found in the table below.  Each link contains the number of sentence pairs in millions.

| Language Pair | Link     |
| -------- | -------- |
| en-as <sub>(9 MB)</sub>       | [0.14M](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/en-as.zip) |
| en-bn <sub>(580 MB)</sub>       | [8.52M](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/en-bn.zip) |
| en-gu  <sub>(178 MB)</sub>      | [3.05M](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/en-gu.zip) |
| en-hi  <sub>(818 MB)</sub>     | [8.56M](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/en-hi.zip) |
| en-kn   <sub>(229 MB)</sub>     | [4.07M](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/en-kn.zip) |
| en-ml  <sub>(365 MB)</sub>      | [5.85M](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/en-ml.zip) |
| en-mr  <sub>(210 MB)</sub>     | [3.32M](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/en-mr.zip) |
| en-or  <sub>(65 MB)</sub>      | [1.00M](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/en-or.zip) |
| en-pa   <sub>(175 MB)</sub>     | [2.42M](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/en-pa.zip) |
| en-ta  <sub>(350 MB)</sub>      |  [5.16M](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/en-ta.zip) |
| en-te   <sub>(280 MB)</sub>    | [4.82M](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/en-te.zip) |


#### Indic-Indic

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
| te |  [0.21M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/as-te.zip)  |  [2.35M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/bn-te.zip)  |  [2.31M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/gu-te.zip)  |  [2.42M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/hi-te.zip)  |  [2.81M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/kn-te.zip)  |  [2.68M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ml-te.zip)  |  [2.23M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/mr-te.zip)  | [1.12M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/or-te.zip)   |  [1.76M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/pa-te.zip)  |  [2.61M](https://storage.googleapis.com/samanantar-public/V0.2/data/indic2indic/ta-te.zip)  |   |


### Change Log
- 06 July 2021, v0.2.1 data with metadata of source and Labse Alignment Score (LAS) was made available [here](https://storage.googleapis.com/samanantar-public/V0.2/data/en2indic/samanantar_v0.2_las.zip)
- 09 June 2021, The Semantic Textual Similarity (STS) benchmark is now available for download
- 05 June 2021, The benchmarking testsets are now available for download
- 15 May 2021, The language wise splits are now available for download
- 02 May 2021, Indic-Indic v0.2 data has been updated with super strict overlap removal
- 30 April 2021, v0.2 uses super strict overlap removal of validation and test data with train data


### Contributors

- Gowtham Ramesh, <sub>([RBCDSAI](https://rbcdsai.iitm.ac.in), [IITM](https://www.iitm.ac.in))</sub>
- Sumanth Doddapaneni, <sub>([RBCDSAI](https://rbcdsai.iitm.ac.in), [IITM](https://www.iitm.ac.in))</sub>
- Aravinth Bheemaraj, <sub>([Tarento](https://www.linkedin.com/company/tarento-group/), [EkStep](https://ekstep.in))</sub>
- Mayank Jobanputra, <sub>([IITM](https://www.iitm.ac.in))</sub>
- Raghavan AK, <sub>([AI4Bharat](https://ai4bharat.org))</sub>
- Ajitesh Sharma, <sub>([Tarento](https://www.linkedin.com/company/tarento-group/), [EkStep](https://ekstep.in))</sub>
- Sujit Sahoo, <sub>([Tarento](https://www.linkedin.com/company/tarento-group/), [EkStep](https://ekstep.in))</sub>
- Harshita Diddee, <sub>([AI4Bharat](https://ai4bharat.org))</sub>
- Mahalakshmi J, <sub>([AI4Bharat](https://ai4bharat.org))</sub>
- Divyanshu Kakwani, <sub>([IITM](https://www.iitm.ac.in), [AI4Bharat](https://ai4bharat.org))</sub>
- Navneet Kumar, <sub>([Tarento](https://www.linkedin.com/company/tarento-group/), [EkStep](https://ekstep.in))</sub>
- Aswin Pradeep, <sub>([Tarento](https://www.linkedin.com/company/tarento-group/), [EkStep](https://ekstep.in))</sub>
- Srihari Nagaraj, <sub>([Tarento](https://www.linkedin.com/company/tarento-group/), [EkStep](https://ekstep.in))</sub>
- Kumar Deepak, <sub>([Tarento](https://www.linkedin.com/company/tarento-group/), [EkStep](https://ekstep.in))</sub>
- Vivek Raghavan, <sub>([EkStep](https://ekstep.in))</sub>
- Anoop Kunchukuttan, <sub>([Microsoft](https://www.microsoft.com/en-in/), [AI4Bharat](https://ai4bharat.org))</sub>
- Pratyush Kumar, <sub>([RBCDSAI](https://rbcdsai.iitm.ac.in), [AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in))</sub>
- Mitesh Shantadevi Khapra, <sub>([RBCDSAI](https://rbcdsai.iitm.ac.in), [AI4Bharat](https://ai4bharat.org), [IITM](https://www.iitm.ac.in))</sub>


### Citing

If you are using any of the resources, please cite the following article: 

```
@misc{ramesh2021samanantar,
      title={Samanantar: The Largest Publicly Available Parallel Corpora Collection for 11 Indic Languages}, 
      author={Gowtham Ramesh and Sumanth Doddapaneni and Aravinth Bheemaraj and Mayank Jobanputra and Raghavan AK and Ajitesh Sharma and Sujit Sahoo and Harshita Diddee and Mahalakshmi J and Divyanshu Kakwani and Navneet Kumar and Aswin Pradeep and Srihari Nagaraj and Kumar Deepak and Vivek Raghavan and Anoop Kunchukuttan and Pratyush Kumar and Mitesh Shantadevi Khapra},
      year={2021},
      eprint={2104.05596},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
``` 

The bibtex entries for the existing data sources is available [here](https://indicnlp.ai4bharat.org/papers/samanantar-existing-data.bib)

### License

<a rel="license"
  href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
</a>
<br />

This data is released under this licensing scheme:

- We do not own any of the text from which this data has been extracted.
- We license the actual packaging of this data under the [Creative Commons CC0 license (“no rights reserved”)](http://creativecommons.org/publicdomain/zero/1.0).
- To the extent possible under law,
  <a rel="dct:publisher"
     href="https://indicnlp.ai4bharat.org/samanantar/">
    <span property="dct:title">AI4Bharat</span></a>
  has waived all copyright and related or neighboring rights to
  <span property="dct:title">Samanantar</span>
- This work is published from: India. 