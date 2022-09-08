import io
import random
kelimeler = []
wordleList = []
olmayanlar = []
desiredLenght = int(input("kelime uzunluğu: "))
with io.open("hepsi.txt", 'r', encoding='utf8') as f:
    text = f.read()
kelimeler = text.split("\n")
for kelime in kelimeler:
    if (len(kelime) == desiredLenght):
        if (" " in kelime):
            continue
        else:
            wordleList.append(kelime)


def randomWord(list, lgt):
    x = 0
    words = []
    while (x < 300 and (len(words) < lgt)):
        randomWord = list[int(random.random()*len(list))]
        bool = True
        for i in randomWord:
            if (len(randomWord.replace(i, "")) == desiredLenght-1):
                continue
            else:
                bool = False
        if (bool):
            words.append(randomWord)
        x = x+1
    while (len(words) < lgt):
        rnd = list[int(random.random()*len(list))]
        if rnd in words:
            continue
        else:
            words.append(rnd)
    str = ""
    for i in words:
        str += i + ","
    return str


def doesHave(haves, string):
    boolean = True
    for i in haves:
        if (i in string):
            continue
        else:
            boolean = False
    return boolean


def dontHave(donts, string):
    boolean = True
    for i in donts:
        if (i in string):
            boolean = False
    return boolean


def notThere(list, harf):
    boolean = True
    for i in list:
        if (i == harf):
            boolean = False
    return boolean


while True:
    string = ""
    olmayanlar.clear()
    print("Başlangıç kelimeleri: ", randomWord(wordleList, 3))
    have = str(input("Hangi harfler var(sarı ve yeşil harfler): "))
    dont = str(input("Hangi harfler yok(gri harfler): "))
    for i in have:
        if (i in dont):
            dont = dont.replace(i, "")
    for a in range(desiredLenght):
        olmayanlar.append("0")
    for i in range(desiredLenght):
        kesin = str(input("varsa " + str(i+1) + " . harf: "))
        if (kesin == ""):
            print(
                str(i+1) + ". harfte olmayanlar(varsa sarı harfler yoksa enter): ", end="")
            yok = str(input())
            element = []
            for j in yok:
                element.append(j)
            olmayanlar[i] = element
            string += " "
        else:
            string += kesin
            if (kesin in dont):
                dont = dont.replace(kesin, "")
    print("--------------")
    for kelime in wordleList:
        boolean = True
        for i in range(desiredLenght):
            if (string[i] == kelime[i]):
                continue
            elif (string[i] == " " and notThere(olmayanlar[i], kelime[i])):
                continue
            else:
                boolean = False
        if (boolean == True and doesHave(have, kelime) and dontHave(dont, kelime)):
            print(kelime)
    print("--------------")
