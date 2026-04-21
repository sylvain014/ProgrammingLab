#Stampare l'equivalente di 538 minuti nel formato 8h:58min 

tempo_in_minuti = 538
ora = tempo_in_minuti // 60
minuti = tempo_in_minuti % 60

print(f'Tempo: {ora}h:{minuti}min')
