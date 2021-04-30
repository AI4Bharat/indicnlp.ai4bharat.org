---
title: "IndicTrans"
weight: 200
toc: true
url: /indic-trans
---
<!-- <a href="https://huggingface.co/ai4bharat/indic-trans"><img alt="Doc" src="https://img.shields.io/static/v1?url=https%3A%2F%2Fhuggingface.co%2Fai4bharat%2Findic-bert&label=Huggingface&color=green&message=indic-trans&logo=huggingface"></a> -->
  

IndicTrans is a Transformer-4X model trained on samanantar dataset. Two models are available which can translate from Indic to English and English to Indic. The model can perform translations for 11 lanaguages: Assamese, Bengali, Gujarati, Hindi, Kannada, Malayalam, Marathi, Oriya, Punjabi, Tamil, Telugu.

### Update 30-04-2021

The models are now available for download

<!-- ### Download

For downloading and usage instructions please follow the [IndicTrans](https://github.com/AI4Bharat/indicTrans) Repository -->

### Download Model

- Indic-English model can be downloaded from [here](https://akpublicdata.blob.core.windows.net/indicnlp/indictrans/indictrans-indic-en-v0.2.zip)
- English-Indic model can be downloaded from [here](https://akpublicdata.blob.core.windows.net/indicnlp/indictrans/inidctrans-en-indic-v0.2.zip)

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
| en-bn       | 8.52M             |
| en-gu       | 3.05M             |
| en-hi       | 8.56M             |
| en-kn       | 4.07M             |
| en-ml       | 5.85M             |
| en-mr       | 3.32M             |
| en-or       | 1.00M             |
| en-pa       | 2.42M             |
| en-ta       | 5.16M             |
| en-te       | 4.82M             |


In total, the training data has 46.9M sentence pairs.


### Benchmarking

We evaluate IndicTrans model on a WAT2021, WAT2020, WMT, UFAL, PMI. Here are the results that we obtain:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-cly1{text-align:left;vertical-align:middle}
.tg .tg-wa1i{font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-amwm{font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-nrix{text-align:center;vertical-align:middle}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-cly1"></th>
    <th class="tg-wa1i" colspan="10"><span style="font-weight:bold">WAT2021</span></th>
    <th class="tg-wa1i" colspan="7"><span style="font-weight:bold">WAT2020</span></th>
    <th class="tg-wa1i" colspan="3"><span style="font-weight:bold">WMT</span></th>
    <th class="tg-wa1i"><span style="font-weight:bold">UFAL</span></th>
    <th class="tg-wa1i"><span style="font-weight:bold">pmi</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-wa1i"></td>
    <td class="tg-wa1i"><span style="font-weight:bold">bn</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">gu</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">hi</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">kn</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">ml</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">mr</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">or</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">pa</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">ta</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">te</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">bn</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">gu</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">hi</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">ml</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">mr</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">ta</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">te</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">hi</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">gu</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">ta</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">ta</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">as</span></td>
  </tr>
  <tr>
    <td class="tg-amwm">IN-EN</td>
    <td class="tg-wa1i"><span style="font-weight:bold">33.7</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">43.4</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">46.9</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">38.3</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">36.9</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">36.</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">36.6</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">46.</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">35.4</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">38.3</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">23.1</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">27.1</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">27.1</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">21.4</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">22.8</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">20.1</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">19.8</span></td>
    <td class="tg-nrix">28.6</td>
    <td class="tg-nrix">20.8</td>
    <td class="tg-nrix">23.2</td>
    <td class="tg-nrix">30.3</td>
    <td class="tg-wa1i"><span style="font-weight:bold">34.8</span></td>
  </tr>
  <tr>
    <td class="tg-0lax"><span style="font-weight:bold">EN-IN</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">16.</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">25.3</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">38.8</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">18.9</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">14.1</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">19.5</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">18.1</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">32.</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">13.9</span></td>
    <td class="tg-wa1i">13.7</td>
    <td class="tg-wa1i"><span style="font-weight:bold">11.8</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">15.7</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">20.7</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">7.1</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">12.9</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">6.5</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">7.5</span></td>
    <td class="tg-wa1i"><span style="font-weight:bold">25.</span></td>
    <td class="tg-nrix">15.8</td>
    <td class="tg-nrix">8.5</td>
    <td class="tg-nrix">11.3</td>
    <td class="tg-wa1i"><span style="font-weight:bold">12.5</span></td>
  </tr>
</tbody>
</table>



