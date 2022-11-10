class Usuario:
    def __init__(self, nombre, apellido, telefono, email, contraseña):
        self.ID = None #Luego se leera este dato desde la BD de paciente o Prestador
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.contraseña = contraseña

    def get_ID(self):
        return self.ID
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_telefono(self):
        return self.telefono
    def get_email(self):
        return self.email
    def get_contraseña(self):
        return self.contraseña

    # FUNCIONES A DESARROLLAR
