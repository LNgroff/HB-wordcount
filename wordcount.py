# put your code here.
filename = open("test.txt")

def getkeys(filename):
    # poem = open(filename)
    #file = open("twain.txt")
    

    for line in filename:
        words = line.rstrip().split(" ")
        
        list_words = []
        #set_list = set(list_words)
        #keys = list(set_list)
        
        for word in words:
            word1 = word.lower().strip("',.!?-#$%^&();:_")
            list_words.append(word1)
    
    filename.close()

    return list_words

def wordcount(list_words):       
    wordcount = {}    
    set_list = set(list_words)
    keys = list(set_list)

    for key in keys:
        wordcount[key] = wordcount.get(key, 0) + 1
    
    for key, value in wordcount.items():
        print("{} {}".format(key,value))



 

wordcount(filename)
"""
for word in set_words:
    if word[-1] in special_char:
                del word[-1]
"""