import codecs



## CARICAMENTO DEL TESTO

##a = codec.open('postLemmatizzati.txt','r','utf8')

##testoTot = a.read()



## CARICAMENTO DELLE RISORSE

listaPolarita = [('bello',2),('brutto',-2),('emozionante',+2)]

##listaTesto = ['lo','spot','era','veramente','bello','ma','non','emozionante','!']

intensificazione = ['veramente']

negazione = ['non']



##listaPost = testoTot.split('\n')

listaPost = ['lo spot essere bello ma non emozionante !', 'un brutto pubblicità']

##listaPost = ['bello questo immagine <<smiling face with sunglasses>> <<flexed biceps>>', 'un brutto pubblicità']


for testo in listaPost:

##testo = 'lo spot era bello ma non emozionante !'

    listaTesto = testo.split(' ')



    polaritaTotale=0

    for c in range(0,len(listaTesto)):

        polarita=0

        for el in listaPolarita:

            if listaTesto[c] == el[0]:

                polarita = el[1]

                if listaTesto[c-1] in negazione:

                    polarita = polarita-1

                if listaTesto[c-1] in intensificazione:

                    polarita = polarita*1.5

                if listaTesto[c+1] in intensificazione:

                    polarita = polarita*1.5

        polaritaTotale+=polarita

        

    print('--'+testo+'-- Polarità: '+str(polaritaTotale))

    



















    

    

