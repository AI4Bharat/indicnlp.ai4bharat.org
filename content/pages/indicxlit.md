---
title: "IndicXlit"
weight: 30
toc: true
url: /indic-xlit
---

IndicXlit is a Transformer-based multilingual transliteration model (with ~11M parameters) for romanised to Indic script conversion, supporting 20 languages from the Indian subcontinent.

<!-- 
### Update 05-06-2021

The Indic-Indic model is now available for download

### Update 30-04-2021

The models are now available for download
 -->
<!-- ### Download

For downloading and usage instructions please follow the [IndicTrans](https://github.com/AI4Bharat/indicTrans) Repository -->

### Download Model

- English-Indic transliteration model can be downloaded [here](https://storage.googleapis.com/indic-xlit-public/final_model/indicxlit-en-indic-v1.0.zip).

### Mirror Links

- Please use this mirror [Google Drive]() link to download the IndicXlit model.

### Usage

All information and instructions pertaining to using the IndicXlit model can be found on the [IndicXlit](https://github.com/AI4Bharat/IndicXlit) GitHub repository.

<!--
### Usage

The easiest way to use IndicTrans is through the Huggingface transformers library. It can be simply loaded like this:

```python
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('ai4bharat/indic-trans')
model = AutoModel.from_pretrained('ai4bharat/indic-trans') 
``` -->

### Model Details

IndicXlit is trained on Aksharantar dataset which covers 21 language pairs. The volume of training, validation and test splits for each language pair is as listed below:

| Subset | as-en | bn-en | brx-en | gu-en | hi-en | kn-en | ks-en | kok-en | mai-en | ml-en | mni-en | mr-en | ne-en | or-en | pa-en | san-en | sd-en | ta-en | te-en | ur-en |
|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|
| Training | 179K | 1231K | 36K | 1143K | 1299K | 2907K | 47K | 613K | 283K | 4101K | 10K | 1453K | 2397K | 346K | 515K | 1813K | 60K | 3231K | 2430K | 699K |
| Validation | 4K | 11K | 3K | 12K | 6K | 7K | 4K | 4K | 4K | 8K | 3K | 8K | 3K | 3K | 9K | 3K | 8K | 9K | 8K | 12K |
| Test | 5531 | 5009 | 4136 | 7768 | 5693 | 6396 | 7707 | 5093 | 5512 | 6911 | 4925 | 6573 | 4133 | 4256 | 4316 | 5334 | - | 4682 | 4567 | 4463 |

<!-- | Language Pair | \# Sentence Pairs |
| -------- | ----------------- |
| as-en | aM |
| bn-en | bM |
| brx-en | b2M |
| gu-en | cM |
| hi-en | dM |
| kn-en | eM |
| ks-en | e2M |
| kok-en | e3M |
| mai-en | e3M |
| ml-en | fM |
| mni-en | f2M |
| mr-en | gM |
| ne-en | g2M |
| or-en | hM |
| pa-en | iM |
| san-en | i2M |
| sd-en | i3M |
| si-en | i4M |
| ta-en | jM |
| te-en | kM |
| ur-en | k2M |
 -->

In total, the Aksharantar dataset contains ~26M word pairs.

### Benchmarking

We evaluate IndicXlit model on the Dakshina testset and compare our results with the Dakshina paper. Results are as mentioned:

<table class="tg">
<!-- <thead>
  <tr>
    <th class="tg-9wq8"></th>
    <th class="tg-9wq8" colspan="10">WAT2021</th>
    <th class="tg-9wq8" colspan="7">WAT2020</th>
    <th class="tg-9wq8" colspan="3">WMT</th>
    <th class="tg-9wq8">UFAL</th>
    <th class="tg-9wq8">pmi</th>
  </tr>
</thead> -->
<thead>
  <tr>
    <td class="tg-9wq8">Language</td>
    <td class="tg-9wq8">bn</td>
    <td class="tg-9wq8">gu</td>
    <td class="tg-9wq8">hi</td>
    <td class="tg-9wq8">kn</td>
    <td class="tg-9wq8">ml</td>
    <td class="tg-9wq8">mr</td>
    <td class="tg-9wq8">pa</td>
    <td class="tg-9wq8">sd</td>
    <td class="tg-9wq8">si</td>
    <td class="tg-9wq8">ta</td>
    <td class="tg-9wq8">te</td>
    <td class="tg-9wq8">urd</td>
    <td class="tg-9wq8">Avg</td>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-9wq8">Dakshina</td>
    <td class="tg-9wq8">49.40</td>
    <td class="tg-9wq8">49.50</td>
    <td class="tg-9wq8">50.00</td>
    <td class="tg-9wq8">66.20</td>
    <td class="tg-9wq8">58.30</td>
    <td class="tg-9wq8">49.70</td>
    <td class="tg-9wq8">40.90</td>
    <td class="tg-9wq8">33.20</td>
    <td class="tg-9wq8">54.70</td>
    <td class="tg-9wq8">65.70</td>
    <td class="tg-9wq8">67.60</td>
    <td class="tg-9wq8">36.70</td>
    <td class="tg-9wq8">51.83</td>
  </tr>
  <tr>
    <td class="tg-9wq8">IndicXlit</td>
    <td class="tg-9wq8">55.49</td>
    <td class="tg-9wq8">62.02</td>
    <td class="tg-9wq8">60.56</td>
    <td class="tg-9wq8">77.18</td>
    <td class="tg-9wq8">63.56</td>
    <td class="tg-9wq8">64.85</td>
    <td class="tg-9wq8">47.24</td>
    <td class="tg-9wq8">48.56</td>
    <td class="tg-9wq8">63.91</td>
    <td class="tg-9wq8">68.10</td>
    <td class="tg-9wq8">73.38</td>
    <td class="tg-9wq8">42.12</td>
    <td class="tg-9wq8">60.58</td>
  </tr>
</tbody>
</table>

### License 

The IndicXlit [code](https://github.com/AI4Bharat/IndicXlit) and [model](https://github.com/AI4Bharat/IndicXlit#download-indicxlit-model) are released under the MIT License.
