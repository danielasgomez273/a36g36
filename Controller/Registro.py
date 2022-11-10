class Registro:
    def __init__(self, IDRegistro, IDUsuario, fecha,  glucemia, notasExtras ):
        self.IDRegistro=IDRegistro
        self.IDUsuario=IDUsuario
        self.fecha = fecha
        self.glucemia=glucemia
        self.notasExtras=notasExtras

    def get_IDRegistro(self):
        return self.IDRegistro
    def get_IDUsuario(self):
        return self.IDUsuario
    def get_fecha(self):
        return self.fecha
    def get_glucemia(self):
        return self.glucemia
    def get_notasExtras(self):
        return self.notasExtras

    # FUNCIONES A DESARROLLAR
    def leerRegistro():
        pass
    def guardarRegistro():
        pass
    def eliminarRegistro():
        pass
    def modificarRegistro():
        pass