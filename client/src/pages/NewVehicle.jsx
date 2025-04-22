import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import api from '../services'
import VehicleForm from '../components/VehicleForm'


export default function NewVehicle() {
    const [searchFilters, setSearchFilters] = useState({
        VehiculoID: '',
        Marca: '',
        Modelo: '',
        Anio: '',
        Precio: ''
      })

      const [loading, setLoading] = useState(false)
      const [error, setError] = useState(false)
      const [message, setMessage] = useState('')

    const handleChange = (e) => {
        setSearchFilters({    
          ...searchFilters,
          [e.target.name]: e.target.value
        })
      }

    const handleSubmit = async (e) => {
        e.preventDefault();
        if(Object.values(searchFilters).includes('')) {
            console.log("Todos los campos son obligatorios");
            // showNotification({
            //     text: "Todos los campos son obligatorios",
            //     error: true
            // })
            return        
        }
        try {
            setLoading(true)
            setError(false)
            await api.post('/vehiculos', searchFilters)
                .then(res => {
                    setLoading(false)
                    setSearchFilters({
                        VehiculoID: '',
                            Marca: '',
                            Modelo: '',
                            Anio: '',
                            Precio: ''
                    })
                    setMessage(res.data.message)
                    console.log(res)
                })
                .catch(err => console.error(err))
        } catch (error) {
            console.error(error)
            setLoading(false)
            setError(true)
            setMessage("Hubo un error al registrar el vehiculo")
        }   

        setTimeout(() => {
            setMessage("")
        }, 3000);
        
    }

    
  return (
    <>
    <div className='flex justify-between'>
      <h2 className='text-2xl font-black text-slate-800 sm:text-4xl'>Agregar Vehiculo</h2>
      <Link
        to="/"
        className="rounded-md bg-blue-600 p-3 text-sm font-bold text-white shadow-sm hover:bg-blue-500"
      >
        Volver a Vehiculos
      </Link>      
    </div>
    <form    
        className="mt-10" 
        onSubmit={handleSubmit}   
    >        
        <div className="mb-4">
            <label
                className="text-gray-800"
                htmlFor="ref"
            >Referencia:</label>
            <input 
                id="ref"
                type="number"
                onChange={handleChange}
                value={searchFilters.VehiculoID}
                className="mt-2 block w-full p-3 bg-gray-50"
                placeholder="Referencia del vehiculo ej : 1234"
                name="VehiculoID"
                required
            />
        </div>
        <VehicleForm 
            searchFilters={searchFilters}
            handleChange={handleChange}
        />
        <input
            type="submit"
            className="mt-5 w-full bg-blue-600 p-2 text-white font-bold text-lg cursor-pointer rounded"
            value={loading ? 'Cargando...' : 'Registrar Vehiculo'}
            disabled={loading}
        />
        {message && (
            <div className={error ? 'mt-2 text-center bg-red-500 text-white p-2 text-sm' : 'mt-2 text-center bg-green-700 text-white p-2 rounded text-sm'}>
                {message}
            </div>
        )}
    </form> 
    </>
  )
}
