import './App.css';
import NavBar from './hoc/navBar/Navbar'
import React from "react";
import {  BrowserRouter as Router, Routes ,Route } from 'react-router-dom';
import Welcome from './layouts/welcome/Welcome'
import AuthContext from './store/auth-context';

function App() {
  return (
    <>
     <NavBar />
     <Welcome />
    </>
  )
}

export default App;
