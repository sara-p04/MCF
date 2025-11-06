import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

#leggere il file e creare un dataframe

df = pd.read_csv ('dati2/ExoplanetsPars_2025.csv', comment='#')
print(df)

#stampi il nome delle colonne

print(df.columns)

#stampare solo le prime 10 righe del dataframe

print(df.head(10))

#produrre un grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale 

massa = df['pl_bmassj']
periodo = df['pl_orbper']

plt.scatter(periodo, massa, color='orchid')

plt.title('Grafico della massa in funzione del periodo orbitale con scala logaritmica')
plt.xlabel('periodo orbitale', fontsize=14)
plt.ylabel('massa', fontsize=14)

plt.xscale('log')
plt.yscale('log')

plt.show()

#produrre un grafico con assi logaritmici della grandezza Rmax^2/mstar in funzione del periodo orbitale

R_max = df['pl_orbsmax']
m_star = df['st_mass']

R_m = R_max*R_max / m_star 

plt.scatter(periodo, R_m, color='orchid')

plt.title('Grafico della massa in funzione del periodo orbitale con scala logaritmica')
plt.xlabel('periodo orbitale', fontsize=14)
plt.ylabel('R_max^2 / m_star', fontsize=14)

plt.xscale('log')
plt.yscale('log')

plt.show()

#produrre un grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale distinguendo gli esopianeti per metodo di scoperta con la relativa leggenda

#selzioniamo i valori del dataframe corrispondenti al metodo di scoperta uguale a Transit e radial velocity

df_t = df.loc[ (df['discoverymethod'] == 'Transit') ]

massa_t = df_t['pl_bmassj']
periodo_t = df_t['pl_orbper']

df_r = df.loc[ (df['discoverymethod'] == 'Radial Velocity') ]

massa_r = df_r['pl_bmassj']
periodo_r = df_r['pl_orbper']

#creiamo il grafico 

plt.scatter(periodo_t, massa_t, color='deepskyblue', alpha=0.4, label='Transit')
plt.scatter(periodo_r, massa_r, color='springgreen', alpha=0.6, label='Radial Velocity')
#titolo grafico
plt.title('grafico periodo orbitale x massa per Transit e Radial Velocity')
#titoli assi
plt.xlabel('periodo orbitale', fontsize=14)
plt.ylabel('massa', fontsize=14)
#scala logaritmica
plt.xscale('log')
plt.yscale('log')
#inseriamo la leggenda
plt.legend(fontsize=12)

plt.show()

#produrre un istogramma sovrapposto della massa del pianeta distinguendol per metodo di scoperta con la legenda
#per poter scegliere i bins e il range dell'istogramma dobbiamo capire quanti dati abbiamo e quale è il range di dati

print('Numero masse_t', massa_t.count())
print('Numero masse_r', massa_r.count())

range_min = min(massa_t.min(), massa_r.min())
range_max = max(massa_t.max(), massa_r.max())

plt.hist(massa_t, bins=80, range=(range_min, range_max), color='red', alpha=0.4, label='Transit')
plt.hist(massa_r, bins=80, range=(range_min, range_max), color='green', alpha=0.6, label='Radial Velocity')
#titolo
plt.title('Istogramma massa dei pianeti', fontsize=12)
plt.legend(fontsize=12)


plt.show()

#produrre lo stesso istogramma per i logaritmi in base 10 della massa

massa_tlog = np.log10(massa_t)
massa_rlog = np.log10(massa_r)

range_minlog = min(massa_tlog.min(), massa_rlog.min())
range_maxlog = max(massa_tlog.max(), massa_rlog.max())

plt.hist(massa_tlog, bins=80, range=(range_minlog, range_maxlog), color='red', alpha=0.4, label='Transit')
plt.hist(massa_rlog, bins=80, range=(range_minlog, range_maxlog), color='green', alpha=0.6, label='Radial Velocity')

#titolo
plt.title('Istogramma log10 delle masse')

#legenda
plt.legend(fontsize=12)

plt.show()

 






