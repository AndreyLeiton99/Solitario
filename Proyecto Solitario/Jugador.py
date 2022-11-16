from io import open
import os

class Jugador:
    nickname = ''
    partidasGanadas = 0
    partidasPerdidas = 0

    def __init__(self, nickname, partidasGanadas, partidasPerdidas):
        self.nickname = nickname
        self.partidasGanadas = partidasGanadas
        self.partidasPerdidas = partidasPerdidas

    def __str__(self):
        return f"\n< DATOS JUGADOR >\nNombre: {self.nickname}" \
               f"\nPartidas ganadas: {self.partidasGanadas}" \
               f"\nPartidas perdidas: {self.partidasPerdidas}"
    @classmethod
    def nuevoJugador(cls, nombre, ganadas, perdidas):
        with open(nombre + '.txt','w') as archivo:
            aux = nombre + '\n' + str(ganadas) + '\n' + str(perdidas) + '\n'
            archivo.write(aux)

    @classmethod
    def verificaJugador(cls, player):
        if os.path.isfile(player.nickname + '.txt'):
            print('\nSe ha encontrado un registro con este nombre, cargando datos!')
            with open(player.nickname + '.txt', 'r')as archivo:
                cont = 0
                for linea in archivo:
                    if cont == 0:
                        player.nickname = linea.rstrip()
                    elif cont == 1:
                        player.partidasGanadas = int(linea)
                    elif cont == 2:
                        player.partidasPerdidas = int(linea)
                    else:
                        break
                    cont += 1
        else:
            Jugador.nuevoJugador(player.nickname, player.partidasGanadas, player.partidasPerdidas)
            print('\nJugador creado con éxito!')

    @classmethod
    def calificador(cls, player, ganaPierde):
        if ganaPierde:
            Jugador.nuevoJugador(player.nickname, player.partidasGanadas, player.partidasPerdidas)
            print('\n¡Jugador actualizado!')
        else:
            Jugador.nuevoJugador(player.nickname, player.partidasGanadas, player.partidasPerdidas)
            print('\n¡Jugador actualizado!')

'''
jugador = Jugador('sebas', 0, 0)
Jugador.verificaJugador(jugador)
print(jugador)
#Jugador.nuevoJugador('sebastian','200000','10000') '''