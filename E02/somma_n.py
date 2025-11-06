#l'esercizio richiede di inserire come input un numero intero n e stampare la somma dei primi n numeri naturali 

n = input ( 'inserisci un numero naturale: ' ) 

#ricordiamo che input genera una variabile di tipo stringa per cui bisogna convertirla per usarla in operazioni matematiche 

N = int(n) #la convertiamo in numero intero

#per fare la somma dei primi n numeri utilizzo un ciclo for in un range da (0, n+1 ) perchè in python l primo estremo è incluso il secondo è escluso

somma = 0

for k in range(0,N+1):
	somma = somma + k
	
#utilizzo la formattazione per esprimere bene il risultato 

print ( 'La somma dei primi {:d} numeri naturali è: {:d}'.format(N,somma))


