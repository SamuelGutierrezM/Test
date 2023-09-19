class Casa:
    def __init__(self,color,cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
def message_build():
    casa_blanca = Casa('blanca',4)
    return f'Tiene una casa de {casa_blanca.cantidad_pisos} de color {casa_blanca.color}'

def test_message_build():
    assert message_build() == 'Tiene una casa de 4 pisos y de color blanco'
