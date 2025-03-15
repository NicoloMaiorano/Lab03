import datetime
import fileinput
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

            stringaDiz = ""

            print("Prima della creazione della mega stringa")
            for line in diz:
                line = line.strip("\n")
                stringaDiz = stringaDiz + line + " "

            print(stringaDiz)

            for p in a:
                p = p.strip("\n")
                if stringaDiz.__contains__(p):
                    pass
                else:
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
            txtIn.strip("\n")
            txtIn = replaceChars(txtIn)
            a = txtIn.split(" ")

            listaErrori = []
            tic = datetime.datetime.now()

            stringaDiz = ""

            for line in fileinput.input(["English.txt"]):
                line = line.strip("\n")
                stringaDiz = stringaDiz + line + " "

            #for line in diz:
            #    line = line.strip("\n")
            #    stringaDiz = stringaDiz + line + " "


            for p in a:
                p = p.strip("\n")
                if stringaDiz.__contains__(p):
                    pass
                else:
                    listaErrori.append(p)

            toc = datetime.datetime.now()
            tempo = toc - tic
            print("Numero di errori: " + str(len(listaErrori)))
            print("Parole errate: ")

            for p in listaErrori:
                print(p)

            print("Tempo impiegato per il controllo ortografico: " + str(tempo))

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
    chars= "\\'*_{}[]()><?#+-.!$%^;,=_"
    for c in chars:
        text = text.replace(c, "")

    return text

