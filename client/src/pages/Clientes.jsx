import { useEffect, useState } from 'react'
import api from '../services'

const Clientes = () => {
  const [vehiculos, setVehiculos] = useState([])

  useEffect(() => {
    api.get('/vehiculos')
      .then(res => setVehiculos(res.data))
      .catch(err => console.error(err))
  }, [])

  console.log('vehiculos::::', vehiculos)
  return (
    <div>
      <h2 className='text-4xl'>Clientes</h2>
      <ul>
        {vehiculos.map(vehiculo => (
          <li key={vehiculo.VehiculoID}>
            <span className='text-2xl'>{vehiculo.Marca} - {vehiculo.Modelo} - {vehiculo.Anio} - {vehiculo.Precio}</span>
            
          </li>
        ))}
      </ul>
    </div>
  )
}

export default Clientes
