class Casa:
    def __init__(self,color,cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

def message_build():
    casa_blanca = Casa('blanco',4)
    return f'Tiene una csa de {casa_blanca.cantidad_pisos} de color {casa_blanca.color}'

def test_mesagge_build():
    assert message_build() == 'Tiene una csa de 4 de color blanco'
