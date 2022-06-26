import styleModule from "./NavBar.module.css";
import SignUpModal from "../../components/signupmodal/SignUpModal";
import LogInModal from "../../components/loginmodal/LogInModal";
import React, { useState, useContext } from 'react';
import AuthContext from '../../store/auth-context';
import LogIn from "./LogIn";
import DashBoardNav from "../DashBoardNav";


export default function NavBar() {

  const ctx = useContext(AuthContext)

  
 
  

  return (
  <>
  {!ctx.isLoggedIn && <LogIn />}
  {ctx.isLoggedIn && <DashBoardNav />}
  </>
  ); 
}
