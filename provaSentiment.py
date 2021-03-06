import codecs


## CARICAMENTO DEL TESTO

a = codecs.open('./prova.txt','r','utf8')               # dos errores en esta linea

testoTot = a.read()



## CARICAMENTO DELLE RISORSE


polaritaLista = [
    ('abbassare',-1),
    ('abbattere',-2),
    ('abbraccio',2),
    ('accantonare',-1),
    ('accattivante',2),
    ('accettare',1),
    ('accolto',1),
    ('accorgere',1),
    ('acquistare',1),
    ('acquisto',1),
    ('adattare',2),
    ('adatto',2),
    ('addebitare',-2),
    ('adorare',3),
    ('affidabile',2),
    ('agevolare',1),
    ('aiutare',2),
    ('aiutato',2),
    ('alto',-1),
    ('altruismo',2),
    ('alzare',1),
    ('amante',2),
    ('amare',3),
    ('amato',3),
    ('amo',2),
    ('amico',1),
    ('ammalare',-2),
    ('ammirazione',3),
    ('amore',3),
    ('angoscia',-3),
    ('animo',1),
    ('appartenere',1),
    ('applauso',2),
    ('apprezzare',2),
    ('appropriato',2),
    ('aprire',1),
    ('artista',1),
    ('ascoltare',1),
    ('assente',-2),
    ('assistenza',2),
    ('assistere',2),
    ('attento',2),
    ('attenzione',2),
    ('attirare',1),
    ('attuale',1),
    ('augurare',2),
    ('auguri',1),
    ('augurio',1),
    ('avanguardia',2),
    ('avanti',1),
    ('azzerare',-1),
    ('bacio',2),
    ('banale',-2),
    ('barzelletta',-3),
    ('basta',-2),
    ('bastare',-2),
    ('bello',2),
    ('bella',2),
    ('bellissimo',3),
    ('bene',2),
    ('benedire',2),
    ('bere',1),
    ('bisogno',1),
    ('bloccare',-1),
    ('boicottare',-3),
    ('bombardamento',-3),
    ('bombardare',-3),
    ('bontà',2),
    ('bravo',2),
    ('brindare',2),
    ('brivido',2),
    ('brutto',-2),
    ('buono',2),
    ('cadere',-1),
    ('cambiamento',1),
    ('cambiare',-2),
    ('capacità',2),
    ('capitalista',-2),
    ('capolavoro',3),
    ('carino',1),
    ('cattivo',-2),
    ('certezza',2),
    ('cliente',1),
    ('climatico',1),
    ('co2',-3),
    ('collaborare',2),
    ('colpito',2),
    ('colpire',2),
    ('commovente',3),
    ('commuovere',3),
    ('commosso',3),
    ('comodo',2),
    ('compagnia',1),
    ('complimentare',2),
    ('complimento',2),
    ('complimenti',2), 
    ('comprare',1),
    ('comunicazione',1),
    ('concentrato',1),
    ('condividere',2),
    ('conferma',1),
    ('conforto',2),
    ('confortare',2),
    ('consolare',2),
    ('consulenza',2),
    ('contento',2),
    ('continuare',1),
    ('contributo',1),
    ('contro',-2),
    ('coraggio',2),
    ('coraggioso',2),
    ('costoso',-2),
    ('credere',1),
    ('crisi',-2),
    ('cuore',2),
    ('cura',2),
    ('dare',1),
    ('delusione',-3),
    ('demenziale',-3),
    ('descrivere',1),
    ('determinazione',2),
    ('difficile',-2),
    ('difficoltà',-2),
    ('dignità',2),
    ('dimenticare',-2),
    ('dimostrare',1),
    ('disagio',-3),
    ('disattivare',-1),
    ('discriminato',-3),
    ('disponibilità',2),
    ('dittatura',-3),
    ('diventare',1),
    ('divino',3),
    ('dolce',2),
    ('dolceamaro',1),
    ('donare',2),
    ('donazione',2),
    ('dono',2),
    ('dubbio',-1),
    ('durare',1),
    ('eccellente',3),
    ('eccellenza',3),
    ('eccellere',3),
    ('ecologico',2),
    ('eliminare',-2),
    ('emergenza',-1),
    ('emozionale',1),
    ('emozionante',3),
    ('emozionare',3),
    ('emozionato',3),
    ('emozione',3),
    ('encomiabile',3),
    ('eroi',2),
    ('esaurire',-3),
    ('esempio',1),
    ('esigenza',1),
    ('estero',-1),
    ('evviva',3),
    ('famiglia',1),
    ('fantastico',3),
    ('farabutto',-3),
    ('fare',1),
    ('feccia',-3),
    ('felice',2),
    ('ferita',-2),
    ('fermare',-1),
    ('fesseria',-3),
    ('festa',2),
    ('festeggiare',2),
    ('fiero',2),
    ('fiera',2),
    ('figata',2),
    ('finire',-1),
    ('formaldeide',-3),
    ('fornire',1),
    ('forza',2),
    ('funzionare',1),
    ('garantire',1),
    ('geniale',3),
    ('gesto',1),
    ('gioia',2),
    ('globalista',-2),
    ('gran',2),
    ('grande',2),
    ('grandioso',3),
    ('grazie',2),
    ('guardare',1),
    ('idea',1),
    ('ideale',3),
    ('identità',2),
    ('illuminato',2),
    ('imbarazzante',-3),
    ('immenso',3),
    ('impatto',2),
    ('impegnare',2),
    ('impegno',2),
    ('implorare',-2),
    ('importante',2),
    ('impossibile',-3),
    ('impresentabile',-3),
    ('incapace',-2),
    ('incredibile',3),
    ('indimenticabile',3),
    ('ingannevole',-3),
    ('iniziativa',1),
    ('inquinamento',-2),
    ('insegnamento',2),
    ('insegnare',1),
    ('insieme',2),
    ('insopportabile',-3),
    ('insuperabile',3),
    ('inutile',-2),
    ('investire',1),
    ('ipocrisia',-3),
    ('ipocrita',-2),
    ('irresponsabile',-3),
    ('isolato',-2),
    ('ispirazione',2),
    ('italia',1),
    ('italiano',1),
    ('kintsugi',2),
    ('lacrima',2),
    ('lanciare',1),
    ('lavorare',1),
    ('lento',-2),
    ('libertà',2),
    ('lodevole',3),
    ('lontano',-1),
    ('maestro',2),
    ('magnifico',3),
    ('maledetto',-3),
    ('mancare',1),
    ('massacrare',-3),
    ('meraviglia',3),
    ('meraviglioso',3),
    ('meritare',2),
    ('migliore',3),
    ('misero',-3),
    ('mitico',3),
    ('mondo',1),
    ('monumentale',3),
    ('morale',2),
    ('nettare',3),
    ('nostalgia',2),
    ('nostalgico',1),
    ('occasione',1),
    ('offrire',1),
    ('ok',1),
    ('onore',3),
    ('opportunità',1),
    ('orgoglio',3),
    ('orgoglioso',3),
    ('orribile',-3),
    ('oscar',2),
    ('pace',2),
    ('pagare',-1),
    ('partecipare',1),
    ('particolare',1),
    ('patriottismo',2),
    ('peggiore',-3),
    ('pena',-2),
    ('pensare',1),
    ('perfetto',3),
    ('pessimo',-3),
    ('piacere',2),
    ('piacevole',2),
    ('plastica',-2),
    ('poesia',2),
    ('popolo',1),
    ('portare',1),
    ('possibilità',1),
    ('potente',2),
    ('potere',1),
    ('povero',-2),
    ('preferito',3),
    ('preferire',3),
    ('premura',2),
    ('prendere',1),
    ('presente',1),
    ('presto',1),
    ('previsto',1),
    ('prezioso',3),
    ('problema',-2),
    ('problematico',-2),
    ('prodotto',1),
    ('produrre',1),
    ('profondità',2),
    ('profondo',2),
    ('progetto',1),
    ('protagonista',1),
    ('provare',1),
    ('pubblicità',1),
    ('qualità',2),
    ('raccomandare',1),
    ('raro',2),
    ('razzista',-3),
    ('reale',1),
    ('regalare',1),
    ('rendere',1),
    ('restare',1),
    ('riaprire',1),
    ('ricco',2),
    ('richiesta',1),
    ('ricominciare',1),
    ('ricordare',1),
    ('ricostruire',1),
    ('ridicolo',-3),
    ('riemergere',1),
    ('riguardare',1),
    ('rimanere',1),
    ('rimettere',1),
    ('rinascere',2),
    ('ringraziamento',2),
    ('ringraziare',2),
    ('rinunciare',-1),
    ('ripartenza',1),
    ('ripartire',1),
    ('ripetitivo',-2),
    ('riprendere',1),
    ('riprendersi',1),
    ('rispettare',2),
    ('rispetto',2),
    ('rispondere',1),
    ('risultato',1),
    ('ritornare',2),
    ('ritrovare',2),
    ('riuscire',2),
    ('riuscito',2),
    ('rotto',-2),
    ('rubare',-3),
    ('sacrificio',2),
    ('sano',1),
    ('scandaloso',-3),
    ('scappare',-2),
    ('scappato',-2),
    ('schifezza',-3),
    ('schifo',-3),
    ('schifare',-3),
    ('schifoso',-3),
    ('sconfortare',-2),
    ('sconto',-3),
    ('scorta',1),
    ('seguire',1),
    ('sensibile',2),
    ('sensibilità',2),
    ('senso',1),
    ('sentimento',1),
    ('sentire',1),
    ('sfruttare',-3),
    ('significativo',2),
    ('significato',1),
    ('signore',1),
    ('sincero',2),
    ('smettere',-2),
    ('sociale',1),
    ('soddisfatto',2),
    ('soddisfare',2),
    ('sognare',2),
    ('solidarietà',2),
    ('solo',-1),
    ('sopportare',-2),
    ('sorpresa',1),
    ('sorriso',2),
    ('sostenere',2),
    ('sparire',-2),
    ('speciale',3),
    ('speculazione',-3),
    ('speranza',2),
    ('sperare',1),
    ('spettacolo',3),
    ('spinta',1),
    ('splendido',3),
    ('spronare',1),
    ('squadra',2),
    ('stancare',-2),
    ('storia',1),
    ('straordinario',3),
    ('stufare',-2),
    ('stupendo',3),
    ('stupire',3),
    ('supportare',2),
    ('supporto',2),
    ('tartassare',-3),
    ('tempo',1),
    ('tenere',1),
    ('toccante',2),
    ('togliere',-1),
    ('top',3),
    ('tornare',1),
    ('tossico',-3),
    ('tradizione',1),
    ('trasparenza',2),
    ('triste',-2),
    ('trovare',1),
    ('uguale',-1),
    ('umanità',2),
    ('unico',2),
    ('uomo',1),
    ('uscire',-2),
    ('utile',2),
    ('valore',2),
    ('valere',2),
    ('vantare',2),
    ('vergogna',-3),
    ('vergognare',-3),
    ('vergognarsi',-3),
    ('vergognoso',-3),
    ('vero',2),
    ('vicino',2),
    ('vincere',2),
    ('violato',-3),
    ('viscido',-3),
    ('visionario',2),
    ('volere',1),
    ('wow',3),
    ('andare avanti',2),
    ('andare tutto bene',2),
    ('avere mangiare fior fior di soldo',-3), 
    ('avere rompere',-3),
    ('avere abbastanza',-3),
    ('balsamo per anima',3),
    ('casa dolce casa',2),
    ('cavalcare onda',-3),
    ('ce il fare',2),
    ('ce la fare',2),
    ('contro legge',-3),
    ('distante ma unito',2),
    ('dove essere barilla essere casa',2),
    ('durare in il tempo',3),
    ('essere a il altezza',2),
    ('essere con me',2),
    ('essere più forte di prima',2),
    ('fino a il midollo',2),
    ('forza di natura',3),
    ('gettare il spugna',-2),
    ('giorno migliore',2),
    ('grazie di cuore',3),
    ('grazie infinito',3),
    ('grazie mille',3),
    ('insieme ma lontano',2),
    ('lasciare perdere',-3),
    ('lontano ma vicino',2),
    ('mettere il cuore',3),
    ('migliore a il mondo',3),
    ('non avere dubbio',2),
    ('non avere parola',2),
    ('non vedere ora',3),
    ('numero uno',3),
    ('a il mondo',3), 
    ('parola senza tempo',2),
    ('pelle di oca',3),
    ('per sempre',3),
    ('piangere a dirotto',3),
    ('provare per credere',2),
    ('restare a casa',1),
    ('restare impresso',3),
    ('ripartire da casa',2),
    ('sempre avanti',3),
    ('sempre così',3),
    ('sempre e comunque',3),
    ('sempre e per sempre',3),
    ('sempre e solo',3),
    ('sempre un passo avanti',3),
    ('senza alcuno dubbio',2),
    ('senza senso',-3),
    ('senza tempo',2),
    ('tenere duro',2),
    ('tenere il mano',2),
    ('toccare il cuore',3),
    ('tornare il sorriso',2),
    ('valore aggiunto',2),]

    
emoji = [
    ('1st place medal',3),                               # INIZIO EMOJI --------------------
    ('beating heart',3),
    ('black heart',3),
    ('blue heart',3),
    ('bottle with popping cork',2),
    ('broken heart',2),
    ('cherry blossom',2),
    ('clapping hands',3),
    ('collision',3),
    ('crying face',3),
    ('cup with straw',2),
    ('downcast face with sweat',1),
    ('drooling face',2),
    ('face blowing a kiss',2),
    ('face screaming in fear',2),
    ('face vomiting',-3),
    ('face with symbols on mouth',3),
    ('fearful face',-2),
    ('flexed biceps',3),
    ('folded hands',2),
    ('four leaf clover',3),
    ('frowning face',2),
    ('globe showing Americas',1),
    ('globe showing Asia-Australia',1),
    ('glowing star',2),
    ('green heart',3),
    ('grinning face',2),
    ('grinning face with big eyes',2),
    ('grinning face with sweat',-1),
    ('growing heart',3),
    ('heart suit',3),
    ('heart with arrow',3),
    ('heart with ribbon',3),
    ('heavy heart exclamation',3),
    ('house',2),
    ('hugging face',3),
    ('hundred points',3),
    ('Italy',3),
    ('kiss mark',2),
    ('lady beetle',2),
    ('lipstick',1),
    ('loudly crying face',2),
    ('mouth',1),
    ('nauseated face',-3),
    ('OK hand',2),
    ('oncoming fist',2),
    ('party popper',2),
    ('pensive face',1),
    ('pizza',1),
    ('pleading face',2),
    ('pouting face',-3),
    ('purple heart',3),
    ('rainbow',3),
    ('raised hand',2),
    ('raising hands',2),
    ('red heart',3),
    ('revolving hearts',3),
    ('sad but relieved face',3),
    ('shopping bags',1),
    ('slightly smiling face',2),
    ('smiling face',2),
    ('smiling face with 3 hearts',3),
    ('smiling face with heart-eyes',3),
    ('smiling face with smiling eyes',2),
    ('smiling face with sunglasses',2),
    ('sparkling heart',3),
    ('star-struck',3),
    ('sun',2),
    ('thumbs up',2),
    ('tired face',2),
    ('TOP arrow',3),
    ('trophy',3),
    ('two hearts',3),
    ('victory hand',2),
    ('waving hand',2),
    ('weary face',-2),
    ('winking face',2),
    ('yellow heart',3) ]



negazione =[
    'contro',
    'mai',
    'nessuno',
    'niente',
    'non']


intensificazione =[
    'ancora',
    'assoluto',
    'davvero',
    'decisamente',
    'definitivamente',
    'enorme',
    'finalmente',
    'forte',
    'grande',
    'gran',
    'maggiore',
    'maggior',
    'meravigliosamente',
    'migliore',
    'miglior',
    'molto',
    'ottimo',
    'peggiore',
    'peggior',
    'pienamente',
    'più',
    'semplicemente',
    'sempre',
    'solo',
    'speciale',
    'super',
    'tanto',
    'totale',
    'troppo',
    'tutto',
    'veramente',
    '!']



downtoners =[
    'abbastanza', 
    'meno',
    'po',
    'poco',
    'quasi',
    'senza']


interrogative =[
    'chissà',
    '?']


listaPost = testoTot.split('\r')                # forma una lista, dove ogni elemento è una frase 

print(listaPost)                                #DEBUG


for frase in listaPost:                         # passare attraverso ogni frase

    if frase != '':                             # scartare le frasi vuote [ERRORE]

        print (frase)                           #DEBUG

        polarita = 0                            # per tener trraccia del valore della polarita

        # ---- EMOJI -------------

        for elemento in emoji:

            if (elemento[0] in frase):              # se alcune parola se trova all'interno della frase, somma il valore della polarita

                print('trovata')                    #DEBUG

                conc = frase.count(elemento[0])

                print(elemento[0])

                print(conc)

                polarita += elemento[1]*conc         # somma il valore


        for elemento in polaritaLista:           # scorre la lista delle parole con polarità 

            if (elemento[0] in frase):             # se alcune parola se trova all'interno della frase, somma il valore della polarita

                print('trovata')             #DEBUG

                print(elemento[0])

                polarita += elemento[1]         # somma il valore

            # else:

            #             for elemento in intensificazione:

            #                 if (elemento in frase):             # se alcune parola se trova all'interno della frase, somma il valore della polarita

            #                     print('conseguida')             #DEBUG

            #                     polarita += elemento[1]         # somma il valore

            #                     break


        print('--'+frase+'-- Polarità: '+ str(polarita)+'\n')




# for frase in listaPost:                         # prendi ogni frase del testo

#     print(frase)

#     if frase != '':

#         if frase[0] == '<':

#             print ('ES UN EMOJI')

#             parole = frase[2:len(frase)-2]

#             print(parole)

#             polaritaTotale = 0

#             for c in range(0,len(emoji)):          # va di parola in parola per ogni frase

#                 print(c) 

#                 polarita = 0

#                 for el in emoji:                

#                     if listaTesto[c] == el[0]:

#                         polarita = el[1]

#                         if listaTesto[c-1] in negazione:

#                             polarita = polarita - 1

#                         if listaTesto[c-1] in intensificazione:

#                             polarita = polarita*1.5

#                         if listaTesto[c+1] in intensificazione:

#                             polarita = polarita*1.5

#                 polaritaTotale += polarita

#         else:


#             print ('ES UN EMOJI')

#             listaTesto = frase.split(' ')               # forma una lista con ogni parola della frase


#             print(listaTesto)


#             polaritaTotale = 0

#             for c in range(0,len(listaTesto)):          # va di parola in parola per ogni frase

#                 print(c) 

#                 polarita = 0

#                 for el in polaritaLista:                

#                     if listaTesto[c] == el[0]:

#                         polarita = el[1]

#                         if listaTesto[c-1] in negazione:

#                             polarita = polarita - 1

#                         if listaTesto[c-1] in intensificazione:

#                             polarita = polarita*1.5

#                         if listaTesto[c+1] in intensificazione:

#                             polarita = polarita*1.5

#                 polaritaTotale += polarita

                
#             print('--'+frase+'-- Polarità: '+ str(polaritaTotale)+'\n')

    

