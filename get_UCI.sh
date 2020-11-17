#!/bin/bash

#Download NIPS from UCI repository
wget -P ./data/ https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/docword.nips.txt.gz
gunzip ./data/docword.nips.txt.gz
wget -P ./data/ https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.nips.txt

#Download ENRON from UCI repository
wget -P ./data/ https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/docword.enron.txt.gz
gunzip ./data/docword.enron.txt.gz
wget -P ./data/ https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.enron.txt

#Download NYTIMES from UCI repository
wget -P ./data/ https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/docword.nytimes.txt.gz
gunzip ./data/docword.nytimes.txt.gz
wget -P ./data/ https://archive.ics.uci.edu/ml/machine-learning-databases/bag-of-words/vocab.nytimes.txt

python prepareUCI.py
