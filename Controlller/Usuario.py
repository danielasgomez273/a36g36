class Usuario:
    def __init__(self, IDUsuario, nombreUsuario, apellidoUsuario, telefonoUsuario, informacionExtraUsuario, fotoPerfilUsuario):
        self.IDUsuario = IDUsuario
        self.nombreUsuario = nombreUsuario
        self.apellidoUsuario = apellidoUsuario
        self.telefonoUsuario = telefonoUsuario
        self.informacionExtraUsuario = informacionExtraUsuario
        self.fotoPerfilUsuario = fotoPerfilUsuario

    def get_IDUsuario(self):
        return self.IDUsuario
    def get_nombreUsuario(self):
        return self.nombreUsuario
    def get_apellidoUsuario(self):
        return self.apellidoUsuario
    def get_telefonoUsuario(self):
        return self.telefonoUsuario
    def get_informacionExtraUsuario(self):
        return self.informacionExtraUsuario
    def get_fotoPerfilUsuario(self):
        return self.fotoPerfilUsuario

    # FUNCIONES A DESARROLLAR
