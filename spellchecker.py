import datetime
import fileinput
import time
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        if language == "italian":
            print("Ricerca con contains:")
            tic = datetime.datetime.now()
            listaErrori = ricercaContains(txtIn, "Italian.txt")
            toc = datetime.datetime.now()
            tempo = toc-tic
            print("Numero di errori: " + str(len(listaErrori)))
            print("Parole errate: ")
            for p in listaErrori:
                print(p)
            print("Tempo impiegato per il controllo ortografico: " + str(tempo))

            print("------------------------------------------------------------")
            print("Ricerca lineare: ")
            tic = datetime.datetime.now()
            listaErrori = ricercaLineare(txtIn, "Italian.txt")
            toc = datetime.datetime.now()
            tempo = toc - tic
            print("Numero di errori: " + str(len(listaErrori)))
            print("Parole errate: ")
            for p in listaErrori:
                print(p)
            print("Tempo impiegato per il controllo ortografico: " + str(tempo))

            print("------------------------------------------------------------")
            print("Ricerca dicotomica: ")
            tic = datetime.datetime.now()
            listaErrori = ricercaDicotomica(txtIn, "Italian.txt")
            toc = datetime.datetime.now()
            tempo = toc - tic
            print("Numero di errori: " + str(len(listaErrori)))
            print("Parole errate: ")
            for p in listaErrori:
                print(p)
            print("Tempo impiegato per il controllo ortografico: " + str(tempo))

        elif language == "english":
            tic = datetime.datetime.now()
            listaErrori = ricercaContains(txtIn, "English.txt")
            toc = datetime.datetime.now()
            tempo = toc - tic
            print("Numero di errori: " + str(len(listaErrori)))
            print("Parole errate: ")
            for p in listaErrori:
                print(p)
            print("Tempo impiegato per il controllo ortografico: " + str(tempo))

            print("------------------------------------------------------------")
            print("Ricerca lineare: ")
            tic = datetime.datetime.now()
            listaErrori = ricercaLineare(txtIn, "English.txt")
            toc = datetime.datetime.now()
            tempo = toc - tic
            print("Numero di errori: " + str(len(listaErrori)))
            print("Parole errate: ")
            for p in listaErrori:
                print(p)
            print("Tempo impiegato per il controllo ortografico: " + str(tempo))

            print("------------------------------------------------------------")
            print("Ricerca dicotomica: ")
            tic = datetime.datetime.now()
            listaErrori = ricercaDicotomica(txtIn, "English.txt")
            toc = datetime.datetime.now()
            tempo = toc - tic
            print("Numero di errori: " + str(len(listaErrori)))
            print("Parole errate: ")
            for p in listaErrori:
                print(p)
            print("Tempo impiegato per il controllo ortografico: " + str(tempo))
        else:
            tic = datetime.datetime.now()
            listaErrori = ricercaContains(txtIn, "Spanish.txt")
            toc = datetime.datetime.now()
            tempo = toc - tic
            print("Numero di errori: " + str(len(listaErrori)))
            print("Parole errate: ")

            for p in listaErrori:
                print(p)

            print("Tempo impiegato per il controllo ortografico: " + str(tempo))

            print("------------------------------------------------------------")
            print("Ricerca lineare: ")
            tic = datetime.datetime.now()
            listaErrori = ricercaLineare(txtIn, "Spanish.txt")
            toc = datetime.datetime.now()
            tempo = toc - tic
            print("Numero di errori: " + str(len(listaErrori)))
            print("Parole errate: ")
            for p in listaErrori:
                print(p)
            print("Tempo impiegato per il controllo ortografico: " + str(tempo))

            print("------------------------------------------------------------")
            print("Ricerca dicotomica: ")
            tic = datetime.datetime.now()
            listaErrori = ricercaDicotomica(txtIn, "Spanish.txt")
            toc = datetime.datetime.now()
            tempo = toc - tic
            print("Numero di errori: " + str(len(listaErrori)))
            print("Parole errate: ")
            for p in listaErrori:
                print(p)
            print("Tempo impiegato per il controllo ortografico: " + str(tempo))

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars= "\\'*_{}[]()><?#+-.!$%^;,=_"
    for c in chars:
        text = text.replace(c, "")

    return text

def ricercaContains(txtIn, nome):
    txtIn = txtIn.lower()
    txtIn.strip("\n")
    txtIn = replaceChars(txtIn)
    a = txtIn.split(" ")
    listaErrori = []
    with open(nome, "r") as f:
        wordlist = f.read().splitlines()
    for p in a:
        p = p.strip("\n")
        if wordlist.__contains__(p):
            pass
        else:
            listaErrori.append(p)
    return listaErrori

def ricercaLineare(txtIn, nome):
    txtIn = txtIn.lower()
    txtIn.strip("\n")
    txtIn = replaceChars(txtIn)
    a = txtIn.split(" ")
    listaErrori = []
    with open(nome, "r") as f:
        wordlist = f.read().splitlines()
    for p in a:
        trovato = 0
        p = p.strip("\n")
        for g in wordlist:
            if p == g:
                trovato = 1

        if trovato == 0:
            listaErrori.append(p)

    return listaErrori

def ricercaDicotomica(txtIn, nome):
    txtIn = txtIn.lower()
    txtIn.strip("\n")
    txtIn = replaceChars(txtIn)
    a = txtIn.split(" ")
    listaErrori = []
    with open(nome, "r") as f:
        wordlist = f.read().splitlines()

    for p in a:
        trovato = 0
        p = p.strip("\n")

        if p == wordlist[int((len(wordlist)/2))]:
            trovato = 1
        elif p > wordlist[int((len(wordlist)/2))]:
            for x in range(int((len(wordlist)/2)), len(wordlist)):
                if p == wordlist[x]:
                    trovato = 1
        else:
            for x in range(int((len(wordlist) / 2))):
                if p == wordlist[x]:
                    trovato = 1

        if trovato == 0:
            listaErrori.append(p)

    return listaErrori