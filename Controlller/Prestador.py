from controlador.Usuario import Usuario

class Prestador(Usuario):
    def __init__(self,IDUsuario, nombreUsuario, apellidoUsuario, telefonoUsuario, informacionExtraUsuario, fotoPerfilUsuario, comprobanteLegal, especialidad):
        super().__init__(IDUsuario, nombreUsuario, apellidoUsuario, telefonoUsuario, informacionExtraUsuario, fotoPerfilUsuario)
        self.comprobanteLegal = comprobanteLegal
        self.especialidad = especialidad

    # HEREDA GETS de ID, nombre, apellido, telefono, info extra y foto
    def get_comprobanteLegal(self):
        return self.comprobanteLegal
    def get_especialidad(self):
        return self.especialidad
    
    # FUNCIONES A DESARROLLAR
    
