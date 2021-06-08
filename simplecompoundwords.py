# Given a list of words, find simple words and compound words
# compound words are words that are only composed of simple words.
# ex) ['apple', 'cat' , 'dog', 'catdog', 'applecat']
# 

from typing import Counter

def isCompound(word, wordset):
    if not wordset:
        return False 
    dp = [True] + [False] * len(word) 
    # dp = [T, F, F, T, F, F, T]
    # 'catcat'

    for i in range(0, len(word)+1):
        for j in range(0, i):
            if not dp[j]:
                #c, ca
                continue
            if dp[j] and word[j:i] in wordset:
                dp[i] = True
                break
    return dp[-1] 


def simplecompound(list):
    
    list = sorted(list, key=lambda x:len(x))
    
    compounds = [] 
    simples = []

    wordset = set() 
    for word in list:
        if isCompound(word, wordset):
            compounds.append(word)
        else:
            simples.append(word)
        wordset.add(word) 
    
    return compounds



test = ['apple', 'cat' , 'dog', 'catdog', 'applecat']
print(simplecompound(test)) 
