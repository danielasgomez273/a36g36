from controlador.Usuario import Usuario

class Paciente(Usuario):
    def __init__(self, IDUsuario, nombreUsuario, apellidoUsuario, telefonoUsuario, informacionExtraUsuario, fotoPerfilUsuario):
        super().__init__(IDUsuario, nombreUsuario, apellidoUsuario, telefonoUsuario, informacionExtraUsuario, fotoPerfilUsuario)
        
        # HEREDA GETS de ID, nombre, apellido, telefono, info extra y foto
        # Atributos a sumar??..
    
    # FUNCIONES A DESARROLLAR..

    