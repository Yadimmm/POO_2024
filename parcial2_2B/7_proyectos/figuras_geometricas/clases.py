class Figura:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible

    def estaVisible(self):
        return self.visible

    def ocultar(self):
        self.visible = False

    def mostrar(self):
        self.visible = True

    def mover(self, x, y):
        self.x = x
        self.y = y

    def calcularArea(self):
        pass

    def get_info(self):
        return f"Posición (x, y): ({self.x}, {self.y}), Visible: {self.visible}"


class Rectangulo(Figura):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self.alto = alto
        self.ancho = ancho

    def calcularArea(self):
        return self.alto * self.ancho

    def get_info(self):
        return f"Rectángulo: Área = {self.calcularArea()}, {super().get_info()}"


class Circulo(Figura):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        self.radio = radio

    def calcularArea(self):
        import math
        return math.pi * (self.radio ** 2)

    def get_info(self):
        return f"Círculo: Área = {self.calcularArea()}, {super().get_info()}"