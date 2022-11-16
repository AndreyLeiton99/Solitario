from Mazo import Mazo
from random import shuffle
from Jugador import Jugador
from os import system


class Juego:
    # Escoge el mazo de destino
    @classmethod
    def indicarMovimiento(cls, origen, destino, mazoV1, mazoV2, mazoV3, mazoV4, mazoV5, mazoV6, mazoV7, cantidad,
                          mazoCorazon, mazoDiamante, mazoPica, mazoTrebol, mazoPrincipal):

        if origen == '1':
            if destino == '2':
                Juego.movimiento(mazoV1, mazoV2, cantidad)
            elif destino == '3':
                Juego.movimiento(mazoV1, mazoV3, cantidad)
            elif destino == '4':
                Juego.movimiento(mazoV1, mazoV4, cantidad)
            elif destino == '5':
                Juego.movimiento(mazoV1, mazoV5, cantidad)
            elif destino == '6':
                Juego.movimiento(mazoV1, mazoV6, cantidad)
            elif destino == '7':
                Juego.movimiento(mazoV1, mazoV7, cantidad)
            elif destino == '8':
                Juego.movimientoCorazon(mazoV1, mazoCorazon)
            elif destino == '9':
                Juego.movimientoDiamante(mazoV1, mazoDiamante)
            elif destino == '10':
                Juego.movimientoPica(mazoV1, mazoPica)
            elif destino == '11':
                Juego.movimientoTrebol(mazoV1, mazoTrebol)

        if origen == '2':
            if destino == '1':
                Juego.movimiento(mazoV2, mazoV1, cantidad)
            elif destino == '3':
                Juego.movimiento(mazoV2, mazoV3, cantidad)
            elif destino == '4':
                Juego.movimiento(mazoV2, mazoV4, cantidad)
            elif destino == '5':
                Juego.movimiento(mazoV2, mazoV5, cantidad)
            elif destino == '6':
                Juego.movimiento(mazoV2, mazoV6, cantidad)
            elif destino == '7':
                Juego.movimiento(mazoV2, mazoV7, cantidad)
            elif destino == '8':
                Juego.movimientoCorazon(mazoV2, mazoCorazon)
            elif destino == '9':
                Juego.movimientoDiamante(mazoV2, mazoDiamante)
            elif destino == '10':
                Juego.movimientoPica(mazoV2, mazoPica)
            elif destino == '11':
                Juego.movimientoTrebol(mazoV2, mazoTrebol)

        if origen == '3':
            if destino == '1':
                Juego.movimiento(mazoV3, mazoV1, cantidad)
            elif destino == '2':
                Juego.movimiento(mazoV3, mazoV2, cantidad)
            elif destino == '4':
                Juego.movimiento(mazoV3, mazoV4, cantidad)
            elif destino == '5':
                Juego.movimiento(mazoV3, mazoV5, cantidad)
            elif destino == '6':
                Juego.movimiento(mazoV3, mazoV6, cantidad)
            elif destino == '7':
                Juego.movimiento(mazoV3, mazoV7, cantidad)
            elif destino == '8':
                Juego.movimientoCorazon(mazoV3, mazoCorazon)
            elif destino == '9':
                Juego.movimientoDiamante(mazoV3, mazoDiamante)
            elif destino == '10':
                Juego.movimientoPica(mazoV3, mazoPica)
            elif destino == '11':
                Juego.movimientoTrebol(mazoV3, mazoTrebol)

        if origen == '4':
            if destino == '1':
                Juego.movimiento(mazoV4, mazoV1, cantidad)
            elif destino == '2':
                Juego.movimiento(mazoV4, mazoV2, cantidad)
            elif destino == '3':
                Juego.movimiento(mazoV4, mazoV3, cantidad)
            elif destino == '5':
                Juego.movimiento(mazoV4, mazoV5, cantidad)
            elif destino == '6':
                Juego.movimiento(mazoV4, mazoV6, cantidad)
            elif destino == '7':
                Juego.movimiento(mazoV4, mazoV7, cantidad)
            elif destino == '8':
                Juego.movimientoCorazon(mazoV4, mazoCorazon)
            elif destino == '9':
                Juego.movimientoDiamante(mazoV4, mazoDiamante)
            elif destino == '10':
                Juego.movimientoPica(mazoV4, mazoPica)
            elif destino == '11':
                Juego.movimientoTrebol(mazoV4, mazoTrebol)

        if origen == '5':
            if destino == '1':
                Juego.movimiento(mazoV5, mazoV1, cantidad)
            elif destino == '2':
                Juego.movimiento(mazoV5, mazoV2, cantidad)
            elif destino == '3':
                Juego.movimiento(mazoV5, mazoV3, cantidad)
            elif destino == '4':
                Juego.movimiento(mazoV5, mazoV4, cantidad)
            elif destino == '6':
                Juego.movimiento(mazoV5, mazoV6, cantidad)
            elif destino == '7':
                Juego.movimiento(mazoV5, mazoV7, cantidad)
            elif destino == '8':
                Juego.movimientoCorazon(mazoV5, mazoCorazon)
            elif destino == '9':
                Juego.movimientoDiamante(mazoV5, mazoDiamante)
            elif destino == '10':
                Juego.movimientoPica(mazoV5, mazoPica)
            elif destino == '11':
                Juego.movimientoTrebol(mazoV5, mazoTrebol)

        if origen == '6':
            if destino == '1':
                Juego.movimiento(mazoV6, mazoV1, cantidad)
            elif destino == '2':
                Juego.movimiento(mazoV6, mazoV2, cantidad)
            elif destino == '3':
                Juego.movimiento(mazoV6, mazoV3, cantidad)
            elif destino == '4':
                Juego.movimiento(mazoV6, mazoV4, cantidad)
            elif destino == '5':
                Juego.movimiento(mazoV6, mazoV5, cantidad)
            elif destino == '7':
                Juego.movimiento(mazoV6, mazoV7, cantidad)
            elif destino == '8':
                Juego.movimientoCorazon(mazoV6, mazoCorazon)
            elif destino == '9':
                Juego.movimientoDiamante(mazoV6, mazoDiamante)
            elif destino == '10':
                Juego.movimientoPica(mazoV6, mazoPica)
            elif destino == '11':
                Juego.movimientoTrebol(mazoV6, mazoTrebol)

        if origen == '7':
            if destino == '1':
                Juego.movimiento(mazoV7, mazoV1, cantidad)
            elif destino == '2':
                Juego.movimiento(mazoV7, mazoV2, cantidad)
            elif destino == '3':
                Juego.movimiento(mazoV7, mazoV3, cantidad)
            elif destino == '5':
                Juego.movimiento(mazoV7, mazoV5, cantidad)
            elif destino == '6':
                Juego.movimiento(mazoV7, mazoV6, cantidad)
            elif destino == '4':
                Juego.movimiento(mazoV7, mazoV4, cantidad)
            elif destino == '8':
                Juego.movimientoCorazon(mazoV7, mazoCorazon)
            elif destino == '9':
                Juego.movimientoDiamante(mazoV7, mazoDiamante)
            elif destino == '10':
                Juego.movimientoPica(mazoV7, mazoPica)
            elif destino == '11':
                Juego.movimientoTrebol(mazoV7, mazoTrebol)

        if origen == '8':  # MAZO CORAZON
            if destino == '1':
                Juego.movimiento(mazoCorazon, mazoV1, 1)
            elif destino == '2':
                Juego.movimiento(mazoCorazon, mazoV2, 1)
            elif destino == '3':
                Juego.movimiento(mazoCorazon, mazoV3, 1)
            elif destino == '4':
                Juego.movimiento(mazoCorazon, mazoV4, 1)
            elif destino == '5':
                Juego.movimiento(mazoCorazon, mazoV5, 1)
            elif destino == '6':
                Juego.movimiento(mazoCorazon, mazoV6, 1)
            elif destino == '7':
                Juego.movimiento(mazoCorazon, mazoV7, 1)

        if origen == '9':  # MAZO DIAMANTE
            if destino == '1':
                Juego.movimiento(mazoDiamante, mazoV1, 1)
            elif destino == '2':
                Juego.movimiento(mazoDiamante, mazoV2, 1)
            elif destino == '3':
                Juego.movimiento(mazoDiamante, mazoV3, 1)
            elif destino == '4':
                Juego.movimiento(mazoDiamante, mazoV4, 1)
            elif destino == '5':
                Juego.movimiento(mazoDiamante, mazoV5, 1)
            elif destino == '6':
                Juego.movimiento(mazoDiamante, mazoV6, 1)
            elif destino == '7':
                Juego.movimiento(mazoDiamante, mazoV7, 1)

        if origen == '10':  # MAZO PICA
            if destino == '1':
                Juego.movimiento(mazoPica, mazoV1, 1)
            elif destino == '2':
                Juego.movimiento(mazoPica, mazoV2, 1)
            elif destino == '3':
                Juego.movimiento(mazoPica, mazoV3, 1)
            elif destino == '4':
                Juego.movimiento(mazoPica, mazoV4, 1)
            elif destino == '5':
                Juego.movimiento(mazoPica, mazoV5, 1)
            elif destino == '6':
                Juego.movimiento(mazoPica, mazoV6, 1)
            elif destino == '7':
                Juego.movimiento(mazoPica, mazoV7, 1)

        if origen == '11':  # MAZO TREBLOL
            if destino == '1':
                Juego.movimiento(mazoTrebol, mazoV1, 1)
            elif destino == '2':
                Juego.movimiento(mazoTrebol, mazoV2, 1)
            elif destino == '3':
                Juego.movimiento(mazoTrebol, mazoV3, 1)
            elif destino == '4':
                Juego.movimiento(mazoTrebol, mazoV4, 1)
            elif destino == '5':
                Juego.movimiento(mazoTrebol, mazoV5, 1)
            elif destino == '6':
                Juego.movimiento(mazoTrebol, mazoV6, 1)
            elif destino == '7':
                Juego.movimiento(mazoTrebol, mazoV7, 1)

        if origen == '12':  # ORIGEN MAZO PRINCIPAL
            if destino == '1':
                Juego.movimiento(mazoPrincipal, mazoV1, 1)
            elif destino == '2':
                Juego.movimiento(mazoPrincipal, mazoV2, 1)
            elif destino == '3':
                Juego.movimiento(mazoPrincipal, mazoV3, 1)
            elif destino == '4':
                Juego.movimiento(mazoPrincipal, mazoV4, 1)
            elif destino == '5':
                Juego.movimiento(mazoPrincipal, mazoV5, 1)
            elif destino == '6':
                Juego.movimiento(mazoPrincipal, mazoV6, 1)
            elif destino == '7':
                Juego.movimiento(mazoPrincipal, mazoV7, 1)
            elif destino == '8':
                Juego.movimientoCorazon(mazoPrincipal, mazoCorazon)
            elif destino == '9':
                Juego.movimientoDiamante(mazoPrincipal, mazoDiamante)
            elif destino == '10':
                Juego.movimientoPica(mazoPrincipal, mazoPica)
            elif destino == '11':
                Juego.movimientoTrebol(mazoPrincipal, mazoTrebol)

    # Valida colores y orden descendente
    @classmethod
    def validar(cls, origen, destino):

        print(f"\nValidando... colocar {origen} debajo de {destino}")
        if int(origen.numero) == (int(destino.numero) - 1) and origen.color != destino.color:
            return True
        else:
            if int(origen.numero) != (int(destino.numero) - 1):
                print("No cumple con el orden descendente")
                return False
            elif origen.color == destino.color:
                print("Los colores deben ser diferentes")
                return False

    @classmethod
    def movimiento(cls, origen, destino, cantidad):
        # hacer validacion para que si el mazo destino se encuentra vacio, solo pueda ponerse una K
        # mazoAuxOrigen.pop(len(mazoAuxOrigen) - cantidad) selecciona la carta que debemos comparar para hacer el movimiento
        # por ejemplo, si tenemos las cartas 8 ♠  7 ♥  6 ♥  5 ♠  4 ♥  3 ♠  2 ♦ y queremos mover 5 cartas a otro mazo
        # la que debe validarse es la 6 ♥, porque las demas ya estan validadas

        if cantidad > len(origen):
            print("\n¡Movimiento inválido!")
            print("La cantidad solicitada para mover excede a la del mazo origen")
            return False
        else:
            if len(destino) == 0: #validar si es mazo esta vacio, si lo esta debe de ponerse una K
                if origen[len(origen) - cantidad].numero == '13':
                    print("\n¡Movimiento válido!")
                    for i in range(len(origen)):
                        if i >= (len(origen) - cantidad):
                            carta = origen[i]
                            destino.append(carta)

                    print("¡Cartas movidas!")
                    for i in range(cantidad):
                        origen.pop()
                    return True
                else:
                    print("\n¡Movimiento inválido!\nEl mazo se encuentra vacio, debe colocar una K")
                    return False

            if Juego.validar(origen[len(origen) - cantidad], destino[-1]):
                print("\n¡Movimiento válido!")
                for i in range(len(origen)):
                    if i >= (len(origen) - cantidad):
                        carta = origen[i]
                        destino.append(carta)

                print("¡Cartas movidas!")
                for i in range(cantidad):
                    origen.pop()

            else:
                print("\n¡Movimiento inválido!")

    @classmethod
    def movimientoCorazon(cls, origen, destino):
        if Juego.validarCorazon(origen[-1], destino):
            destino.append(origen.pop())
            print("\n¡Movimiento válido!")
        else:
            print("\n¡Movimiento inválido!")

    @classmethod
    def movimientoDiamante(cls, origen, destino):
        if Juego.validarDiamante(origen[-1], destino):
            destino.append(origen.pop())
            print("\n¡Movimiento válido!")
        else:
            print("\n¡Movimiento inválido!")

    @classmethod
    def movimientoPica(cls, origen, destino):
        if Juego.validarPica(origen[-1], destino):
            destino.append(origen.pop())
            print("\n¡Movimiento válido!")
        else:
            print("\n¡Movimiento inválido!")

    @classmethod
    def movimientoTrebol(cls, origen, destino):
        if Juego.validarTrebol(origen[-1], destino):
            destino.append(origen.pop())
            print("\n¡Movimiento válido!")
        else:
            print("\n¡Movimiento inválido!")

    @classmethod
    def validarCorazon(cls, origen, destino): # MAZO CORAZONES
        if len(destino) == 0:
            if origen.numero == '1' and origen.signo == '♥':
                return True
            else:
                print("\n¡Error! La primera carta debe ser un As de Corazón")
                return False
        else:
            if (int(origen.numero) - 1) == (int(destino[-1].numero)) and origen.signo == '♥':
                return True
            else:
                return False

    @classmethod
    def validarDiamante(cls, origen, destino):  # MAZO DIAMANTES
        if len(destino) == 0:
            if origen.numero == '1' and origen.signo == '♦':
                return True
            else:
                print("\n¡Error! La primera carta debe ser un As de Diamante")
                return False
        else:
            if (int(origen.numero) - 1) == (int(destino[-1].numero)) and origen.signo == '♦':
                return True
            else:
                return False

    @classmethod
    def validarPica(cls, origen, destino):  # MAZO PICAS
        if len(destino) == 0:
            if origen.numero == '1' and origen.signo == '♠':
                return True
            else:
                print("\n¡Error! La primera carta debe ser un As de Picas")
                return False
        else:
            if (int(origen.numero) - 1) == (int(destino[-1].numero)) and origen.signo == '♠':
                return True
            else:
                return False

    @classmethod
    def validarTrebol(cls, origen, destino):  # MAZO TREBOL
        if len(destino) == 0:
            if origen.numero == '1' and origen.signo == '♣':
                return True
            else:
                print("\n¡Error! La primera carta debe ser un As de Trébol")
                return False
        else:
            if (int(origen.numero) - 1) == (int(destino[-1].numero)) and origen.signo == '♣':
                return True
            else:
                return False

    # si uno de los mazos visibles se encuentra vacio, se rellena con una carta del mazo que no se muestra
    @classmethod
    def revisarMazos(cls, V2, V3, V4, V5, V6, V7, I1, I2, I3, I4, I5, I6):
        if len(V2) == 0 and len(I1) != 0: # si el mazo visible se encuentra vacio AND el mazo insisible tiene cartas
            V2.append(I1.pop()) # rellene el mazo
        if len(V3) == 0 and len(I2) != 0:
            V3.append(I2.pop())
        if len(V4) == 0 and len(I3) != 0:
            V4.append(I3.pop())
        if len(V5) == 0 and len(I4) != 0:
            V5.append(I4.pop())
        if len(V6) == 0 and len(I5) != 0:
            V6.append(I5.pop())
        if len(V7) == 0 and len(I6) != 0:
            V7.append(I6.pop())

    # metodo para actualizar las cartas del mazo principal
    @classmethod
    def actualizarMazoPrincipal(cls, mazoPrincipal, cant):
        if len(mazoPrincipal) == 0:
            print("El mazo principal se encuentra vacio\n")
        else:
            try:
                for i in range(int(cant)):
                    mazoPrincipal.insert(0, mazoPrincipal.pop())

                print("¡Mazo principal actualizado!\n")
            except ValueError as ve:
                print("Error, debe digitar un numero en cantidad!\n")

    @classmethod
    def verificarGanador(cls, mazoCorazon, mazoDiamante, mazoPica, mazoTrebol, jugador):
        if len(mazoCorazon) == 13 and len(mazoDiamante) == 13 and len(mazoPica) == 13 and len(mazoTrebol) == 13:
            print(f"\n\n¡FELICIDADES {jugador.nickname.upper()}! HA GANADO EL JUEGO!")
            return True
        else:
            return False

    @classmethod
    def game(cls):
        repetir = '1'
        while repetir == '1':
            # mazos fundacion
            mazoPica = []
            mazoTrebol = []
            mazoDiamante = []
            mazoCorazon = []

            # mazos invisibles
            mazoI1 = []
            mazoI2 = []
            mazoI3 = []
            mazoI4 = []
            mazoI5 = []
            mazoI6 = []

            # mazos visibles
            mazoV1 = []
            mazoV2 = []
            mazoV3 = []
            mazoV4 = []
            mazoV5 = []
            mazoV6 = []
            mazoV7 = []

            # llenado del mazo principal
            mazoPrincipal = []
            Mazo.iniciarMazo(mazoPrincipal)
            shuffle(mazoPrincipal)

            # llenado de mazos invisibles
            for i in range(1):
                Mazo.repartidor(mazoPrincipal, mazoI1)
            # --------------------------------------
            for i in range(2):
                Mazo.repartidor(mazoPrincipal, mazoI2)
            # --------------------------------------
            for i in range(3):
                Mazo.repartidor(mazoPrincipal, mazoI3)
            # --------------------------------------
            for i in range(4):
                Mazo.repartidor(mazoPrincipal, mazoI4)
            # --------------------------------------
            for i in range(5):
                Mazo.repartidor(mazoPrincipal, mazoI5)
            # --------------------------------------
            for i in range(6):
                Mazo.repartidor(mazoPrincipal, mazoI6)
            # --------------------------------------

            # Llenado de cartas visibles

            Mazo.repartidor(mazoPrincipal, mazoV1)
            # --------------------------------------
            Mazo.repartidor(mazoPrincipal, mazoV2)
            # --------------------------------------
            Mazo.repartidor(mazoPrincipal, mazoV3)
            # --------------------------------------
            Mazo.repartidor(mazoPrincipal, mazoV4)
            # --------------------------------------
            Mazo.repartidor(mazoPrincipal, mazoV5)
            # --------------------------------------
            Mazo.repartidor(mazoPrincipal, mazoV6)
            # --------------------------------------
            Mazo.repartidor(mazoPrincipal, mazoV7)
            # --------------------------------------

            print("\n╭──────────────────╮")
            print("|   ¡BIENVENIDO!   |")
            print("╰──────────────────╯\n\n")

            nombre = input("Por favor, digite su nombre: ")

            jugador = Jugador(nombre, 0, 0)
            Jugador.verificaJugador(jugador)
            print(jugador)

            input("\n\nDigite una tecla para continuar...")

            jugar = True
            while jugar:
                Juego.revisarMazos(mazoV2, mazoV3, mazoV4, mazoV5, mazoV6, mazoV7,
                                   mazoI1, mazoI2, mazoI3, mazoI4, mazoI5, mazoI6) # no recibe mazoV1
                print("\n              ┏━━━━━━━━━・✾・━━━━━━━━━┓")
                print("              ✾   S O L I T A R I O  ✾")
                print("              ┗━━━━━━━━━・✾・━━━━━━━━━┛")

                print("\n╭──────────────────╮")
                print  ("|  Mazo principal  |")
                print  ("╰──────────────────╯\n")

                Mazo.toStringMazo(mazoPrincipal)

                print("\n\n╭──────────────────╮")
                print    ("| Mazos fundación  |")
                print    ("╰──────────────────╯\n")

                Mazo.toStringMazo(mazoTrebol)
                print("\n")
                Mazo.toStringMazo(mazoCorazon)
                print("\n")
                Mazo.toStringMazo(mazoPica)
                print("\n")
                Mazo.toStringMazo(mazoDiamante)
                print("\n")

                print("\n╭───────────────────╮")
                print  ("|     M A Z O S     |")
                print  ("╰───────────────────╯\n")

                # se imprimen los mazos invisibles e invisibles correspondientemente
                print("——————————————》Mazo 1《———————————————")
                print(Mazo.toStringMazo(mazoV1))
                print("\n——————————————》Mazo 2《———————————————")
                print(Mazo.toStringMazoInvisible(mazoI1))
                print(Mazo.toStringMazo(mazoV2))
                print("——————————————》Mazo 3《———————————————")
                print(Mazo.toStringMazoInvisible(mazoI2))
                print(Mazo.toStringMazo(mazoV3))
                print("——————————————》Mazo 4《———————————————")
                print(Mazo.toStringMazoInvisible(mazoI3))
                print(Mazo.toStringMazo(mazoV4))
                print("——————————————》Mazo 5《———————————————")
                print(Mazo.toStringMazoInvisible(mazoI4))
                print(Mazo.toStringMazo(mazoV5))
                print("——————————————》Mazo 6《——————————————")
                print(Mazo.toStringMazoInvisible(mazoI5))
                print(Mazo.toStringMazo(mazoV6))
                print("——————————————》Mazo 7《———————————————")
                print(Mazo.toStringMazoInvisible(mazoI6))
                print(Mazo.toStringMazo(mazoV7))

                print(f"\n1- Refrescar el mazo principal"
                      f"\n2- Hacer un movimiento"
                      f"\n3- Terminar juego\n"
                      f"{jugador.nickname}, por favor digite la opcion que desea realizar:")
                opcion = input()

                if opcion == '1':
                    cant = input("¿Cuántas cartas desea actualizar en el mazo principal?\n")
                    Juego.actualizarMazoPrincipal(mazoPrincipal, cant)
                    input("Presiona una tecla para continuar...")
                elif opcion == '2':
                    print("\n\nDigite el movimiento que desea realizar: ")
                    cantidad = 0
                    origen = ''
                    destino = ''
                    print("\n1- Mazo 1\n2- Mazo 2\n3- Mazo 3\n4- Mazo 4\n5- Mazo 5\n6- Mazo 6\n7- Mazo 7\n\n8- Mazo Corazon\n"
                          "9- Mazo Diamantes\n10- Mazo Picas\n11- Mazo Trébol\n\n12- Mazo Principal\n")
                    bandera = True
                    while bandera:
                        try:
                            origen = input("Origen: ")
                            if int(origen) > 12:
                                print("¡Origen no existe!")
                            else:
                                bandera = False
                        except ValueError as ve:
                            print("¡Error! Debe digitar un numero")
                    print("\n1- Mazo 1\n2- Mazo 2\n3- Mazo 3\n4- Mazo 4\n5- Mazo 5\n6- Mazo 6\n7- Mazo 7\n\n8- Mazo Corazon\n"
                          "9- Mazo Diamantes\n10- Mazo Picas\n11- Mazo Trébol\n")
                    bandera = True
                    while bandera:
                        try:
                            destino = input("Destino: ")
                            if int(destino) > 11:
                                print("¡Destino no existe!")
                            else:
                                bandera = False
                        except ValueError as ve:
                            print("¡Error! Debe digitar un numero")
                    bandera = True
                    while bandera:
                        try:
                            cantidad = int(input("\nCantidad: "))
                            bandera = False
                        except ValueError as ve:
                            print("¡Error! Debe digitar un numero")
                    Juego.indicarMovimiento(origen, destino, mazoV1, mazoV2, mazoV3, mazoV4, mazoV5, mazoV6, mazoV7, cantidad,
                                            mazoCorazon, mazoDiamante, mazoPica, mazoTrebol, mazoPrincipal)
                    input("\nPresione una tecla para continuar...\n")
                elif opcion == '3':
                    op = input('¿Seguro que desea terminar el juego? \n 1. Si\n 2. No\n')
                    if op == '1':
                        if Juego.verificarGanador(mazoCorazon, mazoDiamante, mazoPica, mazoTrebol, jugador):
                            print("\n╭──────────────────────╮")
                            print("|   H A  G A N A D O   |")
                            print("╰──────────────────────╯")
                            jugador.partidasGanadas = jugador.partidasGanadas + 1
                            print(jugador)
                            Jugador.calificador(jugador, True)
                            break
                        else:
                            print("\n╭──────────────────────╮")
                            print("|  H A  P E R D I D O  |")
                            print("╰──────────────────────╯")
                            jugador.partidasPerdidas = jugador.partidasPerdidas + 1
                            print(jugador)
                            Jugador.calificador(jugador, False)
                            break
                    elif op == 2:
                        break
                    else:
                        print("¡Opción inválida! Digite una opción correcta")
                else:
                    input("¡Opción inválida!\nPresione una tecla para continuar...")

            repetir = input("\n¿Desea volver a jugar?\n1- Si\n2- No, gracias\nOpción: ")

        print("\n╭──────────────────────────────────────╮")
        print  ("|   ¡GRACIAS POR JUGAR, HASTA LUEGO!   |")
        print  ("╰──────────────────────────────────────╯\n\n")

