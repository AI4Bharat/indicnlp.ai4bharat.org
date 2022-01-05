---
title: "IndicTrans"
weight: 210
toc: true
url: /indic-trans
---
<!-- <a href="https://huggingface.co/ai4bharat/indic-trans"><img alt="Doc" src="https://img.shields.io/static/v1?url=https%3A%2F%2Fhuggingface.co%2Fai4bharat%2Findic-bert&label=Huggingface&color=green&message=indic-trans&logo=huggingface"></a> -->
  

IndicTrans is a Transformer-4X model trained on samanantar dataset. Two models are available which can translate from Indic to English and English to Indic. The model can perform translations for 11 lanaguages: Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu.

### Update 05-06-2021

The Indic-Indic model is now available for download

### Update 30-04-2021

The models are now available for download

<!-- ### Download

For downloading and usage instructions please follow the [IndicTrans](https://github.com/AI4Bharat/indicTrans) Repository -->

### Download Model

- Indic-English model can be downloaded from [here](https://storage.googleapis.com/samanantar-public/V0.3/models/indic-en.zip)
- English-Indic model can be downloaded from [here](https://storage.googleapis.com/samanantar-public/V0.3/models/en-indic.zip)
- Indic-Indic can be downloaded from [here](https://storage.googleapis.com/samanantar-public/V0.3/models/m2m.zip)

### Mirror Links

- Please use this mirror [gdrive](https://drive.google.com/drive/folders/1bfF2m1UzzNe_M9SB6M60BfQeTsx4zq5j?usp=sharing) link to download the models 

### Usage

The instructions for running inference can be found at [IndicTrans](https://github.com/AI4Bharat/indicTrans.git) GitHub repository 

<!--
### Usage

The easiest way to use IndicTrans is through the Huggingface transformers library. It can be simply loaded like this:

```python
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('ai4bharat/indic-trans')
model = AutoModel.from_pretrained('ai4bharat/indic-trans') 
``` -->


### Model Details

IndicTrans is trained with Samanantar dataset which covers 11 language pairs.The amount of pretraining data for each language pair is listed below:

| Language Pair | \# Sentence Pairs   |
| -------- | ----------------- |
| en-as       | 0.14M             |
| en-bn       | 8.6M             |
| en-gu       | 3.06M             |
| en-hi       | 10.13M             |
| en-kn       | 4.09M             |
| en-ml       | 5.92M             |
| en-mr       | 3.63M             |
| en-or       | 1.00M             |
| en-pa       | 2.98M             |
| en-ta       | 5.26M             |
| en-te       | 4.95M             |


In total, the training data has 49.7M sentence pairs.


### Benchmarking

We evaluate IndicTrans model on a WAT2021, WAT2020, WMT, UFAL, PMI. Here are the results that we obtain:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-9wq8{border-color:inherit;text-align:center;vertical-align:middle}
</style>
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



