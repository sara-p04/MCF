import pandas as pd 
import matplotlib.pyplot as plt

#leggere il file csv e creare il dataframe pandas corrispondente 

df_file = pd.read_csv ('dati/kplr010666592-2011240104155_slc.csv')

print ( df_file )

#stampi il nome delle colonne del dataframe 

print(df_file.columns)

#produciamo un grafico con il flusso in funzione del tempo ( i dati necessari sono nelle colonne 'TIME' e 'PDCSAP_FLUX' ) 

#creiamo le variabili che utilizzo nelle assi x 

tempo = df_file['TIME'] 
flusso = df_file['PDCSAP_FLUX']
errore = df_file['PDCSAP_FLUX_ERR']

#creazione del grafico 

plt.plot(tempo,flusso)

plt.title('flusso in funzione del tempo')
plt.xlabel('tempo')
plt.ylabel('flusso')

plt.show()

#creazione grafico con i punti del grafico demarcati da un simbolo 

plt.plot(tempo,flusso, 'o' )

plt.title('flusso in funzione del tempo con pallini')
plt.xlabel('tempo')
plt.ylabel('flusso')

plt.show()

#creazione grafico con barre di errore 

plt.errorbar(tempo, flusso, yerr=errore, fmt='o' )

plt.title('flusso in funzione del tempo con barre di errore')
plt.xlabel('tempo')
plt.ylabel('flusso')
plt.savefig('grafico3.png', dpi=300)

plt.show()

#creazione grafico simile ai precedenti selezionando un intervallo temporale in uno dei minimi 

#selezione valori della tabella 
df_minimo = df_file.loc[ (df_file['TIME'] > 954.5) & (df_file['TIME'] < 955.0 )]
print(df_minimo)

tempo_min = df_minimo['TIME'] 
flusso_min = df_minimo['PDCSAP_FLUX']
errore_min = df_minimo['PDCSAP_FLUX_ERR']

#creazione grafico

plt.errorbar(tempo_min, flusso_min, yerr=errore_min, fmt='o' )

plt.title('flusso in funzione del tempo con barre di errore')
plt.xlabel('tempo')
plt.ylabel('flusso')

plt.show()

#creare un grafico come per il punto ma con la selezione del punto 6 mostrata come riquadro 


fig, ax = plt.subplots(figsize=(12,6))

#grafico principale 

ax.errorbar(tempo, flusso, yerr=errore, fmt='o' )

ax.set_title('flusso in funzione del tempo con barre di errore')
ax.set_xlabel('tempo')
ax.set_ylabel('flusso')
ax.set_ylim(1.010*(10**6), 1.030*(10**6))

#grafico interno

ins_ax = ax.inset_axes([0.6, 0.6, 0.3, 0.3])
ins_ax.errorbar(tempo_min, flusso_min, yerr=errore_min, fmt='o', color='orchid')
ins_ax.set_title ( 'zoom sul minimo' ) 





plt.show()





