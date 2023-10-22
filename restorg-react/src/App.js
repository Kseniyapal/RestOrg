import './Styles/App.css';
import { BrowserRouter, Link, Route, Redirect, Routes, Router } from 'react-router-dom';
import React from 'react';
import Main from "./Pages/Main.jsx"
import NotFound from './Pages/NotFound';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/main" element={<Main/>}/>
        <Route path="*" element={<NotFound/>}/>
      </Routes>
    </BrowserRouter>

  );
}

export default App;
