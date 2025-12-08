def match_words(words):
    ctr = 0
    lst = []
    for words in words :
        if len(words) > 1 and words[0] == words[-1]:
            ctr += 1
            lst.append(words)

    print("List of words having first and last character same : \n",lst)
    return ctr
count = match_words(['abc', 'cfc','xyz', 'aba', '1221'])

print("Number of words having first and last character same:", count)

