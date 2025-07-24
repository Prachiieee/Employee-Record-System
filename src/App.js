import logo from './logo.svg';
import './App.css';
import About from './components/About';
import Home from './components/Home';
import Create from './components/Create';
import Services from './components/Services';
import { Route, Routes } from 'react-router-dom';
import Navi from './components/Navbar.tsx';
import React from 'react';
import Login from './components/login.js';
import Register from './components/register.js';
import Department from './components/Department.jsx';

function App() {
  return (
    <div className="App">
      <Navi/>
      <Routes>
        <Route path="" element={<Home/>}/>
        <Route path="/aboutpage" element={<About/>}/>
        <Route path="/CreateRecord" element={<Create/>}/>
        <Route path="/Services" element={<Services/>}/>
        <Route path="/Login" element={<Login/>}/>
        <Route path="/register" element={<Register/>}/>
        <Route path="/department" element={<Department/>}/>
      </Routes>
    </div>
  );
}

export default App;
