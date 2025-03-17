import spellchecker

sc = spellchecker.SpellChecker()
txtIn = ""

while(txtIn != 4):
    sc.printMenu()

    txtIn = input("Inserire il numero del menu: ")

    match txtIn:
        case "1":
            txt = input("Inserisci la tua frase in Italiano\n")
            sc.handleSentence(txt, "italian")

        case "2":
            txt = input("Inserisci la tua frase in Inglese\n")
            sc.handleSentence(txt,"english")

        case "3":
            txt = input("Inserisci la tua frase in Spagnolo\n")
            sc.handleSentence(txt,"spanish")

        case "4":
            print("Grazie, arrivederci!")

        case _:
            print("Errore nella selezione del menu!")

#Il dinosaauro in pigiama decise di andare a fare la spesa, dimenticandosi però che non avva portasfoglio nè pantaloni, suscitando sguradi perplexi tra i pasanti.