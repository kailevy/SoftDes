"""
Software Design Mini Project 3
Kai Levy

This script will pull Wikipedia articles from the internet in both English and Simple English
and compare the two.
"""
from pattern.web import *  
import sys
import string
import math
import numpy as np
import matplotlib.pyplot as plt

ignore_list = ['Notes', 'Related Pages', 'See also','References','Further reading']
languages = ['en', 'simple'] 
article_list = ['earth', 'poker', 'virus', 'wikipedia', 'computer', 'orchestra', 'long hair', 'association football', 'kiss']

def get_page(title,lang):
    """ Downloads a Wikipedia page and returns it as a string, 
    discounting certain sections, as well as punctuation and numbers"""
    w = Wikipedia(language = lang)
    article = w.search(title)
    full_text = ''
    fname = title + '_' + lang + '.txt'
    for section in article.sections:
        if section.title not in ignore_list:
            txt_temp = section.content.encode('utf8')
            txt_temp = txt_temp.translate(string.maketrans('',''),string.punctuation)
            txt_temp = txt_temp.translate(string.maketrans('',''),string.digits)
            full_text +=  txt_temp
    return full_text

def get_words(s):
    """ Returns a dictionary of word counts, given a string"""
    d = {}
    s = s.lower()
    for word in s.split():
        d[word] = d.get(word,0) + 1
    return d

def total_wc(d):
    """ Returns the number of words, given a string"""
    return sum(d.values())

def avg_word_length(s,wc):
    """ Returns the average word length in characters, given a string and word count"""
    s = s.translate(string.maketrans('',''),string.whitespace)
    return len(s) / float(wc)

def avg_par_length(s):
    """ Returns the average world length of paragraph, given a string"""
    pars = s.split('\n')
    return len(s) / float(len(pars))

def compute_similarity(d1,d2):
    """ Computes cosine similarity of the two dictionaries of words. This method was adapted from:
    http://stackoverflow.com/questions/15173225/how-to-calculate-cosine-similarity-given-2-sentence-strings-python"""
    intersection = set(d1.keys()) & set(d2.keys())
    numerator = sum([d1[w] * d2[w] for w in intersection])
    sum1 = sum([d1[w] ** 2 for w in d1.keys()])
    sum2 = sum([d2[w] ** 2 for w in d2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def article_stats(s_list,subject):
    """ Evaluates wordcount, average word length, average paragraph length, and similarity between
    the two articles and returns them in a list"""
    word_dicts = {languages[0]:{},languages[1]:{}}
    stats = [subject]
    for i,article in enumerate(s_list):
        word_dicts[languages[i]] = get_words(article)
        wc = total_wc(word_dicts[languages[i]])
        stats.append((wc,avg_word_length(article, wc),avg_par_length(article)))
    stats.append(compute_similarity(word_dicts[languages[0]],word_dicts[languages[1]]))
    return stats

def process_article(title):
    """ Completely processes a given article in both english and simple english and returns its stats"""
    strings = []
    for lang in languages:
        strings.append(get_page(title,lang))
    return article_stats(strings,title)

def plot_avgs(li,arg):
    """Plots the average word lengths and paragraph lengths in bar charts"""
    key = {'Word':1,'Paragraph':2}
    n_groups = len(article_list)
    en = []
    simple = []
    for sub_li in li:
        en.append(sub_li[1][key[arg]])
        simple.append(sub_li[2][key[arg]])

    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35

    rects1 = plt.bar(index, en, bar_width, alpha = 1, color = 'b', label = 'English')
    rects2 = plt.bar(index + bar_width, simple, bar_width, alpha = 1, color = 'r', label = 'Simple English')

    plt.xlabel('Article')
    plt.ylabel('Average Word Length')
    plt.title('Average ' + arg + ' Length of Simple English and English')
    plt.xticks(index + bar_width, article_list)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':  
    data = []
    for title in article_list:
        data.append(process_article(title))
    plot_avgs(data,'Word')
    plot_avgs(data, 'Paragraph')
    avg_sim = 0
    sims = {}
    for sub_li in data:
        sims[sub_li[0]] = sub_li[3]
        avg_sim += sub_li[3]
    avg_sim = avg_sim / len(article_list)
    print avg_sim
    print sims
