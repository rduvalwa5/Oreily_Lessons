'''
Created on Jul 27, 2012

@author: rduvalwa2
'''
#!/usr/local/bin/python3
""" pair_frequency.py
"""
text = """\
Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full;
One for the master,
And one for the dame,
And one for the little boy
Who lives down the lane."""

for punc in ",?;.":
    text = text.replace(punc, "")
words = {}
textwords = text.lower().split()
firstword = textwords[0]
for nextword in textwords[1:]:
    if firstword not in words:
          words[firstword] = {}
    words[firstword][nextword] = words[firstword].get(nextword,0)+1
    print("For word ", nextword, "\n", words)
    firstword = nextword
for word in sorted(words.keys()):
       d = words[word]
       for word2 in sorted(d.keys()):
           print(word, ":", word2, d[word2])