# Text Summarization
import nltk
import re
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from heapq import nlargest
import string
from flask import Flask, render_template,request,url_for, jsonify
import logging as logger 

nltk.download('stopwords')

#load stopwords
stop = nltk.corpus.stopwords.words('english')
def remove_stopwords(sentence):
    filtered_sentence = " ".join([i for i in sentence if i not in stop])
    return filtered_sentence

def textsummary(text):
  #Split paragraph into sentences.
  sentences = sent_tokenize(text)
 
#Pre-process your text. Remove punctuation, special characterts, numbers, etc.
  clean_sentences = [s.translate(string.punctuation) for s in sentences] 
  clean_sentences = [s.translate(string.digits) for s in clean_sentences] 


#lowercase
  clean_sentences = [s.lower() for s in clean_sentences]
  clean_sentences = [remove_stopwords(s.split()) for s in clean_sentences]
 

#Weighted Word Frequencies | Word Focused
#Compute word frequencies for each sentence
  word_frequencies = {}
  for i in range(len(clean_sentences)):
      for word in nltk.word_tokenize(clean_sentences[i]):
          if word not in word_frequencies.keys():
              word_frequencies[word] = 1
          else:
              word_frequencies[word] += 1

#Find max frequency in text and compute the weighted frequency based on the maximum frequency.
  # maximum_frequency = max(word_frequencies.values())
  for word in word_frequencies.keys():
      word_frequencies[word] = (word_frequencies[word]/max(word_frequencies.values()))

#Apply scores to each UNCLEANED SENTENCE
  sentence_scores = {}
  for sent in sentences:
      for word in nltk.word_tokenize(sent.lower()):
          if word in word_frequencies.keys():
              if len(sent.split(' ')) < 50:
                  if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                  else:
                    sentence_scores[sent] += word_frequencies[word]
 
#Choose number of sentences you want in your summary
  summary_sentences = nlargest(5, sentence_scores, key=sentence_scores.get)
  summary = ' '.join(summary_sentences)
  return summary