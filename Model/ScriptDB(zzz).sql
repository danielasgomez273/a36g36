-- Observacion: las claves foraneas apuntan a las PK. Es decir que la restriccion de FK se hace solo donde esta la FK

-- creamos base de datos
CREATE DATABASE zzz;

-- nos posicionamos en ella
USE zzz;

/* DIVIDIMOS EL CAMINO DE LAS CONEXIONES EN TRES PARTES */


--######################################################################################################
-- PRIMERO DESDE SERVICIO A CARRITO

-- creamos tabla de PRESTADOR
CREATE TABLE IF NOT EXISTS `zzz`.`prestador` (
  `idPrestador` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NOT NULL,
  `contraseña` VARCHAR(45) NOT NULL,
  `telefono` INT NOT NULL,
  `informacionExtra` VARCHAR(151) NOT NULL,
  PRIMARY KEY (`idPrestador`),
  UNIQUE INDEX `idPrestador_UNIQUE` (`idPrestador` ASC),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC),
  UNIQUE INDEX `contraseña_UNIQUE` (`contraseña` ASC));

-- creamos la tabla SERVICIO.
CREATE TABLE IF NOT EXISTS `zzz`.`servicio` (
  `idServicio` INT NOT NULL AUTO_INCREMENT,
  `nombreServicio` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(150) NOT NULL,
  `monto` INT NOT NULL,
  `sede` VARCHAR(45) NOT NULL,
  `idPrestador` INT NOT NULL,
  PRIMARY KEY (`idServicio`),
  UNIQUE INDEX `nombreServicio_UNIQUE` (`nombreServicio` ASC),
  UNIQUE INDEX `idServicio_UNIQUE` (`idServicio` ASC),
  INDEX `idPrestador_idx` (`idPrestador` ASC),
  CONSTRAINT `idPrestador_servicio_fk`
    FOREIGN KEY (`idPrestador`)  -- APUNTA A LA PK DE SERVICIO
    REFERENCES `zzz`.`prestador` (`idPrestador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
  );

-- creamos tabla de con_carrito_servicio (Vamos a borrar esta tabla y carrito con id_servicio directamente)




-- ########################################################################################################
 -- AHORA VAMOS DE NOTA DE CREDITO A CARRITO 


  


  
  
/* CREACION TABLA PACIENTE */
CREATE TABLE `paciente` (
  `idpaciente` int AUTO_INCREMENT,
  `nombre_paciente` varchar(45) NOT NULL,
  `apellido_paciente` varchar(45) NOT NULL,
  `telefono_paciente` int NOT NULL UNIQUE,
  `email_paciente` varchar(45) NOT NULL UNIQUE,
  `contraseña_paciente` varchar(45) NOT NULL UNIQUE,
  PRIMARY KEY (`idpaciente`)
);

/* CREACION TABLA FICHA MEDICA */
CREATE TABLE `ficha_medica` (
  `idficha_medica` int NOT NULL AUTO_INCREMENT,
  `tipo_diabetes` int NOT NULL,
  `terapia_insulina` varchar(60) NOT NULL,
  `terapia_pastillas` varchar(60) NOT NULL,
  `tipo_glucometro` varchar(60) NOT NULL,
  `tipo_sensor` varchar(60) NOT NULL,
  `comorbilidad` varchar(90) DEFAULT NULL,
  `objetivo_glucosa` varchar(90) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `sexo` varchar(45) NOT NULL,
  `idpacienteFK` int NOT NULL,
  PRIMARY KEY (`idficha_medica`),
  
  
  CONSTRAINT `idpaciente_ficha_medica_FK`
    FOREIGN KEY (`idpacienteFK`)  
    REFERENCES `zzz`.`paciente` (`idpaciente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


/* CREACION TABLA REGISTROS DIARIOS */
CREATE TABLE `registros_glucemia` (
  `idregistros_glucemia` int NOT NULL AUTO_INCREMENT,
  `fecha_registro` datetime NOT NULL,
  `valor_glucemia` double NOT NULL,
  `comentario_registro` varchar(60) DEFAULT NULL,
  `idpacienteFK` int NOT NULL,
  PRIMARY KEY (`idregistros_glucemia`),
  
 /* UNIQUE INDEX `idNotacredito_UNIQUE` (`idNotaCredito` ASC), */
  CONSTRAINT `idpaciente_registros_glucemia_FK`
    FOREIGN KEY (`idpacienteFK`)  
    REFERENCES `zzz`.`paciente` (`idpaciente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

-- Creamos la tabla CARRITO.
CREATE TABLE IF NOT EXISTS `zzz`.`carrito` (
  `idCarrito` INT NOT NULL AUTO_INCREMENT,
  `sede` VARCHAR(45) NOT NULL,
  `fechaElegida` DATE NOT NULL,
  `horaElegida` VARCHAR(8) NOT NULL,
  `monto` INT NOT NULL,
  `idUsuarioFK` INT NOT NULL,
  `idServicioFK` INT NOT NULL,
  `idpacienteFK` INT NOT NULL,
  PRIMARY KEY (`idCarrito`),

  CONSTRAINT `idCarrito_carrito_fk`
    FOREIGN KEY (`idServicioFK`)  -- APUNTA A LA PK DE SERVICIO
    REFERENCES `zzz`.`servicio` (`idServicio`)
	ON DELETE NO ACTION
    ON UPDATE NO ACTION,
 CONSTRAINT `idpaciente_carrito_FK`
    FOREIGN KEY (`idpacienteFK`)
    REFERENCES `zzz`.`paciente` (`idpaciente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
 );

 


 -- Creamos tabla factura_electronica
CREATE TABLE `factura_electronica` (
  `idFactura` INT NOT NULL AUTO_INCREMENT,
  `fecha` datetime NOT NULL,
  `descripcionFactura` VARCHAR(100) NULL,
  `total` double NOT NULL,
  `idCarritoFK` INT NOT NULL,

  PRIMARY KEY (`idFactura`),
  UNIQUE INDEX `idFactura_UNIQUE` (`idFactura` ASC),
  UNIQUE INDEX `idCarrito_UNIQUE` (`idCarritoFK` ASC), 

   CONSTRAINT `idCarritoFk_factura_electronica_fk`
    FOREIGN KEY (`idCarritoFK`)  -- APUNTA A LA PK DE CARRITO
    REFERENCES carrito(`idCarrito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
  );
  
   -- Creamos tabla nota_credito
CREATE TABLE IF NOT EXISTS `zzz`.`nota_credito` (
  `idNotaCredito` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(150) NOT NULL,
  `fecha` DATETIME NOT NULL,
  `idFacturaFK` INT NOT NULL,
  PRIMARY KEY (`idNotaCredito`),
  UNIQUE INDEX `idNotacredito_UNIQUE` (`idNotaCredito` ASC),

  CONSTRAINT `idFacturaFK_nota_credito_fk`
    FOREIGN KEY (`idFacturaFK`)  -- APUNTA A LA PK DE factura electronica
    REFERENCES `zzz`.`factura_electronica` (`idFactura`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
  
  );
  

/*  INGRESO DATOS  */
-- Primero creemos un nuevo prestador
INSERT INTO prestador (email,contraseña,telefono,informacionExtra)
VALUES
("prestador01@gmail.com","1234","12345678","Hola me llamo pepe"),
("carlos02@gmail.com","5678","15427583","Hola me llamo carlos"),
("anaa03@gmail.com","1276","174836298","Hola me llamo ana");
SELECT * FROM prestador;

INSERT INTO servicio (nombreServicio,descripcion,monto,sede,idPrestador)
VALUES
("Analisis Clinico GSangre","Analisis de glucosa en sangre",1000,"Colon 1500 CBA",1),
("Consulta Nutricionista (Dra Allende)","Consulta con Dra Allende",1200,"Colon 1500 CBA",2),
("Analisis Clinico Completo","Analisis de sangre completo",1000,"Colon 1500 CBA",3),
("Consulta Diabetologo (DrPerez) ","Consulta con Dr Perez",1200,"Colon 1500 CBA",1),
("Analisis Clinico T4L","Analisis de glucosa en sangre, T4libre",1000,"Colon 1500 CBA",3);
SELECT * FROM servicio;

/* MUESTRA SERVICIOS DE UN PRESTADOR  */
SELECT * FROM servicio INNER JOIN prestador ON servicio.idPrestador = prestador.idPrestador
WHERE prestador.idPrestador =3;


/* INSERT DATOS PACIENTES*/

/* INSERT DATOS */
INSERT INTO paciente (nombre_paciente, apellido_paciente, telefono_paciente, email_paciente, contraseña_paciente) VALUES 
("David1", "Costa", 26441, "1davidcst2991@gmail.com", "A123123"),
("David2", "Costa", 26442, "2davidcst2991@gmail.com", "S12A3123"),
("David3", "Costa", 26443, "3davidcst2991@gmail.com", "12S3123"),
("David3", "Costa", 26444, "4davidcst2991@gmail.com", "12V3123"),
("David5", "Costa", 26445, "5davidcst2991@gmail.com", "DD123123"),
("David6", "Costa", 26446, "6davidcst2991@gmail.com", "AAAA123123"),
("David7", "Costa", 26447, "7davidcst2991@gmail.com", "SSSS123123"),
("David8", "Costa", 26448, "8davidcst2991@gmail.com", "DD12312A3");
SELECT * FROM `zzz`.paciente;

INSERT INTO ficha_medica (tipo_diabetes, terapia_insulina, terapia_pastillas, tipo_glucometro, tipo_sensor, comorbilidad, objetivo_glucosa, fecha_nacimiento, sexo, idpacienteFK) VALUES 
(1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 1),
(2, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 2),
(1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 3),
(1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 4),
(2, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 5),
(1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 6),
(2, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 7),
(1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 8);
SELECT * FROM ficha_medica;


INSERT INTO registros_glucemia (fecha_registro, valor_glucemia, comentario_registro, idpacienteFK) VALUES
("2022-10-01 10:00:00", 0.19, "primera medicion", 1),
("2022-10-02 11:00:00", 0.29, "a medicion", 1),
("2022-11-03 12:00:00", 0.39, "asc medicion", 1),
("2022-02-04 13:00:00", 0.49, "ASD medicion", 2),
("2021-03-05 14:00:00", 0.59, "AS medicion", 4),
("2021-04-05 15:00:00", 0.19, "pridxamera medicion", 6),
("2021-05-06 15:00:00", 0.29, "priadvmera medicion", 1),
("2020-06-06 12:00:00", 0.39, "da medicion", 2),
("2020-06-04 02:00:00", 0.49, "vd medicion", 5),
("2020-07-02 17:00:00", 0.59, "e medicion", 1);
SELECT * FROM registros_glucemia;

SELECT * FROM paciente 
INNER JOIN registros_glucemia ON paciente.idpaciente = registros_glucemia.idpacienteFK
WHERE paciente.idpaciente = 1;

INSERT INTO carrito (sede, fechaElegida, horaElegida, monto, idUsuarioFK, idServicioFK, idpacienteFK) VALUES
("SJ", "2020-07-02", "17:00:00", 150, 1,1,1),
("SJ", "2020-07-02", "17:00:00", 150, 1,1,1),
("SJ", "2020-07-02", "17:00:00", 150, 1,1,1),
("SJ", "2020-07-02", "17:00:00", 150, 1,1,1),
("SJ", "2020-07-02", "17:00:00", 150, 1,1,1);
SELECT * FROM carrito;

/* carrito borrar idUusarioFk, unificar fecha y hora a datetime, borrar campo usuario.. PASAR TODO A CAMEL CASE */

/* AGREGAR CARRITOS, AGREGAR FACTURAS Y HACER CONSULTAS! !!  */
