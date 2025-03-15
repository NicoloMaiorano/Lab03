import datetime
import time
import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        if language == "italian":
            diz = open("Italian.txt", "r")
            txtIn.strip("\n")
            txtIn = replaceChars(txtIn)
            a = txtIn.split(" ")

            listaErrori = []
            tic = datetime.datetime.now()
            for p in a:
                trovato = 0
                for line in diz:
                    line.strip("\n")
                    line = line.split(" ")
                    if line[0].strip("\n") == p:
                        trovato = 1

                if trovato == 0:
                    listaErrori.append(p)



            toc = datetime.datetime.now()
            tempo = toc-tic
            print("Numero di errori: " + str(len(listaErrori)))
            print("Parole errate: ")

            for p in listaErrori:
                print(p)

            print("Tempo impiegato per il controllo ortografico: " + str(tempo))


        elif language == "english":
            diz = open("English.txt", "r")
        else:
            diz = open("Spanish.txt", "r")




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
    chars= "\\'*_{}[]()><#+-.!$%^;,=_"
    for c in chars:
        text = text.replace(c, "")

    return text