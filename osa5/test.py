def kumpi_voitti(pelilauta: list):
    pelaaja1 = int(0)
    pelaaja2 = int(0)
    for i in range(len(pelilauta)):
        for j in range(len(pelilauta[i])):
            if pelilauta[i][j] == 1:
                pelaaja1 += 1
            elif pelilauta[i][j] == 2:
                pelaaja2 += 1
    if pelaaja1 > pelaaja2:
        return 1
    elif pelaaja2 > pelaaja1:
        return 2
    else:
        return 0
'''
m= [[0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 0],
    [0, 0, 2, 0, 2, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
m= [[0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 0],
    [0, 0, 2, 0, 2, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0]]
'''
m= [[0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0]]

voittaja = kumpi_voitti(m)
if kumpi_voitti== 0:
    print("tasapeli")
else:
    print("pelaaja" + str(voittaja) +" voittaja")
