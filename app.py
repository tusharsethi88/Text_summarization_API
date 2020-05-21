# Text Summarization
import nltk
import re
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from heapq import nlargest
import string
from flask import Flask, render_template,request,url_for, jsonify
import logging as logger
from text_summarizer import textsummary
from text_summarizer import remove_stopwords

# Flask App Name
flaskAppInstance = Flask(__name__)


# print(textsummary(text))
@flaskAppInstance.route('/text_summarization', methods=['GET', 'POST'])
def text_summarization():
  if request.method == "GET":
    return jsonify({"response": "Get Request Called"})
  elif request.method == "POST":
    req_Json = request.json
    texttosummary = req_Json['texttosummary']
    return jsonify({"response": textsummary(texttosummary)})


if __name__ == '__main__':
    flaskAppInstance.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
