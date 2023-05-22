import sqlite3
conexionSqlite3 = sqlite3.connect("OneDropBD.db")
cursor = conexionSqlite3.cursor()

##################################### creamos tabla de PRESTADOR MODIFICACION 2023 ##################################### 
cursor.execute('''
            CREATE TABLE IF NOT EXISTS `prestador` (
            `id_prestador` INTEGER NOT NULL,
            `email_prestador` TEXT NOT NULL UNIQUE,
            `contraseña_prestador` TEXT NOT NULL UNIQUE,
            `telefono_prestador` INTEGER NOT NULL UNIQUE,
            `informacion_extra_prestador` TEXT NOT NULL,
            PRIMARY KEY("id_prestador" AUTOINCREMENT) 
            );
   ''')

##################################### creamos tabla de  SERVICIO MODIFICACION 2023 ##################################### 
cursor.execute('''
            CREATE TABLE IF NOT EXISTS "servicio" (
                "id_servicio"	INTEGER NOT NULL,
                "nombre_servicio"	TEXT NOT NULL UNIQUE,
                "descripcion_servicio"	TEXT NOT NULL,
                "sede_servicio"	TEXT NOT NULL,
                "precio_servicio"	REAL NOT NULL,
                "comentarios_servicio"	TEXT NOT NULL,
                "duracion_servicio"	TEXT NOT NULL,
                "id_prestador_fk"	INTEGER NOT NULL,
                PRIMARY KEY("id_servicio" AUTOINCREMENT),
                FOREIGN KEY("id_prestador_fk") REFERENCES "prestador"("id_prestador")
            );
   ''')   

##################################### creamos tabla de  PAQUETE MODIFICACION 2023 ##################################### 
cursor.execute('''
            CREATE TABLE IF NOT EXISTS "paquete" (
                "id_paquete"	INTEGER NOT NULL,
                "duracion_total"	TEXT NOT NULL,
                "precio_total"	REAL NOT NULL,
                "sede_paquete"	TEXT NOT NULL,
                "fecha_seleccionada"  TEXT NOT NULL,     
                PRIMARY KEY("id_paquete" AUTOINCREMENT)
            );
   ''')   

##################################### creamos tabla INTERMEDIA PAQUETE-SERVICIO MODIFICACION 2023 ##################################### 
cursor.execute('''
            CREATE TABLE IF NOT EXISTS "paquete_servicio" (            
                "id_paquete_servicio" INTEGER NOT NULL,
                "id_paquete_fk"	INTEGER NOT NULL,
                "id_servicio_fk" INTEGER NOT NULL,                
                PRIMARY KEY("id_paquete_servicio" AUTOINCREMENT),
                FOREIGN KEY("id_paquete_fk") REFERENCES "paquete"("id_paquete")
                FOREIGN KEY("id_servicio_fk") REFERENCES "servicio"("id_servicio")
            );
   ''') 

##################################### creamos tabla de PACIENTE MODIFICACION 2023 ##################################### 
cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS "paciente" (
                "id_paciente"	INTEGER NOT NULL,
                "nombre_paciente"	TEXT NOT NULL,
                "apellido_paciente"	TEXT NOT NULL,
                "email_paciente"	TEXT NOT NULL UNIQUE,
                "contraseña_paciente"	TEXT NOT NULL UNIQUE,
                "fecha_nacimiento"	TEXT NOT NULL,
                "sexo"	TEXT NOT NULL,
                "telefono_paciente"	INTEGER NOT NULL UNIQUE,
                PRIMARY KEY("id_paciente" AUTOINCREMENT)
            );
    ''')

##################################### creamos tabla de FICHA MEDICA MODIFICACION 2023 ##################################### 
cursor.execute('''
            CREATE TABLE IF NOT EXISTS "ficha_medica" (
                "id_ficha_medica"	INTEGER NOT NULL,
                "tipo_diabetes"	TEXT NOT NULL,
                "terapia_insulina"	TEXT NOT NULL,
                "terapia_pastillas"	TEXT NOT NULL,
                "tipo_glucometro"	TEXT NOT NULL,
                "tipo_sensor"	TEXT NOT NULL,
                "comorbilidades"	TEXT NOT NULL,
                "objetivo_glucosa"	TEXT NOT NULL,
                "id_paciente_fK"	INTEGER NOT NULL UNIQUE,
                FOREIGN KEY("id_paciente_fK") REFERENCES "paciente"("id_paciente"),
                PRIMARY KEY("id_ficha_medica" AUTOINCREMENT)
            );
   ''')

##################################### creamos tabla de REGISTROS DIARIOS MODIFICACION 2023 ##################################### 
cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS "registro_glucemia" (
                "id_registro_glucemia"	INTEGER NOT NULL,
                "fecha_registro"	TEXT NOT NULL,
                "hora_registro"	TEXT NOT NULL,
                "valor_glucemia"	REAL NOT NULL,
                "comentario_registro"	TEXT,
                "id_paciente_fK"	INTEGER NOT NULL,
                PRIMARY KEY("id_registro_glucemia" AUTOINCREMENT),
                FOREIGN KEY("id_paciente_fK") REFERENCES "paciente"("id_paciente")
            );
   ''')

##################################### creamos tabla CARRITO MODIFICACION 2023 ##################################### 
cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS "carrito" (
                "id_carrito"	INTEGER NOT NULL,
                "id_paciente_fk"	INTEGER NOT NULL,
                "estado_carrito"	TEXT NOT NULL,                
                FOREIGN KEY("id_paciente_fk") REFERENCES "paciente"("id_paciente"),
                PRIMARY KEY("id_carrito" AUTOINCREMENT)
            );
   ''')

##################################### creamos tabla FACTURA MODIFICACION 2023 ##################################### 
cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS "factura" (
                "id_factura"	INTEGER NOT NULL,
                "id_carrito_fk"	INTEGER NOT NULL UNIQUE,
                "fecha_completa_factura" TEXT NOT NULL,
                "concepto_factura" TEXT NOT NULL,
                "valor_factura"	REAL NOT NULL,
                "medio_pago_factura"	TEXT NOT NULL,
                "estado_pago"	TEXT NOT NULL,                
                FOREIGN KEY("id_carrito_fk") REFERENCES "carrito"("id_carrito"),
                PRIMARY KEY("id_factura" AUTOINCREMENT)
            );
   ''')

##################################### creamos tabla INTERMEDIA CARRITO-PAQUETE MODIFICACION 2023 ##################################### 
cursor.execute('''
            CREATE TABLE IF NOT EXISTS "carrito_paquete" (            
                "id_carrito_paquete" INTEGER NOT NULL,
                "id_paquete_fk"	INTEGER NOT NULL,
                "id_carrito_fk" INTEGER NOT NULL,                
                PRIMARY KEY("id_carrito_paquete" AUTOINCREMENT),
                FOREIGN KEY("id_paquete_fk") REFERENCES "paquete"("id_paquete")
                FOREIGN KEY("id_carrito_fk") REFERENCES "carrito"("id_carrito")
            );
   ''') 

conexionSqlite3.close()
