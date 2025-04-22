-- Crear la base de datos
CREATE DATABASE VentasVehiculos;
GO

-- Usar la base de datos
USE VentasVehiculos;
GO

-- Crear la tabla de vehículos
CREATE TABLE Vehiculos (
    VehiculoID INT PRIMARY KEY,
    Marca NVARCHAR(50),
    Modelo NVARCHAR(50),
    Anio INT,
    Precio DECIMAL(18, 2)
);
GO

-- Crear la tabla de clientes
CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY,
    Nombre NVARCHAR(100),
    Email NVARCHAR(100),
    Telefono NVARCHAR(20)
);
GO

-- Crear la tabla de concesionarios
CREATE TABLE Concesionarios (
    ConcesionarioID INT PRIMARY KEY,
    Nombre NVARCHAR(100),
    Direccion NVARCHAR(255),
    Ciudad NVARCHAR(50)
);
GO

-- Crear la tabla de transacciones
CREATE TABLE Transacciones (
    TransaccionID INT PRIMARY KEY,
    VehiculoID INT FOREIGN KEY REFERENCES Vehiculos(VehiculoID),
    ClienteID INT FOREIGN KEY REFERENCES Clientes(ClienteID),
    ConcesionarioID INT FOREIGN KEY REFERENCES Concesionarios(ConcesionarioID),
    FechaVenta DATETIME,
    PrecioVenta DECIMAL(18, 2)
);
GO