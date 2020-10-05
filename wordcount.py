# put your code here.

import sys
from collections import Counter

# filename = sys.argv[1]   # first real argument
# for melon_data in open(filename):
#     print(melon_data)
filename = sys.argv[1]

def wordcount(filename):
    
    with open(filename) as doc:
        document = doc.read().replace("\n", " ")

    new_list = []
    split_doc = document.split(" ")

    for word in split_doc:
        if word == " ":
            continue
        word1 = word.lower().strip("',.!?-#$%^&();:_") #word stripped of special char
        new_list.append(word1)
        
    counted = Counter(new_list)

    print(sorted(counted.items(), key=lambda x: x[1]))
        #prints function as tuples ascending
    # print(sorted(counted.items(), key=lambda x: x[1], reverse=True))
        # prints function as tuples descending

"""def ascending_order(filename):
    dictionary = wordcount(filename)

    result = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])}

    print(result)
    """
    


    # print(Counter(sorted(new_list)))
        # sorts by value descending
    # print(sorted(Counter(new_list)))
        # prints sorted keys without values as list
'''
>>> x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
>>> {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}

{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
'''

"""
    for line in document:
        words = line.rstrip().split(" ")
        for word in words:
            word1 = word.lower().strip("',.!?-#$%^&();:_") #word stripped of special char
            new_list.append(word1)
"""
"""    
    set_words = set(words)
    keys = list(set_words)    
        for word in words:   
            word1 = word.lower().strip("',.!?-#$%^&();:_")
            wordcount[word1] = wordcount.get(word1, 0) + 1
 
    for word, value in sorted(wordcount.items()):
        print("{} {}".format(word,value))
"""    

wordcount(filename)



