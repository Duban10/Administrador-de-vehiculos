import { formatCurrency } from '../utils'
import { useNavigate, useLocation, useParams, redirect } from 'react-router-dom'
import api from '../services'
import { useState } from 'react'


export default function VehicleDetails({ vehiculo }) {

    const navigate = useNavigate()
    const location = useLocation()
    const { id } = useParams()
    
    const deleteVehicle = async (e) => {
        e.preventDefault()
        try {
            console.log("vehiculo:::: ", vehiculo)
            await api.delete(`/vehiculos/${vehiculo.VehiculoID}`)
            .then(res => {
                console.log(res)                
            })
            .catch(err => console.error(err))
            await api.get('/vehiculos')
                .then(res => console.log(res.data))
                .catch(err => console.error(err))
            navigate(`/`)
        } catch (error) {
            console.error(error)
        }
        
    } 

  return (
    <tr className="border-b ">
        <td className="p-3 text-lg text-gray-800 text-center">
            {vehiculo.Marca}
        </td>
        <td className="p-3 text-lg text-gray-800 text-center">
            {vehiculo.Modelo}
        </td>
        <td className="p-3 text-lg text-gray-800 text-center">
            {vehiculo.Anio}
        </td>
        <td className="p-3 text-lg text-gray-800 text-center">
            {formatCurrency(vehiculo.Precio)}
        </td>
        <td className="p-3 text-lg text-gray-800 ">
            <div className='flex gap-2 items-center'>
                <button
                    onClick={() => navigate(`/vehicle/${vehiculo.VehiculoID}/editar`)}
                    className='bg-blue-600 hover:bg-blue-500 text-white rounded-lg w-full p-2 uppercase font-bold text-xs text-center cursor-pointer'
                >
                    Editar
                </button>
                <button
                    onClick={(e) => {
                        navigate(`/eliminando/${vehiculo.VehiculoID}`)
                        if (!confirm('¿ Está seguro de eliminar ?')) {
                            e.preventDefault()
                            navigate(`/`)
                        }else{                            
                            deleteVehicle(e)
                        }
                    }}
                    className='bg-red-600 hover:bg-red-500 text-white rounded-lg w-full p-2 uppercase font-bold text-xs text-center cursor-pointer'
                >
                    Eliminar
                </button>
            </div>
        </td>
    </tr> 
  )
}
