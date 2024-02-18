from importlib import import_module


def _load_class(module_class):
    qname = module_class.split('.')
    length = len(qname)
    clazz = qname[length - 1]
    module = ""
    for i in range(length - 1):
        module += qname[i] + "."

    module = module.rstrip('.')
    return getattr(import_module(module), clazz)


class Modelo303:

    """Clase que contiene los datos necesarios para generar el modelo 303 trimestral para arrendadores con IVA.

    Attributes:
        ejercicio (int): Ejercicio de la declaración.
        periodo (string): Periodo de la declaración Datos validos: (1T, 2T, 3T o 4T)
        nif_empresa_desarrollo (string): NIF de la empresa de desarrollo. A cumplimentar por las entidades desarrolladoras (EEDD). Máximo 9 caracteres.
        version (string): Versión del programa. Debe consignarse el identificador de la versión del SW desarrollado por la ED. Máximo 4 caracteres.
        nombre_fiscal (string): Apellidos y nombre o Razón social del contribuyente. Máximo 80 caracteres.
        nif_contribuyente: (string): NIF contribuyente. Máximo 9 caracteres.
        base_imponible (float): Importe trimestral del alquiler sin computar el IVA. Tenga en cuenta que la base imponible del IVA en el arrendamiento de un local de negocio está constituida por el importe total de la contraprestación, incluyendo no solo el importe de la renta, sino también las cantidades asimiladas que el arrendador pueda exigir al arrendatario o inquilino. Por ejemplo, los gastos de comunidad, el IBI, los gastos de suministros (calefacción, agua, luz), las reparaciones y otros conceptos análogos. En ocasiones, estos gastos son facturados al arrendador y posteriormente el arrendador los repercute al arrendatario. No se solicitan las cuotas de IVA puesto que se calculan aplicando sobre la base consignada el 21 por 100. Tenga en cuenta que deberá declarar las cuotas de arrendamiento exigibles, hayan sido cobradas o no. En caso de impago podrá recuperar el IVA ingresado cuando se cumplan los requisitos previstos en el artículo 80.Tres o Cuatro, consignando las casillas "Modificación bases y cuotas" (casillas 14 y 15).
        iban (string): IBAN donde domiciliar el pago/devolucion. Sólo se permiten IBAN españoles (que empiecen por ES).
        gastos_bienes_servicios (float): Base imponible trimestral de los gastos en bienes y servicios corrientes.
        iva_gastos_bienes_servicios (float): IVA trimestral soportado deducible de los gastos en bienes y servicios corrientes. Para ser deducible el IVA soportado debe disponer de factura completa emitida a nombre del arrendador. Podrá incluir, entre otras, las cuotas soportadas por suministros, reparaciones y obras de mejora, servicios profesionales independientes (abogados, asesoría, notaría, API) y servicios exteriores (publicidad, limpieza, vigilancia). No son deducibles, ni siquiera parcialmente, las cuotas soportadas en bienes y servicios que se utilicen simultáneamente para esta actividad y para necesidades privadas cuando el precio de adquisición sea inferior a 3.005,06 euros (ordenadores, móviles...). Tampoco son deducibles los gastos en los que no se soporte el impuesto (intereses de préstamo, seguros, IBI o la amortización del inmueble).
        adquisiciones_bienes_inversion (float): Base imponible trimestral de las adquisiciones de bienes de inversión.
        iva_adquisiciones_bienes_inversion (float): IVA trimestral soportado deducible de las adquisiciones de bienes de inversión. Podrá deducir el importe de las cuotas soportadas por la adquisición de bienes de inversión (cuantía superior a 3.005,06 euros) que se utilicen en la actividad de arrendamiento, como el mobiliario. Asimismo, el IVA soportado en la construcción o adquisición del inmueble, las obras de reforma o mejoras. En el caso de que la afectación a la actividad sea parcial, deberá calcularse la parte afecta.
        volumen_anual_operaciones (float): Volumen anual de operaciones. Sólo necesario para 4T.
    """
    _EJERCICIO_MIN = 2023
    _EJERCICIO_MAX = 2024

    def __init__(
        self,
        ejercicio,  # Ejercicio de la declaración
        data        # Datos necesarios para generar del modelo
    ):
        # Validación del ejercicio
        if not self._EJERCICIO_MIN <= ejercicio <= self._EJERCICIO_MAX:
            raise ValueError(f"El ejercicio ha de ser un año entre {Modelo303._EJERCICIO_MIN} y {Modelo303._EJERCICIO_MAX}")

        Ejercicio = _load_class(f"arrendatools.modelo303.ejercicio_{ejercicio}.Ejercicio{ejercicio}")
        # Instanciar la clase del ejercicio correspondiente
        self.generador = Ejercicio(ejercicio, data)

    def generar(self):
        """
        Genera el string para la importación de datos en el modelo 303 de la Agencia Tributaria de España (PRE 303 - Servicio ayuda modelo 303).
        El string generado se puede guardar en un fichero y es compatible con el modelo 303 para la presentación trimestral del IVA.
        """
        return self.generador.generar()
