

class Vehiculo:
    def __init__(self, capacidad_personas, capacidad_bicicletas):
        self.capacidad_personas = capacidad_personas
        self.capacidad_bicicletas = capacidad_bicicletas
        self.personas = []

    def agregar_persona(self, persona):
        if len(self.personas) < self.capacidad_personas:
            self.personas.append(persona)