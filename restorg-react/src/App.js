import './Styles/App.css';
import { BrowserRouter, Link, Route, Redirect, Routes, Router } from 'react-router-dom';
import React from 'react';
import Main from "./Pages/Main.jsx";
import NotFound from './Pages/NotFound';
import Sign from "./Pages/Sign.jsx";
import Register from "./Pages/Register.jsx"
import Board from "./Pages/Board.jsx"
import Menu from "./Pages/Menu.jsx"


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Main/>}/>
        <Route path="/menu" element={<Menu/>}/>
        <Route path="/register" element={<Register/>}/>
        <Route path="/sign" element={<Sign/>}/>
        <Route path="/order" element={<Main/>}/>
        <Route path="/sign" element={<Main/>}/>
        <Route path="/board" element={<Board/>}/>
        <Route path="*" element={<NotFound/>}/>
      </Routes>
    </BrowserRouter>

  );
}

export default App;
