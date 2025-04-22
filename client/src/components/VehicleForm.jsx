import React from 'react'

export default function VehicleForm({ searchFilters, handleChange }) {
  return (
    <>
    <div className="mb-4">
            <label
                className="text-gray-800"
                htmlFor="marca"
            >Marca:</label>
            <input 
                id="marca"
                type="text"
                onChange={handleChange}
                value={searchFilters.Marca}
                className="mt-2 block w-full p-3 bg-gray-50"
                placeholder="Marca del vehiculo. ej. BMW"
                name="Marca"
                required
            />
        </div>
        <div className="mb-4">
            <label
                className="text-gray-800"
                htmlFor="price"
            >Modelo:</label>
            <input 
                id="modelo"
                type="text"
                onChange={handleChange}
                value={searchFilters.Modelo}
                className="mt-2 block w-full p-3 bg-gray-50"
                placeholder="Modelo del vehiculo. ej. R1300, F900"
                name="Modelo"
                required
            />
        </div>
        <div className="mb-4">
            <label
                className="text-gray-800"
                htmlFor="anio"
            >Año:</label>
            <input 
                id="anio"
                type="number"
                onChange={handleChange}
                value={searchFilters.Anio}
                className="mt-2 block w-full p-3 bg-gray-50"
                placeholder="Año del vehiculo. ej. 2024, 2023"
                name="Anio"
                required
            />
        </div>
        <div className="mb-4">
            <label
                className="text-gray-800"
                htmlFor="precio"
            >Precio:</label>
            <input 
                id="precio"
                type="number"
                onChange={handleChange}
                value={searchFilters.Precio}
                className="mt-2 block w-full p-3 bg-gray-50"
                placeholder="Precio Producto. ej. 200, 300"
                name="Precio"
                required
            />
        </div>
    </>
  )
}
