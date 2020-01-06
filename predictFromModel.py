from gensim import corpora
import gensim.models
from gensim import utils

model = gensim.models.Word2Vec.load(".\\vocab.txt")

while True:
    print("Write the path of the txt file: ")
    inputPath = input()
    
    f = open(inputPath)
    
    print("Write the phrase to compare: ")
    inputSent = input()
    
    for line in f.readlines():
        similarity = model.wv.wmdistance(inputSent.lower().split(), line.lower().split())
        if similarity <= 0.025:
            print("The similarity: "+str(similarity))

    f.seek(0)

