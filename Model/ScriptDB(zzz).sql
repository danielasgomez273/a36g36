-- Observacion: las claves foraneas apuntan a las PK. Es decir que la restriccion de FK se hace solo donde esta la FK

-- creamos base de datos
CREATE DATABASE zzz;

-- nos posicionamos en ella
USE zzz;

/* DIVIDIMOS EL CAMINO DE LAS CONEXIONES EN TRES PARTES */


/* ########################################################################## */
-- PRIMERO DESDE SERVICIO A CARRITO

-- creamos tabla de PRESTADOR
CREATE TABLE IF NOT EXISTS `zzz`.`prestador` (
  `idPrestador` INT NOT NULL AUTO_INCREMENT,
  `nombrePrestador` varchar(45) NOT NULL,
  `apellidoPrestador` varchar(45) NOT NULL,
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


/* ########################################################################## */
 -- AHORA CREAMOS LA TABLA PACIENTE, LUEGO FICHA MDICA Y POR ULTIMO REGISTROS DIARIOS. EN ESTAS ULTIMAS DOS NO IMPORTA EL ORDEN EN EL QUE SON CREADAS, YA QUE LAS DOS APUNTAN INDEPENDIENTEMENTE A PACIENTE
  
  
/* CREACION TABLA PACIENTE */
CREATE TABLE `paciente` (
  `idPaciente` int AUTO_INCREMENT,
  `nombrePaciente` varchar(45) NOT NULL,
  `apellidoPaciente` varchar(45) NOT NULL,
  `telefonoPaciente` int NOT NULL UNIQUE,
  `emailPaciente` varchar(45) NOT NULL UNIQUE,
  `contraseñaPaciente` varchar(45) NOT NULL UNIQUE,
  PRIMARY KEY (`idPaciente`)
);

/* CREACION TABLA FICHA MEDICA */
CREATE TABLE `fichaMedica` (
  `idFichaMedica` int NOT NULL AUTO_INCREMENT,
  `tipoDiabetes` int NOT NULL,
  `terapiaInsulina` varchar(60) NOT NULL,
  `terapiaPastillas` varchar(60) NOT NULL,
  `tipoGlucometro` varchar(60) NOT NULL,
  `tipoSensor` varchar(60) NOT NULL,
  `comorbilidad` varchar(90) DEFAULT NULL,
  `objetivoGlucosa` varchar(90) NOT NULL,
  `fechaNacimiento` date NOT NULL,
  `sexo` varchar(45) NOT NULL,
  `idpacienteFK` int NOT NULL,
  PRIMARY KEY (`idFichaMedica`),
  
  
  CONSTRAINT `idPaciente_fichaMedica_FK`
    FOREIGN KEY (`idpacienteFK`)  
    REFERENCES `zzz`.`paciente` (`idPaciente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);


/* CREACION TABLA REGISTROS DIARIOS */
CREATE TABLE `registrosGlucemia` (
  `idRegistrosGlucemia` int NOT NULL AUTO_INCREMENT,
  `fechaRegistro` datetime NOT NULL,
  `valorGlucemia` double NOT NULL,
  `comentarioRegistro` varchar(60) DEFAULT NULL,
  `idpacienteFK` int NOT NULL,
  PRIMARY KEY (`idRegistrosGlucemia`),
  
  UNIQUE INDEX `idRegistrosGlucemia_UNIQUE` (`idRegistrosGlucemia` ASC),
  CONSTRAINT `idPaciente_registrosGlucemia_FK`
    FOREIGN KEY (`idpacienteFK`)  
    REFERENCES `zzz`.`paciente` (`idPaciente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

-- Creamos la tabla carrito.
CREATE TABLE IF NOT EXISTS `zzz`.`carrito` (
  `idCarrito` INT NOT NULL AUTO_INCREMENT,
  `sede` VARCHAR(45) NOT NULL,
  `fechaElegida` DATETIME NOT NULL,
  `monto` INT NOT NULL,
  `idServicioFK` INT NOT NULL,
  `idPacienteFK` INT NOT NULL,
  PRIMARY KEY (`idCarrito`),

  CONSTRAINT `idCarrito_carrito_fk`
    FOREIGN KEY (`idServicioFK`)  -- APUNTA A LA PK DE SERVICIO
    REFERENCES `zzz`.`servicio` (`idServicio`)
	ON DELETE NO ACTION
    ON UPDATE NO ACTION,
 CONSTRAINT `idpaciente_carrito_FK`
    FOREIGN KEY (`idPacienteFK`)
    REFERENCES `zzz`.`paciente` (`idPaciente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
 );

 
/* ########################################################################## */
 -- AHORA VAMOS DE FACTURA ELECTRONICA A NOTA DE CREDITO 

 -- Creamos tabla facturaElectronica
CREATE TABLE `facturaElectronica` (
  `idFactura` INT NOT NULL AUTO_INCREMENT,
  `fecha` datetime NOT NULL,
  `descripcionFactura` VARCHAR(100) NULL,
  `total` double NOT NULL,
  `idCarritoFK` INT NOT NULL,

  PRIMARY KEY (`idFactura`),
  UNIQUE INDEX `idFactura_UNIQUE` (`idFactura` ASC),
  UNIQUE INDEX `idCarrito_UNIQUE` (`idCarritoFK` ASC), 

   CONSTRAINT `idCarritoFk_facturaElectronica_fk`
    FOREIGN KEY (`idCarritoFK`)  -- APUNTA A LA PK DE CARRITO
    REFERENCES `zzz`.`carrito` (`idCarrito`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
  );
  
   -- Creamos tabla notaCredito
CREATE TABLE IF NOT EXISTS `zzz`.`notaCredito` (
  `idNotaCredito` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(150) NOT NULL,
  `fechaNotaCredito` DATETIME NOT NULL,
  `idFacturaFK` INT NOT NULL,
  PRIMARY KEY (`idNotaCredito`),
  UNIQUE INDEX `idNotacredito_UNIQUE` (`idNotaCredito` ASC),

  CONSTRAINT `idFacturaFK_nota_credito_fk`
    FOREIGN KEY (`idFacturaFK`)  -- APUNTA A LA PK DE factura electronica
    REFERENCES `zzz`.`facturaElectronica` (`idFactura`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
  
  );
  
  

