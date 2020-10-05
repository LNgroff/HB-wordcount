# put your code here.

import sys
from collections import Counter

# filename = sys.argv[1]   # first real argument
# for melon_data in open(filename):
#     print(melon_data)
filename = sys.argv[1]

def wordcount(filename):
    
    with open(filename) as doc:
        document = doc.read().replace("\n", " ").strip(" ")

    new_list = []
    split_doc = document.split(" ")

    for word in split_doc:
        word1 = word.lower().strip("',.!?-#$%^&();:_") #word stripped of special char
        new_list.append(word1)
        
    counted = Counter(new_list)
    counted_items = counted.items()
    word_key = lambda x: (-x[1], x[0])
    
    # sorted_word_count = sorted(counted.items(), key=lambda x: (x[1], x[0])
    # changing what comes after x will change how it is sorted
    
    print(counted_items)
    
    sorted_word_count = sorted(counted_items, key = word_key)
   
    print(sorted_word_count)

    for tuple in sorted_word_count:
        print(tuple[0], tuple[1])
    
    # print(sorted(counted_items, key=lambda x: (-x[1], x[0]))
        #prints function as tuples ascending values  
    # print(sorted(counted.items(), key=lambda x: x[1], reverse=True))
        # prints function as tuples descending values


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



