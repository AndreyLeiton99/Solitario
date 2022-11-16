class Carta:

    # Atributos
    # ♠♣♥♦
    numero = ''
    signo = ''
    color = ''
    visible = ''

    # Constructor

    def __init__(self, num, sign, colorr, visiblee):
        self.numero = num
        self.signo = sign
        self.color = colorr
        self.visible = visiblee

    # toString - mostrar cartas

    def __str__(self):
        if(self.numero == '1'):
            return f"As {self.signo}"
        if (self.numero == '11'):
            return f" J {self.signo}"
        if (self.numero == '12'):
            return f" Q {self.signo}"
        if (self.numero == '13'):
            return f" K {self.signo}"
        if (self.numero == '10'):
            return f"10 {self.signo}"

        return f" {self.numero} {self.signo}"
