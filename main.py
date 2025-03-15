import spellchecker

sc = spellchecker.SpellChecker()
txtIn = ""

while(txtIn != 4):
    sc.printMenu()

#aabid
#aabouda
#aad
#aadli
#aagadi
#aalla

    txtIn = input("Inserire il numero del menu: ")

    match txtIn:
        case "1":
            txt = input("Inserisci la tua frase in Italiano\n")
            sc.handleSentence(txt.lower(), "italian")

        case 2:
            txt = input("Inserisci la tua frase in Inglese\n")
            sc.handleSentence(txt.lower(),"english")

        case 3:
            txt = input("Inserisci la tua frase in Spagnolo\n")
            sc.handleSentence(txt.lower(),"spanish")

        case 4:
            print("Grazie, arrivederci!")

        case _:
            print("Errore nella selezione del menu!")
