import './App.css';
import NavBar from './hoc/navBar/Navbar'
import React, {useContext} from "react";
import ReactDOM from "react-dom/client";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
import Welcome from './layouts/welcome/Welcome'
import AuthContext from './store/auth-context';
import Friends from './components/friends/Friends';
import Search from './components/Search/Search';


function App() {
  const ctx = useContext(AuthContext)
  return (
    <>
     <NavBar />
     {!ctx.isLoggedIn && <Welcome />}
     <Routes>
    {ctx.isLoggedIn && <Route path="/friends" element={<Friends />} />}
    {ctx.isLoggedIn && <Route path="/search" element={<Search />} />}
    </Routes>
    </>  
  )
}

export default App;