import importlib.util        
spec = importlib.util.spec_from_file_location(
  "RegistroConexionSqlite3", "Model\RegistroConexionSqlite3.py")    
ConexionBDregistro = importlib.util.module_from_spec(spec)        
spec.loader.exec_module(ConexionBDregistro)

class Registro:
    def __init__(self, fecha,  glucemia, comentario_registro,IDUsuario):
        self.fecha = fecha
        self.glucemia=glucemia
        self.comentario_registro=comentario_registro
        self.IDUsuario=IDUsuario
        self.IDRegistro=ConexionBDregistro.CreateRegistro(fecha, glucemia, comentario_registro, IDUsuario)

    def get_IDRegistro(self):
        return self.IDRegistro
    def get_IDUsuario(self):
        return self.IDUsuario
    def get_fecha(self):
        return self.fecha
    def get_glucemia(self):
        return self.glucemia
    def get_comentario_registro(self):
        return self.comentario_registro

    # FUNCIONES A DESARROLLAR
    def readAllRegistros():
        pass
    def guardarRegistro():
        pass
    def eliminarRegistro():
        pass
    def modificarRegistro():
        pass
