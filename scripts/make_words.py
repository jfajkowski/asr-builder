#!/usr/bin/python3
import codecs
import sys
import re
from nltk import word_tokenize


text_file_path = sys.argv[1]

words = []
with codecs.open(text_file_path, encoding='UTF-8', mode='r') as f_in:
    raw = f_in.read()
    utterances = str.join('\n', re.findall(r'<s> (.+) </s>', raw))
    words += word_tokenize(utterances, language='polish')

for word in sorted(set(words)):
    print(word)