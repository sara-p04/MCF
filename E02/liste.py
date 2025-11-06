#il programma richiede di creare
# una lista con i nomi dei giorni della settimana 
# una lista con i nomi dei giorni della settimana per il mese di ottobre 
# un dizionare che mette in relazione i giorni della settimana con i giorni del mese 
# stampare la correlazione

#lista con i giorni della settimana

l = [ 'Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica' ]

#il mese di ottobre è costituito da una settimana da merc a dom, 3 settimane intere e una da lunedi a venerdi
#creiamo la lista completa selezionando dalla settimana i giorni necessari 

l_ott = l[2:7] + l*3 + l[0:5]

print ( 'controllo la lista dei giorni della settimana per ottobre')

print ( l_ott ) #questo comando stampa la lista con parentesi e virgole 

#se volessi stampare gli elementi in colonna dovrei utilizzare un ciclo for

#creiamo un dizionario 

ottobre = { i+1 : l_ott[i] for i in range ( len(l_ott) ) }

print ( 'mese di ottobre' ) 

for i in ottobre: 
	print ( '{:d} {: ^10}'.format ( i, ottobre[i] ) )

#con i indico la chiave del dizionario con nome_diz[i] indico il valore 
#Dal momento che il dizionario non può avere chiavi ripetute dobbiamo inserire come tali i numeri e come valori i giorni della settimana 

	
