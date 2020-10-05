# put your code here.
filename = open("test.txt")

def wordcount(filename):
    # poem = open(filename)
    #file = open("twain.txt")

    wordcount = {}
    for line in filename:
        words = line.rstrip().split(" ")
        
        set_words = set(words)
        keys = list(set_words)

        for word in words:
            word1 = word.lower().strip("',.!?-#$%^&();:_")
            wordcount[word1] = wordcount.get(word1, 0) + 1
    

    for word, value in sorted(wordcount.items()):
        print("{} {}".format(word,value))


    filename.close()

 
wordcount(filename)



