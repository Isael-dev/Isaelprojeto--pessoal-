import random 

jogada = int(input("ESCOLHA UMA OPÇÃO PLAYER: [0 - PEDRA | 1 - PAPEL | 2 - TESOURA] ")) 
cpu = random.randint(0,2)

#Player ganhar
if jogada == 0 and cpu == 2:
    print("Player Venceu!")
if jogada == 1 and cpu == 0:
    print("PLayer Venceu!")
if jogada== 2 and cpu == 1:
    print("Player Venceu!")

    #CPU ganhar
if jogada == 0 and cpu == 1:
    print("CPU Venceu!")
if jogada == 1 and cpu == 2:
    print("CPU Venceu!")
if jogada == 2 and cpu == 0:
    print("CPU Venceu!")

    #Os dois empataram
if jogada == 0 and cpu == 0:
    print("Empate")
if jogada == 1 and cpu == 1:
    print("Empate")
if jogada == 2 and cpu == 2:
    print("Empate")