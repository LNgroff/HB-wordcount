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

"""
Broken down lambda function:
# sorted_word_count = sorted(counted.items(), key=lambda x: (x[1], x[0]))
Lambda function is an "anonymous" function that only lives for the duration of being called.
counted.items() returns a list of tuples
x : (x[1], x[0])) --> first x refers to the first item within each tuple to sort by
                  --> second x refers to the second item within each tuple to sort by
"""       
    # sorted_word_count = sorted(counted.items(), key=lambda x: (x[1], x[0]))

    counted = Counter(new_list)
    counted_items = counted.items()
    word_key = lambda x: (-x[1], x[0])
    
    # sorted_word_count = sorted(counted.items(), key=lambda x: (x[1], x[0])
    # changing what comes after x will change how it is sorted
    
    print(counted_items)
    
    sorted_word_count = sorted(counted_items, key = word_key)
    # this is the same lambda function in the comment above, but with each peice
    # identified outside of it so as to make it clearer
   
    print(sorted_word_count)

    for tuple in sorted_word_count:
        print(tuple[0], tuple[1])
    
    # print(sorted(counted_items, key=lambda x: (-x[1], x[0]))
        #prints function as tuples ascending values  
    # print(sorted(counted.items(), key=lambda x: x[1], reverse=True))
        # prints function as tuples descending values

# Used the below print statements prior to using a lambda function
    # print(Counter(sorted(new_list)))
        # sorts by value descending
    # print(sorted(Counter(new_list)))
        # prints sorted keys without values as list

wordcount(filename)


"""
Previous code used prior to using the counter


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
