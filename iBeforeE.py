'''
Given a word or sentence, return a corrected version where every word follows the "I before E except after C" rule.

If a word contains "ei" not preceded by "c", replace it with "ie".
If a word contains "ie" preceded by "c", replace it with "ei".
All other words are left unchanged.
'''

import re

def i_before_e(sentence):

    words = sentence.split()
    corrected = [replace(word) for word in words]
    return " ".join(corrected)

def replace(word):

    word = re.sub(r'(?<!c)ei', 'ie', word, flags = re.IGNORECASE)
    word = re.sub(r'(?<=c)ie', 'ei', word, flags = re.IGNORECASE)
    return word


print(i_before_e("beleive")) #should return "believe".
print(i_before_e("recieve"))# should return "receive".
print(i_before_e("we recieved a breif")) # return "we received a brief".
print(i_before_e("she beleived the friendly niece could percieve the greif")) # should return "she believed the friendly niece could perceive the grief".
print(i_before_e("we recieved relief after the theif gave us a breif piece of feirce deceit")) # should return "we received relief after the thief gave us a brief piece of fierce deceit"