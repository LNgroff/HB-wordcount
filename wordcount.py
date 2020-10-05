# put your code here.

import sys

# filename = sys.argv[1]   # first real argument
# for melon_data in open(filename):
#     print(melon_data)
filename = sys.argv[1]

def wordcount(filename):
    
    document = open(filename)
    

    wordcount = {}
    for line in document:
        words = line.rstrip().split(" ")
        
        set_words = set(words)
        keys = list(set_words)

        for word in words:
            word1 = word.lower().strip("',.!?-#$%^&();:_")
            wordcount[word1] = wordcount.get(word1, 0) + 1
    

    for word, value in sorted(wordcount.items()):
        print("{} {}".format(word,value))


 
wordcount(filename)



