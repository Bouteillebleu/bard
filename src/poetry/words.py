'''
Created on 20 Aug 2011

@author: Bluebottle
'''
import nltk
import string
import re

def word_starts_with_punctuation(word):
    for char in string.punctuation:
        if word.startswith(char):
            return True
    else:
        return False

def word_has_pronunciation(word):
    if word in nltk.corpus.cmudict.words():
        return True
    else:
        return False

def word_accent_shape(word):
    #print nltk.corpus.cmudict.dict()
    pronunciation = nltk.corpus.cmudict.dict()[word][0]
    accent_shape = []
    accented_phoneme = re.compile(r'\w+(\d+)')
    for phoneme in pronunciation:
        if accented_phoneme.match(phoneme):
            accent = int(accented_phoneme.match(phoneme).group(1))
            accent_shape.append(accent)
    return accent_shape

def syllable_count(word):
    return len(word_accent_shape(word))