import numpy as np
tablica = [[0]*27]
for i in range (23):
    wiersz=[0]
    for j in range(24):
        t = 0
        if i==10:
            if j==13:
                wiersz.append(0)
                t=1
                
        if i==11:
            if j>=11 and j<=15:
                if j==13:
                    wiersz.append(0)
                    t=1
                else:
                    wiersz.append(1)
                    t=1

        if i==12 or i==13:
            if j==11 or j==15:
                wiersz.append(1)
                t=1
            if j>11 and j<15:
                wiersz.append(0)
                t=1

        if i==14:
            if j>=11 and j<=15:
                wiersz.append(1)
                t=1
        if t==0:
            x = np.random.randint(0,2)
            wiersz.append(x)

    wiersz.append(wiersz[1])
    wiersz.append(0)
    tablica.append(wiersz)

tablica.append(tablica[1])
tablica.append(tablica[0])

for linia in tablica:
    print(linia)

    
        
