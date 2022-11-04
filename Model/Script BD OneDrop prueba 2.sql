/*  CREACION BD */
CREATE DATABASE onedrop;
USE onedrop;

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
  `tarapia_insulina` varchar(60) NOT NULL,
  `terapia_pastillas` varchar(60) NOT NULL,
  `tipo_glucometro` varchar(60) NOT NULL,
  `tipo_sensor` varchar(60) NOT NULL,
  `comorbilidad` varchar(90) DEFAULT NULL,
  `objetivo_glucosa` varchar(90) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `sexo` varchar(45) NOT NULL,
  `idpaciente` int NOT NULL UNIQUE,
  PRIMARY KEY (`idficha_medica`)
);

/* CREACION TABLA REGISTROS DIARIOS */
CREATE TABLE `registros_glucemia` (
  `idregistros_glucemia` int NOT NULL AUTO_INCREMENT,
  `fecha_registro` datetime NOT NULL,
  `valor_glucemia` double NOT NULL,
  `comentario_registro` varchar(60) DEFAULT NULL,
  `idpaciente` int NOT NULL,
  PRIMARY KEY (`idregistros_glucemia`)
);

/* INSERT DATOS */
INSERT INTO paciente VALUES 
(NULL,"David1", "Costa", 26441, "1davidcst2991@gmail.com", "A123123"),
(NULL,"David2", "Costa", 26442, "2davidcst2991@gmail.com", "S12A3123"),
(NULL,"David3", "Costa", 26443, "3davidcst2991@gmail.com", "12S3123"),
(NULL,"David3", "Costa", 26444, "4davidcst2991@gmail.com", "12V3123"),
(NULL,"David5", "Costa", 26445, "5davidcst2991@gmail.com", "DD123123"),
(NULL,"David6", "Costa", 26446, "6davidcst2991@gmail.com", "AAAA123123"),
(NULL,"David7", "Costa", 26447, "7davidcst2991@gmail.com", "SSSS123123"),
(NULL,"David8", "Costa", 26448, "8davidcst2991@gmail.com", "DD12312A3");
SELECT * FROM onedrop.paciente;

INSERT INTO ficha_medica VALUES 
(NULL,1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 1),
(NULL,2, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 2),
(NULL,1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 3),
(NULL,1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 4),
(NULL,2, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 5),
(NULL,1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 6),
(NULL,2, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 7),
(NULL,1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 8);
SELECT * FROM ficha_medica;

INSERT INTO registros_glucemia VALUES
(NULL, "2022-10-01 10:00:00", 0.19, "primera medicion", 1),
(NULL, "2022-10-02 11:00:00", 0.29, "a medicion", 1),
(NULL, "2022-11-03 12:00:00", 0.39, "asc medicion", 1),
(NULL, "2022-02-04 13:00:00", 0.49, "ASD medicion", 2),
(NULL, "2021-03-05 14:00:00", 0.59, "AS medicion", 4),
(NULL, "2021-04-05 15:00:00", 0.19, "pridxamera medicion", 6),
(NULL, "2021-05-06 15:00:00", 0.29, "priadvmera medicion", 1),
(NULL, "2020-06-06 12:00:00", 0.39, "da medicion", 2),
(NULL, "2020-06-04 02:00:00", 0.49, "vd medicion", 5),
(NULL, "2020-07-02 17:00:00", 0.59, "e medicion", 1);
SELECT * FROM registros_glucemia;


/* <<<<<<<<<<<<<<<< CONSULTAS DE PRUEBA  >>>>>>>>>>>>>>>>>>>>>*/

/*  ------ PACIENTE ----- /*
/*  Corrobora que no se puedan ingresar ptes con mismo telefono, mail ni contraseña.. SIN EMBARGO, DEBERIAMOS HACERLO COMO FOREIN K? 
O TABLA INTERMEDIA?? NO SE SIENTE CORRECTO HACERLO ASI...  */
INSERT INTO paciente VALUES 
(NULL,"David1", "Costa", 26441, "1davidcst2991@gmail.com", "A123123");

/*  ------ FICHA MEDICA ----- /*
/* Correspondencia de una ficha medica con un paciente */
SELECT * FROM paciente INNER JOIN ficha_medica ON paciente.idpaciente = ficha_medica.idpaciente
WHERE paciente.idpaciente = 7;
/* Corrobora que no se puedan ingresar fichas hacia el mismo paciente... SIN EMBARGO, DEBERIAMOS HACERLO COMO FOREIN K? 
O TABLA INTERMEDIA?? NO SE SIENTE CORRECTO HACERLO ASI... */
INSERT INTO ficha_medica VALUES 
(NULL,1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 1);
SELECT * FROM ficha_medica;

/*  ------ REGISTROS GLUCEMIA ----- /*
/* PACIENTE 1 TIENE 5 REGISTROS */
SELECT * FROM paciente 
INNER JOIN registros_glucemia ON paciente.idpaciente = registros_glucemia.idpaciente
WHERE paciente.idpaciente = 1;
/* PACIENTE 7 NO TIENE REGISTROS */
SELECT * FROM paciente 
INNER JOIN registros_glucemia ON paciente.idpaciente = registros_glucemia.idpaciente
WHERE paciente.idpaciente = 7;

