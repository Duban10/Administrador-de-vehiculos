import React from 'react'
import { Outlet } from 'react-router-dom'

export default function Layout() {
  return (
    <>
    <header className='bg-slate-800'>
      <div className='flex justify-center sm:justify-between mx-auto max-w-6xl items-center'>
        <h1 className='text-2xl py-10 text-center font-extrabold text-white sm:text-4xl'>
            Administrador de Vehiculos
        </h1>
        <img src="/auto.png" alt="Logo Autogermana" className='w-[30%] h-[30%] hidden sm:block filter invert' />
      </div>

    </header>
    <main className='mt-10 mx-auto max-w-6xl p-5 sm:p-10 bg-white shadow'>    
      <Outlet />    
    </main>
    </> 
  )
}
