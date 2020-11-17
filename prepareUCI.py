import json
import numpy as np
import pickle
import sys

def printTxt(corpus, vocab, outputFileName):
    temp = []
    f = open(outputFileName, "w")
    for idx, doc in enumerate(corpus):
        f.write((str(idx) + ' ') * 2)
        for token in doc:
            vocabID, count = token
            vocabName = vocab[vocabID]
            f.write((str(vocabName) + ' ') * count)
        f.write('\n')
    f.close()
    
def readUCITxt(inputDocwordName, inputVocabName):
    vocab = open(inputVocabName).read().splitlines()
    corpus = []
    docword = open(inputDocwordName).read().splitlines()
    docword = docword[3:]
    preID = 0
    for idx, line in enumerate(docword):
        lineList = line.split(' ')
        intList = [int(i) for i in lineList] 
        if intList[0] != preID:
            preID = intList[0]
            corpus.append([])
        corpus[-1].append((intList[1]-1, intList[2]))
    return corpus, vocab

def UCI2Txt(inputDocwordName, inputVocabName, outputFileName):
    corpus, vocab = readUCITxt(inputDocwordName, inputVocabName)
    printTxt(corpus, vocab, outputFileName)

def main():

    UCI2Txt('./data/docword.nytimes.txt', './data/vocab.nytimes.txt', './data/nytimes.txt')
    UCI2Txt('./data/docword.enron.txt', './data/vocab.enron.txt', './data/enron.txt')
    UCI2Txt('./data/docword.nips.txt', './data/vocab.nips.txt', './data/nips.txt')

    rna_corpus = pickle.load(open("./data/rna.corpus.pickle", "rb"))
    rna_vocab = pickle.load(open("./data/rna.vocab.pickle", "rb")) 
    printTxt(rna_corpus, rna_vocab, './data/rna.txt')
        
    return

if __name__ == '__main__':
    main()
