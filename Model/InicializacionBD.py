import sqlite3
conexionSqlite3 = sqlite3.connect("crandoBDdePrueba.db")
cursor = conexionSqlite3.cursor()

# creamos tabla de PRESTADOR
cursor.execute('''
            CREATE TABLE IF NOT EXISTS `prestador` (
            `idPrestador` INTEGER NOT NULL,
            `email` TEXT NOT NULL UNIQUE,
            `contraseña` TEXT NOT NULL UNIQUE,
            `telefono` INTEGER NOT NULL UNIQUE,
            `informacionExtra` TEXT NOT NULL,
            PRIMARY KEY("idPrestador" AUTOINCREMENT)
            );
   ''')

# creamos tabla de SERVICIO
cursor.execute('''
            CREATE TABLE IF NOT EXISTS "servicio" (
                "idServicio"	INTEGER NOT NULL,
                "nombreServicio"	INTEGER NOT NULL UNIQUE,
                "descripcion"	TEXT NOT NULL,
                "monto"	REAL NOT NULL,
                "sede"	TEXT NOT NULL,
                "idPrestador"	INTEGER NOT NULL,
                PRIMARY KEY("idServicio" AUTOINCREMENT),
                FOREIGN KEY("idPrestador") REFERENCES "prestador"("idPrestador")
            );
   ''')
   
# creamos tabla de PACIENTE
cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS "paciente" (
                "idpaciente"	INTEGER NOT NULL,
                "nombre_paciente"	TEXT NOT NULL,
                "apellido_paciente"	TEXT NOT NULL,
                "telefono_paciente"	TEXT NOT NULL UNIQUE,
                "email_paciente"	TEXT NOT NULL UNIQUE,
                "contraseña_paciente"	TEXT NOT NULL UNIQUE,
                PRIMARY KEY("idpaciente" AUTOINCREMENT)
            );
    ''')

# creamos tabla de FICHA MEDICA
cursor.execute('''
            CREATE TABLE IF NOT EXISTS "ficha_medica" (
                "idficha_medica"	INTEGER NOT NULL,
                "tipo_diabetes"	INTEGER NOT NULL,
                "terapia_insulina"	TEXT NOT NULL,
                "terapia_pastillas"	TEXT NOT NULL,
                "tipo_glucometro"	TEXT NOT NULL,
                "tipo_sensor"	TEXT NOT NULL,
                "comorbilidad"	TEXT NOT NULL,
                "objetivo_glucosa"	TEXT NOT NULL,
                "fecha_nacimiento"	TEXT NOT NULL,
                "sexo"	TEXT NOT NULL,
                "idpacienteFK"	INTEGER NOT NULL UNIQUE,
                PRIMARY KEY("idficha_medica" AUTOINCREMENT)
                FOREIGN KEY("idpacienteFK") REFERENCES "paciente"("idpaciente")
            );
   ''')

# creamos tabla de REGISTROS DIARIOS
cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS "registros_glucemia" (
                "idregistros_glucemia"	INTEGER NOT NULL,
                "fecha_registro"	TEXT NOT NULL,
                "valor_glucemia"	REAL NOT NULL,
                "comentario_registro"	TEXT,
                "idpacienteFK"	INTEGER NOT NULL,
                PRIMARY KEY("idregistros_glucemia" AUTOINCREMENT),
                FOREIGN KEY("idpacienteFK") REFERENCES "paciente"("idpaciente")
            );
   ''')

# creamos tabla de CARRITO
cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS "carrito" (
                "idCarrito"	INTEGER NOT NULL,
                "sede"	TEXT NOT NULL,
                "fechaElegida"	TEXT NOT NULL,
                "horaElegida"	TEXT NOT NULL,
                "monto"	REAL NOT NULL,
                "idPacienteFK"	INTEGER NOT NULL,
                "idServicioFK"	INTEGER NOT NULL,
                FOREIGN KEY("idPacienteFK") REFERENCES "paciente"("idpaciente"),
                FOREIGN KEY("idServicioFK") REFERENCES "servicio"("idServicio"),
                PRIMARY KEY("idCarrito" AUTOINCREMENT)
            );
   ''')

# creamos tabla de FACTURA ELECTRONICA
cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS "factura_electronica" (
                "idFactura"	INTEGER NOT NULL,
                "fecha"	TEXT NOT NULL,
                "descripcionFactura"	INTEGER,
                "total"	REAL NOT NULL,
                "idCarritoFK"	INTEGER NOT NULL UNIQUE,
                PRIMARY KEY("idFactura" AUTOINCREMENT)
            );
   ''')

# creamos tabla de NOTA DE CREDITO
cursor.execute('''
            CREATE TABLE IF NOT EXISTS "nota_credito" (
                "idNotaCredito"	INTEGER NOT NULL,
                "descripcion"	TEXT NOT NULL,
                "fecha"	TEXT NOT NULL,
                "idFacturaFK"	INTEGER NOT NULL,
                FOREIGN KEY("idFacturaFK") REFERENCES "factura_electronica"("idFactura"),
                PRIMARY KEY("idNotaCredito" AUTOINCREMENT)
            );
   ''')

conexionSqlite3.close()
