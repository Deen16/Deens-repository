import random

def random_number():
    print(str(random.randint(1,100)))

def capital_indexes(word):
    indexes = []
    for x in range (len(word)):
        if word[x] == word.upper()[x]:
              indexes.append(x)
              print(indexes)

def mid(word):
    if(len(word)%2)==():
        print("")
    else:
        print(word[len(word)//2])

random_number()
capital_indexes(input(""))
mid(input(""))
