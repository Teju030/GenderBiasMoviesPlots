# Gender Bias in Movie Plots based on geographical locations

Movies are a simulation of society. They mirror the issues, problems, thinking and perception of the contemporary world we live in. Therefore, in any society, movies act as a strong medium to understand how prevalent gender bias and stereotypes are. Gender bias can be defined as dominance, in particular contexts (for example, in occupations or among primary social roles), of one gender over the other. As a consequence, the less dominant gender is underrepresented and stereotypes appear. This can be seen in movies as well, for example, characters like nurses tend to be female and doctors tend to be male. Also, more often than not, Women are stereotyped and sexualized when they are depicted in movies. 

In this project, we leverage Natural Language Processing (NLP) techniques to study this bias especially in developing and developed regions. 


## 1. Prerequisites

Python >= 3.7
Gensim For Word Embeddings

## 2. Architecture 
<img src="demo/architecutre.png" width="400" height="400">

## 2. Folder and Code Walkthrough

### 2.1 Collecting Data - CollectingMoviePlots.ipynb

We use CMU Dataset(http://www.cs.cmu.edu/~ark/personas/) which scrapped the data from Wikipedia in November 2012. For the remaining years 2013-2020, we extract the movie plots from Wikipedia for the different countries. The code is present in CollectingMoviePlots.ipynb

### 2.2 EventChainConstruction.ipynb

This notebook consists of our implementation of the Event Chain Architecture we've proposed.

### 2.3 WeightedLogOddsRatio.ipynb

We use WeightedLogOdds Ratios of the code to get the assymetrics unigrams and bigrams. Code is present in WeightedLogOddsRatio.ipynb

### 2.5 weat.py and config.py

Run weat.py to get WEAT scores. 

## 3. Results

Kindly refer [here](https://drive.google.com/drive/folders/1aYc4OZHBLFc9oQIl9r8HN5ExUTgitNVW?usp=sharing) for our results and collected data.

## 4. Collaborators

* Jessica D'souza
* Tejaswini Patil
* Surabhi Gujare
* Akshata Talele
* Vaishnavi Kotawar

