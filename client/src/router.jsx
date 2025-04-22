
import { lazy, Suspense } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
// import { action as newVehicleAction } from "./pages/NewVehicle";
// import IndexPage from "./views/IndexPage";
import Layout from "./layouts/Layout";
import EditVehicle from "./pages/EditVehicle";
const IndexPage = lazy(() => import("./pages/Vehicles"));
const NewVehicle = lazy(() => import("./pages/NewVehicle"));
// import FavoritesPage from "./views/FavoritesPage";
// const FavoritesPage = lazy(() => import("./views/FavoritesPage"));

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
            {/* <Route path="/" element={<IndexPage />} index /> */}
            <Route path="/" element={
              <Suspense fallback={
                <div>Cargando...</div>
              }>
                <IndexPage />
              </Suspense>
            } index />
            <Route path="/vehicle/nuevo" element={
                <Suspense fallback={
                  <div>Cargando...</div>
                }>
                  <NewVehicle />
                </Suspense>
              } 
            />
            <Route path="/vehicle/:id/editar" element={
                <Suspense fallback={
                  <div>Cargando...</div>
                }>
                  <EditVehicle />
                </Suspense>
              } 
            />
            <Route path="/eliminando/:id" element={
                <Suspense fallback={
                  <div>Cargando...</div>
                }>
                  <></>
                </Suspense>
              } 
            />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
