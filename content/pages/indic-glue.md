---
title: "IndicGLUE"
weight: 150
url: /indic-glue
---


To thoroughly evaluate language models on Indian languages, we need a robust NLU benchmark consisting of a wide variety of tasks and covering all the Indian languages. IndicGLUE is a natural language understanding benchmark that we propose. It consists of 6 tasks which we describe in the next section.

In addition, we also compile a list of additional evaluations which comprises of challenging public tasks, but cover only some of the Indian languages.


#### Tasks

##### News Category Classification

Predict the genre of a given news article. The dataset contains around 125k news articles across 9 Indian languages. Example:

*Article Snippet*:

```
கர்நாடக சட்டப் பேரவையில் வெற்றி பெற்ற எம்எல்ஏக்கள் இன்று பதவியேற்றுக் கொண்ட நிலையில் , காங்கிரஸ் எம்எல்ஏ ஆனந்த் சிங் க்கள் ஆப்சென்ட் ஆகி அதிர்ச்சியை ஏற்படுத்தியுள்ளார் . உச்சநீதிமன்ற உத்தரவுப்படி இன்று மாலை முதலமைச்சர் எடியூரப்பா இன்று நம்பிக்கை வாக்கெடுப்பு நடத்தி பெரும்பான்மையை நிரூபிக்க உச்சநீதிமன்றம் உத்தரவிட்டது . 
```

*Category*: Politics



##### Named Entity Recognition

Recognize entities and their coarse types in a sequence of words. The dataset contains around 787k examples across 11 Indian languages.

*Example*:


|     |     |     |     |     |     |     |     |     |     |
|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| **Token** | चाणक्य | पुरी   | को   | यहाँ  | देखने  | हेतु   | यहाँ  | क्लिक | करें   |
| **Type** | B-LOC | I-LOC | O    | O    | O    | O    | O    | O    | O    |



##### Headline Prediction

 Predict the correct headline for a news article from a given list of four candidate headlines. The dataset contains around 880k examples across 11 Indian languages. Example:

*News Article:*

     ರಾಷ್ಟ್ರೀಯ\nಪುಣೆ: 23 ವರ್ಷದ ಇನ್ಫೋಸಿಸ್ ಮಹಿಳಾ ಟೆಕ್ಕಿಯೊಬ್ಬರನ್ನು ನಡು ರಸ್ತೆಯಲ್ಲಿಯೇ ಮಾರಾಕಾಸ್ತ್ರಗಳಿಂದ ಬರ್ಬರವಾಗಿ ಹತ್ಯೆ ಮಾಡಿರುವ ಘಟನೆ ಪುಣೆಯಲ್ಲಿ ಶನಿವಾರ ರಾತ್ರಿ ನಡೆದಿದೆ.\nಅಂತರ ದಾಸ್ ಕೊಲೆಯಾದ ಮಹಿಳಾ ಟೆಕ್ಕಿಯಾಗಿದ್ದಾರೆ. ಅಂತರಾ ಅವರು ಪಶ್ಚಿಮ ಬಂಗಾಳದ ಮೂಲದವರಾಗಿದ್ದಾರೆ. ಕಳೆದ ರಾತ್ರಿ 8.00 ಗಂಟೆ ಸುಮಾರಿಗೆ ಕೆಲಸ ಮುಗಿಸಿ ಮನೆಗೆ ತೆರಳುತ್ತಿದ್ದ ಸಂದರ್ಭದಲ್ಲಿ ಅಂತರಾ ಅವರ ಮೇಲೆ ದಾಳಿ ಮಾಡಿರುವ ದುಷ್ಕರ್ಮಿಗಳು ಮಾರಾಕಾಸ್ತ್ರಗಳಿಂದ ಹಲ್ಲೆ ನಡೆಸಿದ್ದಾರೆಂದು ಪೊಲೀಸರು ಹೇಳಿದ್ದಾರೆ.\nದಾಳಿ ನಡೆಸಿದ ನಂತರ ರಕ್ತದ ಮಡುವಿನಲ್ಲಿ ಬಿದ್ದು ಒದ್ದಾಡುತ್ತಿದ್ದ ಅಂತರಾ ಅವರನ್ನು ಸ್ಥಳೀಯರು ಆಸ್ಪತ್ರೆಗೆ ದಾಳಸಿದ್ದಾರೆ. ಆದರೆ, ಆಸ್ಪತ್ರೆಗೆ ದಾಖಲಿಸುವಷ್ಟರಲ್ಲಿ ಅಂತರಾ ಅವರು ಸಾವನ್ನಪ್ಪಿದ್ದಾರೆಂದು ಅವರು ಹೇಳಿದ್ದಾರೆ.\nಪ್ರಕರಣ ದಾಖಲಿಸಿಕೊಂಡಿರುವ ಪೊಲೀಸರು ತನಿಖೆ ಆರಂಭಿಸಿದ್ದಾರೆ",

* *Candidate 1*: ಇನ್ಫೋಸಿಸ್ ಮಹಿಳಾ ಟೆಕ್ಕಿಯ ಬರ್ಬರ ಹತ್ಯೆ    *[correct answer]*
* *Candidate 2:* ಮಾನಸಿಕ ಅಸ್ವಸ್ಥೆ ಮೇಲೆ  ಮಕ್ಕಳ ಕಳ್ಳಿ ಎಂದು ಭೀಕರ ಹಲ್ಲೆ
* *Candidate 3:* ಕಸಬ ಬೆಂಗ್ರೆಯಲ್ಲಿ ಮುಸುಕುಧಾರಿಗಳ ತಂಡದಿಂದ ಮೂವರು ಯುವಕರ ಮೇಲೆ ಹಲ್ಲೆ : ಓರ್ವ ಗಂಭೀರ
* *Candidate 4:* ಕಣಿವೆ ರಾಜ್ಯದಲ್ಲಿ mobile ಬಂದ್, ಪ್ರಿಂಟಿಂಗ್ ಪ್ರೆಸ್ ಮೇಲೆ ದಾಳಿ



##### Wikipedia Section Title Prediction

Predict the correct title for a Wikipedia section from a given list of four candidate titles. The dataset has 400k examples across 11 Indian languages.

*Section Text*:

```
2005માં, જેકમેન નિર્માણ કંપની, સીડ પ્રોડકશન્સ ઊભી કરવા તેના લાંબાસમયના મદદનીશ જહોન પાલેર્મો સાથે જોડાયા, જેમનો પ્રથમ પ્રોજેકટ 2007માં વિવા લાફલિન હતો. જેકમેનની અભિનેત્રી પત્ની ડેબોરા-લી ફર્નેસ પણ કંપનીમાં જોડાઈ, અને પાલેર્મોએ પોતાના, ફર્નેસ અને જેકમેન માટે “ યુનિટી ” અર્થવાળા લખાણની આ ત્રણ વીંટીઓ બનાવી.[૨૭] ત્રણેયના સહયોગ અંગે જેકમેને જણાવ્યું કે “ મારી જિંદગીમાં જેમની સાથે મેં કામ કર્યું તે ભાગીદારો અંગે ડેબ અને જહોન પાલેર્મો અંગે હું ખૂબ નસીબદાર છું. ખરેખર તેથી કામ થયું. અમારી પાસે જુદું જુદું સાર્મથ્ય હતું. હું તે પસંદ કરતો હતો. I love it. તે ખૂબ ઉત્તેજક છે. ”[૨૮]ફોકસ આધારિત સીડ લેબલ, આમન્ડા સ્કિવેઈટઝર, કેથરિન ટેમ્બલિન, એલન મંડેલબમ અને જોય મરિનો તેમજ સાથે સિડની આધારિત નિર્માણ કચેરીનું સંચાલન કરનાર અલાના ફ્રીનો સમાવેશ થતાં કદમાં વિસ્તૃત બની. આ કંપીનોનો ઉદ્દેશ જેકમેનના વતનના દેશની સ્થાનિક પ્રતિભાને કામે લેવા મધ્યમ બજેટવાળી ફિલ્મો બનાવવાનો છે. 
```

* *Candidate 1:* એકસ-મેન
* *Candidate 2:* કારકીર્દિ
* *Candidate 3:* નિર્માણ કંપન [*correct answer*]
* *Candidate 4:* ઓસ્ટ્રેલિય



##### Cloze-style Question Answering

Given a text with an entity randomly masked, the task is to predict that masked entity from a list of 4 candidate entities. The dataset contains around 239k examples across 11 languages. Example:

*Text*

```
ਹੋਮੀ ਭਾਬਾ ਦਾ ਜਨਮ 1949 ਈ ਨੂਂ ਮੁੰਬਈ ਵਿੱਚ ਪਾਰਸੀ ਪਰਿਵਾਰ ਵਿੱਚ ਹੋਇਆ । ਸੇਂਟ ਮੇਰੀ ਤੋਂ ਮੁਢਲੀ ਸਿਖਿਆ ਪ੍ਰਾਪਤ ਕਰਕੇ ਉਹ ਬੰਬੇ ਯੂਨੀਵਰਸਿਟੀ ਗ੍ਰੈਜੁਏਸ਼ਨ ਲਈ ਚਲਾ ਗਿਆ । ਇਸ ਤੋਂ ਬਾਅਦ ਉਹ ਉਚੇਰੀ ਸਿਖਿਆ ਲਈ <MASK> ਚਲਾ ਗਿਆ । ਉਸਨੇ ਓਥੇ ਆਕਸਫੋਰਡ ਯੂਨੀਵਰਸਿਟੀ ਤੋਂ ਐਮ.ਏ ਅਤੇ ਐਮ ਫਿਲ ਦੀਆਂ ਡਿਗਰੀਆਂ ਪ੍ਰਾਪਤ ਕੀਤੀਆਂ । ਤਕਰੀਬਨ ਦਸ ਸਾਲ ਤਕ ਉਸਨੇ ਸੁਸੈਕਸ ਯੂਨੀਵਰਸਿਟੀ ਦੇ ਅੰਗਰੇਜ਼ੀ ਵਿਭਾਗ ਵਿੱਚ ਬਤੌਰ ਲੈਕਚਰਾਰ ਕਾਰਜ ਨਿਭਾਇਆ । ਇਸਤੋਂ ਇਲਾਵਾ ਹੋਮੀ ਭਾਬਾ ਪੈਨਸੁਲਵੇਨਿਆ , ਸ਼ਿਕਾਗੋ ਅਤੇ ਅਮਰੀਕਾ ਦੀ ਹਾਰਵਰਡ ਯੂਨੀਵਰਸਿਟੀ ਵਿੱਚ ਵੀ ਪ੍ਰੋਫ਼ੇਸਰ ਦੇ ਆਹੁਦੇ ਤੇ ਰਿਹਾ ।
```

* *Candidate 1*: ਬਰਤਾਨੀਆ *[correct answer]*
* *Candidate 2*: ਭਾਰਤ
* *Candidate 3*: ਸ਼ਿਕਾਗੋ
* *Candidate 4*: ਪਾਕਿਸਤਾਨ



##### Cross-lingual Sentence Retrieval

Given a sentence in language $L_1$ the task is to retrieve its translation from a set of candidate sentences in language $L_2$. The dataset contains around 39k parallel sentence pairs across 8 Indian languages. Example:

*Input Sentence*

```
In the health sector the nation has now moved ahead from the conventional approach.
```

*Retrieve the following translation from a set of 4886 sentences:*

```
ആരോഗ്യമേഖലയില് ഇന്ന് രാജ്യം പരമ്പരാഗത രീതികളില് നിന്ന് മുന്നേറിക്കഴിഞ്ഞു.
```



#### Additional Evaluation Tasks

##### Natural Language Inference

- Winnograd Natural Language Inference (WNLI)
- Choice of Plausible Alternatives (COPA)

##### Sentiment Analysis

- IITP Movie Reviews Sentiment 
- IITP Product Reviews
- ACTSA Sentiment Classifcation

##### Genre Classification

- Soham Articles Genre Classification
- iNLTK Headlines Genre Classifcation
- BBC News Articles

##### Discourse Analysis

* MIDAS Discourse


##### Paraphrase Detection

* Amrita Exact Paraphrase Detection
* Amrita Rough Paraphrase Detection


#### Downloads

*A script to download the dataset will soon be provided*