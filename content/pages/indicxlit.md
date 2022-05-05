---
title: "IndicXlit"
weight: 30
toc: true
url: /indic-xlit
---

IndicXlit is a Transformer model for transliteration from romanized input to native Indic language script supporting 20 languages from the Indian subcontinent.

<!-- 
### Update 05-06-2021

The Indic-Indic model is now available for download

### Update 30-04-2021

The models are now available for download
 -->
<!-- ### Download

For downloading and usage instructions please follow the [IndicTrans](https://github.com/AI4Bharat/indicTrans) Repository -->

### Download Model

- English-Indic transliteration model can be downloaded [here]().

### Mirror Links

- Please use this mirror [Google Drive]() link to download the IndicXlit model.

### Usage

The instructions for running inference can be found on the [IndicXlit]() GitHub repository.

<!--
### Usage

The easiest way to use IndicTrans is through the Huggingface transformers library. It can be simply loaded like this:

```python
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('ai4bharat/indic-trans')
model = AutoModel.from_pretrained('ai4bharat/indic-trans') 
``` -->

### Model Details

IndicXlit is trained on Aksharantar dataset which covers 21 language pairs. The volume of pretraining data for each language pair is as listed below:

| Language Pair | \# Sentence Pairs |
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


In total, the training data has X.YM sentence pairs.

### Benchmarking

We evaluate IndicTrans model on a WAT2021, WAT2020, WMT, UFAL, PMI. Here are the results that we obtain:

<!-- <style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal}
.tg .tg-9wq8{border-color:inherit;text-align:center;vertical-align:middle}
</style> -->
<table class="tg">
<thead>
  <tr>
    <th class="tg-9wq8"></th>
    <th class="tg-9wq8" colspan="10">WAT2021</th>
    <th class="tg-9wq8" colspan="7">WAT2020</th>
    <th class="tg-9wq8" colspan="3">WMT</th>
    <th class="tg-9wq8">UFAL</th>
    <th class="tg-9wq8">pmi</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-9wq8"></td>
    <td class="tg-9wq8">bn</td>
    <td class="tg-9wq8">gu</td>
    <td class="tg-9wq8">hi</td>
    <td class="tg-9wq8">kn</td>
    <td class="tg-9wq8">ml</td>
    <td class="tg-9wq8">mr</td>
    <td class="tg-9wq8">or</td>
    <td class="tg-9wq8">pa</td>
    <td class="tg-9wq8">ta</td>
    <td class="tg-9wq8">te</td>
    <td class="tg-9wq8">bn</td>
    <td class="tg-9wq8">gu</td>
    <td class="tg-9wq8">hi</td>
    <td class="tg-9wq8">ml</td>
    <td class="tg-9wq8">mr</td>
    <td class="tg-9wq8">ta</td>
    <td class="tg-9wq8">te</td>
    <td class="tg-9wq8">hi</td>
    <td class="tg-9wq8">gu</td>
    <td class="tg-9wq8">ta</td>
    <td class="tg-9wq8">ta</td>
    <td class="tg-9wq8">as</td>
  </tr>
  <tr>
    <td class="tg-9wq8">IN-EN</td>
    <td class="tg-9wq8">28.4</td>
    <td class="tg-9wq8">39.5</td>
    <td class="tg-9wq8">43.2</td>
    <td class="tg-9wq8">34.9</td>
    <td class="tg-9wq8">33.4</td>
    <td class="tg-9wq8">32.4</td>
    <td class="tg-9wq8">33.4</td>
    <td class="tg-9wq8">42.</td>
    <td class="tg-9wq8">32.</td>
    <td class="tg-9wq8">35.1</td>
    <td class="tg-9wq8">19.2</td>
    <td class="tg-9wq8">23.</td>
    <td class="tg-9wq8">23.5</td>
    <td class="tg-9wq8">19.6</td>
    <td class="tg-9wq8">19.6</td>
    <td class="tg-9wq8">17.9</td>
    <td class="tg-9wq8">17.8</td>
    <td class="tg-9wq8">29.4</td>
    <td class="tg-9wq8">23.4</td>
    <td class="tg-9wq8">24.3</td>
    <td class="tg-9wq8">30.1</td>
    <td class="tg-9wq8">28.7</td>
  </tr>
  <tr>
    <td class="tg-9wq8">EN-IN</td>
    <td class="tg-9wq8">14.7</td>
    <td class="tg-9wq8">24.8</td>
    <td class="tg-9wq8">37.9</td>
    <td class="tg-9wq8">18.2</td>
    <td class="tg-9wq8">14.4</td>
    <td class="tg-9wq8">19.2</td>
    <td class="tg-9wq8">18.5</td>
    <td class="tg-9wq8">31.4</td>
    <td class="tg-9wq8">13.3</td>
    <td class="tg-9wq8">13.2</td>
    <td class="tg-9wq8">10.2</td>
    <td class="tg-9wq8">14.6</td>
    <td class="tg-9wq8">19.4</td>
    <td class="tg-9wq8">6.9</td>
    <td class="tg-9wq8">12.5</td>
    <td class="tg-9wq8">5.8</td>
    <td class="tg-9wq8">7.2</td>
    <td class="tg-9wq8">25.</td>
    <td class="tg-9wq8">16.2</td>
    <td class="tg-9wq8">8.8</td>
    <td class="tg-9wq8">11.6</td>
    <td class="tg-9wq8">12</td>
  </tr>
</tbody>
</table>

### License 

The IndicXlit [code]() and [model](https://github.com/AI4Bharat/indicTrans#download-indictrans-models) are released under the MIT License.
