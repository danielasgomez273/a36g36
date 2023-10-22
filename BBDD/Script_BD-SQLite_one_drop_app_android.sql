-- creamos base de datos
-- CREATE DATABASE bd_one_drop;

-- nos posicionamos en ella
-- USE bd_one_drop;

/* CREACION TABLA USUARIO */
            CREATE TABLE IF NOT EXISTS "usuario" (
                "id_usuario"    INTEGER NOT NULL,
                "email_usuario" TEXT NOT NULL UNIQUE,
                "password_usuario"  TEXT NOT NULL UNIQUE,
                PRIMARY KEY("id_usuario" AUTOINCREMENT)
            );
            

/* CREACION TABLA DATOS_USUARIO */
            CREATE TABLE IF NOT EXISTS "datos_usuario" (
                "id_datos_d_usuario"    INTEGER NOT NULL,
                "nombre_d_usuario"  TEXT NOT NULL,
                "apellido_d_usuario"    TEXT NOT NULL,
                "fecha_nacimiento_d_usuario"    DATE NOT NULL,
                "sexo_d_usuario"    TEXT NOT NULL,
                PRIMARY KEY("id_datos_d_usuario" AUTOINCREMENT)
            );           

  
/* CREACION TABLA DATOS_MEDICOS */
            CREATE TABLE IF NOT EXISTS "datos_medicos" (
                "id_datos_medicos"  INTEGER NOT NULL,
                "peso_usuario"  INTEGER NOT NULL,
                "tipo_diabetes_usuario" TEXT NOT NULL,
                "terapia_diabetes_usuario"  TEXT NOT NULL,
                PRIMARY KEY("id_datos_medicos" AUTOINCREMENT)
            );

/* CREACION TABLA REGISTRO PRESION */
            CREATE TABLE IF NOT EXISTS "registro_presion" (
                "id_registro_presion"       INTEGER NOT NULL,
                "cantidad_presion"  FLOAT NOT NULL,
                "fecha_hora_presion"    DATE NOT NULL,
                "comentario_presion"        TEXT,
                "id_datos_medicos_rpr_FK"       INTEGER NOT NULL,

                PRIMARY KEY("id_registro_presion" AUTOINCREMENT)
                FOREIGN KEY("id_datos_medicos_rpr_FK") REFERENCES "datos_medicos"("id_datos_medicos")
            );





/* CREACION TABLA REGISTRO PESO */
            CREATE TABLE IF NOT EXISTS "registro_peso" (
                "id_registro_peso"      INTEGER NOT NULL,
                "cantidad_peso" FLOAT NOT NULL,
                "fecha_hora_peso"   DATE NOT NULL,
                "comentario_peso"       TEXT,
                "id_datos_medicos_rp_FK"        INTEGER NOT NULL,

                PRIMARY KEY("id_registro_peso" AUTOINCREMENT)
                FOREIGN KEY("id_datos_medicos_rp_FK") REFERENCES "datos_medicos"("id_datos_medicos")
            );

/* CREACION TABLA REGISTRO GLUCEMIA */
            CREATE TABLE IF NOT EXISTS "registro_glucemia" (
                "id_registro_glucemia"      INTEGER NOT NULL,
                "cantidad_glucemia"   FLOAT NOT NULL,
                "fecha_hora_glucemia"   DATE NOT NULL,
                "comentario_glucemia"       TEXT,
                "id_datos_medicos_rgl_FK"       INTEGER NOT NULL,

                PRIMARY KEY("id_registro_glucemia" AUTOINCREMENT)
                FOREIGN KEY("id_datos_medicos_rgl_FK") REFERENCES "datos_medicos"("id_datos_medicos")
            );   

/* CREACION TABLA REGISTRO ANALISIS */
            CREATE TABLE IF NOT EXISTS "registro_analisis" (
                "id_registro_analisis"      INTEGER NOT NULL,
                "documento_analisis"    TEXT NOT NULL,
                "fecha_hora_analisis"   DATE NOT NULL,
                "id_datos_medicos_ra_FK"        INTEGER NOT NULL,
                PRIMARY KEY("id_registro_analisis" AUTOINCREMENT)
                FOREIGN KEY("id_datos_medicos_ra_FK") REFERENCES "datos_medicos"("id_datos_medicos")
            );
