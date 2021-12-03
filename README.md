# Gender Bias in Movie Plots based on geographical locations

Movies are a simulation of society. They mirror the issues, problems, thinking and perception of the contemporary world we live in. Therefore, in any society, movies act as a strong medium to understand how prevalent gender bias and stereotypes are. Gender bias can be defined as dominance, in particular contexts (for example, in occupations or among primary social roles), of one gender over the other. As a consequence, the less dominant gender is underrepresented and stereotypes appear. This can be seen in movies as well, for example, characters like nurses tend to be female and doctors tend to be male. Also, more often than not, Women are stereotyped and sexualized when they are depicted in movies. 

In this project, we leverage Natural Language Processing (NLP) techniques to study this bias especially in developing and developed regions. 


## 1. Prerequisites

Python >= 3.7
Gensim For Word Embeddings

## 2. Folder and Code Walkthrough

### 2.1 Dependency parsing, POS tagging and NER

In order to study the bias amongst different genders, we need to find out how different characters from different genders are portrayed. This information can be extracted by utilizing the linguistic features used to describe each of the characters.  CoreNLP developed by the Stanford NLP group consists of parser that can be used to derive these linguistic annotations for any text.

### 2.2 dependency_scraping.py

This File consists of the code to get the governor, dependency and part of speech tag for every token in the movie plot.

### 2.3 cloud_mapping.py

After running each movie plot through the parser and collecting the relevant tags, we now need to extract the relevant characteristics for every male and female characters. This python code will give the adjective and verb list for each proper noun or female/male synonymous words

### 2.4 Odds_Ratio_Calculation.py

This code computes the asymmetric words that occurs more often in men or women that the other half

### 2.5 weat.py and config.py

Run weat.py to get WEAT scores. Please download the embeddings from Stanford Glove and put them under WEAT/embeddings/ folder

## 3. Collaborators

* Tejaswini Patil
* Jessica D'souza
* Surabhi Gujare
* Akshata Talele
* Vaishnavi Kotawar

