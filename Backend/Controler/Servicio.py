class Servicio:
    def __init__(self, IDServicio,IDPrestador, fecha, duracion, precio, descripcion ):
        self.IDServicio=IDServicio
        self.IDPrestador = IDPrestador
        self.fecha = fecha
        self.duracion = duracion
        self.precio = precio
        self.descripcion = descripcion


    def get_IDServicio(self):
        return self.IDServicio
    def get_IDPrestador(self):
        return self.IDPrestador
    def get_fecha(self):
        return self.fecha
    def get_duracion(self):
        return self.duracion
    def get_precio(self):
        return self.precio
    def get_descripcion(self):
        return self.descripcion

    # FUNCIONES A DESARROLLAR
    def reservarServicio():
        pass
    def eliminarServicio():
        pass