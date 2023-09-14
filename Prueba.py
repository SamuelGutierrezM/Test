class Casa:
    def __init__(self,color,cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa('blanco',4)

print(f'Tiene una casa de {casa_blanca.cantidad_pisos} de color {casa_blanca.color}')