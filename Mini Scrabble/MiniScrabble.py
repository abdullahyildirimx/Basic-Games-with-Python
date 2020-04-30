import datetime
import sys
list1=[]
list1 = open("letter_values.txt", encoding="utf8").read().splitlines()
dict1 = {}
for i in range(0,len(list1)):
    (key1, val1) = list1[i].split(":")
    dict1[str(key1)] = int(val1)
list2=[]
list2 = open("correct_words.txt", encoding="utf8").read().splitlines()
chooseword=list2[0]
word=list2[0].split(":")[0]
dict2 = {}
for j in range(0,len(list2)):
    (key2, val2) = list2[j].split(":")
    val2=val2.split(',')
    dict2[str(key2)] = val2
print("Shuffled words are", word.lower(), "Please guess words for these letters with minimum three letters")
a=datetime.datetime.now()
b=datetime.datetime.now()
c=b-a
totalpoint=0
wordlist=[]
while 30-c.seconds>0:
    n=str(input("Guessed Word: ")).upper()
    if n in wordlist:
        print("This word is guessed before")
    elif n not in dict2[word.upper()]:
        print("your guessed word is not a valid word")
    else:
        wordlist.append(n)
    b=datetime.datetime.now()
    c=(b-a)
    if 30-c.seconds>0:
        print("You have", 30-c.seconds, "seconds.")
    elif 30-c.seconds<=0:
        print("You have", 0, "seconds.")
for i1 in range(0,len(wordlist)):
    wordscore=0
    for i2 in range(0,len(wordlist[i1])):
        wordscore=wordscore+dict1[wordlist[i1][i2]]
    totalpoint=totalpoint+wordscore*len(wordlist[i1])
words=""
for i3 in range(0,len(wordlist)):
    if i3==len(wordlist)-1:
        words=words+(wordlist[i3].lower())
    else:
        words=words+(wordlist[i3].lower())+'-'
print("Score for", word.lower(), "is", totalpoint, "and guessed words are", words)
