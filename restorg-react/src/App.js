import './Styles/App.css';
import { BrowserRouter, Link, Route, Redirect, Routes, Router } from 'react-router-dom';
import React from 'react';
import Main from "./Pages/Main.jsx";
import NotFound from './Pages/NotFound';
import Sign from "./Pages/Sign.jsx";
import Register from "./Pages/Register.jsx"
import Board from "./Pages/Board.jsx"
import Menu from "./Pages/Menu.jsx"
import Order from './Pages/Order.jsx';
import Dish from './Pages/DIsh.jsx';
import Payment from './Pages/Payment.jsx'
import DishRegistration from './Pages/DishRegistration.jsx';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Main/>}/>
        <Route path="/menu/:drinks" element={<Menu/>}/>
        <Route path="/menu" element={<Menu/>}/>
        <Route path="/register" element={<Register/>}/>
        <Route path="/register_dish" element={<DishRegistration/>}/>
        <Route path="/sign" element={<Sign/>}/>
        <Route path="/order/:id" element={<Order/>}/>
        <Route path="/board" element={<Board/>}/>
        <Route path="/menu_position/:id/:type" element={<Dish/>}/>
        <Route path="/payment" element={<Payment/>}/>
        <Route path="*" element={<NotFound/>}/>
      </Routes>
    </BrowserRouter>

  );
}

export default App;
