città =("Monza", [("Gennaio", 45),("Febbraio", 67), ("Marzo", 65)],
        "Brescia",[("Gennaio",64),("Febbraio",87),("Marzo",54)],
        "Como",[("Gennaio",63),("Febbraio",80),("Marzo",34)],


)

cittatrova=False

while True:  
    citta2=input("Inserire la citta  ")
    for capoluoghi,*rilevazione in città:
        if(citta2 == città):
            cittatrova=True
    if( not cittatrova):
        print("non c'è")
    else:
        break
def totale(città,valmax,mesemax,valmin,mesemin,media):
    mesemin=[]
    valmin=1000
    mesemax=[]
    valmax=0
    media=0
    conta=0
    tot=0
    for capoluogo ,*rilevazioni in città:
        media=0
        conta=0
        tot=0
        for mese,dato in rilevazioni:
            tot+=rilevazione
            conta+=1
    media=tot/conta
    for capoluoghi ,*rilevazioni in città:
        for mese,dato in rilevazione:
            if(valmax<mese):
                valmax=mese
                mesemax=[mese]
            elif(valmax==mese):
                    mesemax=[mese]
    for capoluoghi ,*rilevazione in città:
        for mese,dato in rilevazione:
            if(valmin<mese):
                valmin=mese
                mesemin=[mese]
            elif(valmin==mese):
                    mesemin=[mese]

    tupla=(media,(valmax,mesemax),(valmin,mesemin))
    return tupla

 
 




