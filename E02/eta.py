from datetime import datetime, timedelta
data = input ( 'Inserire data di nascita come g-m-a h:m:s ' ) 

data1 = datetime.strptime ( data, "%d-%m-%Y %H:%M:%S" )
print ( 'La mia data di nascita ', data1 )
adesso = datetime.now()
print ( 'Oggi ', adesso )

timediff = adesso - data1
secondi = timediff.total_seconds()
secondis = str(secondi)
giorni = secondi // (3600*24)
giornis = str(giorni)
anni = giorni // 365.25
annis = str(anni)
stringa_tot = 'Anni dalla mia nascita {:s}, Giorni dalla mia nascita {:s}, Secondi dalla mia nascita {:s}'.format(annis, giornis, secondis) 
print (stringa_tot)
