def  kumpi_voitti(pelilauta: list):
    print(pelilauta)
    for j in pelilauta:
      for i in j:
        if i==1:
          player1 +=1
        elif i==2:
          player2 +=1
         
m= [
    [0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 0],
    [0, 0, 2, 0, 0, 0, 0, 2, 0],
    [0, 0, 2, 0, 2, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
winner = kumpi_voitti(m)
if winner == 0:
  print(winner)
