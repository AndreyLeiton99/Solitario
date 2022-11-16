from Carta import Carta
class Mazo:
# Atributos
    mazo = []

# Constructor
    def __init__(self):
        self.mazo = []

# Metodos
    @classmethod
    def toStringMazo(cls, mazo):
        if len(mazo) == 0:
            print("[]", end=" ")
            return ""
        else:
            for i in range(len(mazo)):
                print(mazo[i], end=" ")
            return ""

    # Este metodo imprime ocultas las cartas que asi lo necesiten
    @classmethod
    def toStringMazoInvisible(cls, mazo):
        asteriscos = ''
        for i in range(len(mazo)):
            asteriscos += ' [?]  '
        return asteriscos

    # este metodo recibe el MAZO PRINCIPAL que se va a usar en el juego y lo llena con las 52 cartas
    @classmethod
    def iniciarMazo(cls, mazoPrincipal):
        contador = 1
        # corazones
        while contador <= 13:
            carta = Carta(str(contador), '♥', 'R', 'V')
            mazoPrincipal.append(carta)
            contador += 1

        contador = 1
        # picas
        while contador <= 13:
            carta = Carta(str(contador), '♠', 'N', 'V')
            mazoPrincipal.append(carta)
            contador += 1

        contador = 1
        # diamantes
        while contador <= 13:
            carta = Carta(str(contador), '♦', 'R', 'V')
            mazoPrincipal.append(carta)
            contador += 1

        contador = 1
        # trebol
        while contador <= 13:
            carta = Carta(str(contador), '♣', 'N', 'V')
            mazoPrincipal.append(carta)
            contador += 1

    # este metodo se utiliza para repartir las cartas al incializar el juego
    @classmethod
    def repartidor(cls, mazo1, mazo2):
        aux = mazo1.pop()
        mazo2.append(aux)

