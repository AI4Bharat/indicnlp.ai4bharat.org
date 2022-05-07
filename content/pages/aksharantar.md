---
title: "Aksharantar"
weight: 25
toc: true
url: /aksharantar
---
  

Aksharantar is the largest publicly available transliteration dataset for 21 Indic languages. The corpus has 26M Indic language-English transliteration pairs.

### Downloads

- The Aksharantar dataset can be downloaded  from the [Aksharantar Hugging Face repository](https://huggingface.co/datasets/ai4bharat/Aksharantar/tree/main).
- Each language-pair corpus in the Aksharantar dataset is split into training, validation and test subsets. Each subset is a JSONL file consisting of individual data instances comprising a unique identifier, native word, English word, transliteration source and a score (if applicable).
- Individual language-pair download links are provided in the [data split](https://github.com/SushaneP/indicnlp.ai4bharat.org/edit/master/content/pages/aksharantar.md#data-split) below.


### Data Split

The language-wise splits for Aksharantar is shown in the table with total number of word pairs (in millions). Individual download links for each language-pair are as against the hyperlink.

| Subset | [as-en <sub>(4.72 MB)</sub>](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/asm.zip) | [bn-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/ben.zip) <sub>(31.5 MB)</sub> | [brx-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/brx.zip) <sub>(0.933 MB)</sub> | [gu-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/guj.zip) <sub>(29.5 MB)</sub> | [hi-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/hin.zip) <sub>(31.4 MB)</sub> | [kn-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/kan.zip) <sub>(83.7 MB)</sub> | [ks-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/kas.zip) <sub>(1.1 MB)</sub> | [kok-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/kok.zip) <sub>(16.6 MB)</sub> | [mai-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/mai.zip) <sub>(6.74 MB)</sub> | [ml-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/mal.zip) <sub>(125 MB)</sub> | [mni-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/mni.zip) <sub>(0.313 MB)</sub> | [mr-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/mar.zip) <sub>(39.9 MB)</sub> | [ne-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/nep.zip) <sub>(67 MB)</sub> | [or-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/ori.zip) <sub>(9.09 MB)</sub> | [pa-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/pan.zip) <sub>(12.1 MB)</sub> | [sa-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/san.zip) <sub>(56 MB)</sub> | [sd-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/sid.zip) <sub>(1.37 MB)</sub> | [ta-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/tam.zip) <sub>(92.7 MB)</sub> | [te-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/tel.zip) <sub>(69.1 MB)</sub> | [ur-en](https://huggingface.co/datasets/ai4bharat/Aksharantar/blob/main/urd.zip) <sub>(17 MB)</sub> |
|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| Training | 179K | 1231K | 36K | 1143K | 1299K | 2907K | 47K | 613K | 283K | 4101K | 10K | 1453K | 2397K | 346K | 515K | 1813K | 60K | 3231K | 2430K | 699K |
| Validation | 4K | 11K | 3K | 12K | 6K | 7K | 4K | 4K | 4K | 8K | 3K | 8K | 3K | 3K | 9K | 3K | 8K | 9K | 8K | 12K |
| Test | 5531 | 5009 | 4136 | 7768 | 5693 | 6396 | 7707 | 5093 | 5512 | 6911 | 4925 | 6573 | 4133 | 4256 | 4316 | 5334 | - | 4682 | 4567 | 4463 |

### Change Log
- 07 May 2022 - The Aksharantar dataset is now available for download.


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

```
@misc{madhani2022aksharantar,
      title={Aksharantar: Towards Building Open Transliteration Tools for the Next Billion Users}, 
      author={Yash Madhani and Sushane Parthan and Priyanka Bedekar and Ruchi Khapra and Anoop Kunchukuttan and Pratyush Kumar and Mitesh Shantadevi Khapra},
      year={2022},
      eprint={},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

<!-- 
The bibtex entries for the existing data sources is available [here](https://indicnlp.ai4bharat.org/papers/samanantar-existing-data.bib) -->

### License

<!-- <a rel="license" float="left" href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" width="100" />
  <img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png" style="border-style: none;" alt="CC-BY" width="100" href="http://creativecommons.org/publicdomain/zero/1.0/"/>
</a>
<br/> -->


This data is released under the following licensing scheme:

- Manually collected data: Released under CC-BY license. 
- Mined dataset (from Samanantar and IndicCorp): Released under CC0 license. 
- Existing sources: Released under CC0 license. 

**CC-BY License**

<a rel="license" float="left" href="https://creativecommons.org/about/cclicenses/">
  <img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png" style="border-style: none;" alt="CC-BY" width="100"/>
</a>

<br>
<br>
<!-- 
and the Aksharantar benchmark and all manually transliterated data under the [Creative Commons CC-BY license (“no rights reserved”)](https://creativecommons.org/licenses/by/4.0/). -->


**CC0 License Statement**

<a rel="license" float="left" href="https://creativecommons.org/about/cclicenses/">
  <img src="https://licensebuttons.net/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" width="100"/>
</a>

<br>
<br>

- We do not own any of the text from which this data has been extracted.
- We license the actual packaging of the mined data under the [Creative Commons CC0 license (“no rights reserved”)](http://creativecommons.org/publicdomain/zero/1.0).
- To the extent possible under law, <a rel="dct:publisher" href="https://indicnlp.ai4bharat.org/aksharantar/"> <span property="dct:title">AI4Bharat</span></a> has waived all copyright and related or neighboring rights to <span property="dct:title">Aksharantar</span> manually collected data and existing sources.
- This work is published from: India.