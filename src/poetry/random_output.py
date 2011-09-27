'''
Created on 20 Aug 2011

@author: Bluebottle
'''
import nltk
from verse_forms import iambic_pentameter
from random import choice, shuffle
from poetry.words import word_has_pronunciation, word_starts_with_punctuation,\
    word_accent_shape, syllable_count

def main():
    cfd = model_setup()
    #generate_random_text(cfd,generate_starting_word(),10)
    for i in range(10):
        #print "%d: %s" % (i, " ".join(generate_poetry_line(cfd,iambic_pentameter())) )
        generate_poetry_line(cfd,iambic_pentameter())
        print "   : %d" % (i + 1)

def model_setup():
    text = text_to_use()
    bigrams = nltk.bigrams(text)
    cfd = nltk.ConditionalFreqDist(bigrams)
    return cfd

def text_to_use():
    return nltk.corpus.shakespeare.words('hamlet.xml')

def generate_starting_word():
    word = choice(text_to_use())
    while not word_has_pronunciation(word):
        word = choice(text_to_use())
    return word

def generate_random_text(cfdist,word='king',num=15):
    for i in range(num):
        print word,
        print nltk.corpus.cmudict.dict()[word],
        print word_accent_shape(word)
        word = choice(cfdist[word].samples())
        while word_starts_with_punctuation(word) or not word_has_pronunciation(word):
            word = choice(cfdist[word].samples())

def generate_poetry_line(cfdist,verse_form,word=None):
    if word is None:
        word = generate_starting_word()
    poetry_line = []
    word_count = 0
    while word_count < len(verse_form):
        # For now, ignore metre?
        # Also, word is not the first of this line, but the last of the previous line.
        word = choose_next_word(cfdist,word,verse_form[word_count:])
        poetry_line.append(word)
        word_count += syllable_count(word)
        print word,
    return poetry_line

def choose_next_word(cfdist,word,verse_form):
    possibilities = cfdist[word].samples()
    shuffle(possibilities)
    for poss_word in possibilities:
        if not word_starts_with_punctuation(poss_word) and word_has_pronunciation(poss_word) and (syllable_count(poss_word) <= len(verse_form)):
            return poss_word
    else:
        return generate_starting_word()
    #next_word = choice(cfdist[word].samples())
    #while word_starts_with_punctuation(next_word) or not word_has_pronunciation(next_word) or (syllable_count(next_word) > len(verse_form)):
    #    next_word = choice(cfdist[word].samples())
    #print next_word,
    #print verse_form
    #return next_word

if __name__ == '__main__':
    main()