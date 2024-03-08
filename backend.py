import random

#Juego de cartas 21
juego_21 =[]

while True:
    print('Bienvenidos al casino')
    cartas_jugador= random.randint(2,26)
    cartas_dealer= random.randint(2,26)

    #Partida
    while True:
        print('El jugador sacó: ', cartas_jugador, 'El dealer tiene esto: ',cartas_dealer)
        decision_mas_cartas = input('Quiere más cartas? S/N')
        if decision_mas_cartas == 'S':
            cartas_jugador = cartas_jugador + random.randint(1,13)  #añade una carta(con valor entre 1 y 13) a las cartas del jugador
        else:
            
            if cartas_jugador== cartas_dealer:
                print("El dealer es el ganador")
                juego_21.append('Dealer')
                break

            elif cartas_jugador == 21 or (cartas_jugador > cartas_dealer and cartas_jugador < 21):
                print("El jugador es el ganador")
                juego_21.append('Jugador')
                break
            else:
                print("El dealer es el ganador")
                juego_21.append('Dealer')
                break

    pregunta_salir = input("Desea terminar el juego? S/N")
    if pregunta_salir == "S":
        break
    else: 
        print('\n'*20)

print(juego_21)
