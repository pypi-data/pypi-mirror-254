class Ejercicio:

    """
        Abstract class Ejercicio.
        Subclasses need to implement generar method.
    """

    def __init__(self, ejercicio, data):
        """Creates the Ejercicio instance and assign the proper attributes."""
        self._ejercicio = ejercicio
        self.data = data

    def generar(self):
        """Generates the Modelo303 string for the ejercicio"""
        raise NotImplementedError()
