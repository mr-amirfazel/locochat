import styleModule from "./NavBar.module.css";
import { Link } from "react-router-dom";
import SignUpModal from "../../components/signupmodal/SignUpModal";
import LogInModal from "../../components/loginmodal/LogInModal";
import React, { useState } from 'react';


export default function NavBar() {

  const [signup, setsignup] = useState(false);
  const [login, setlogin] = useState(false);
  
  const signup_try = () => {
    setsignup(true);
  }

  const login_try = () => {
    setlogin(true);
  }

  const signup_close = () => {
    setsignup(false);
  }
  const login_close = () => {
    setlogin(false);
  }

  return (
<>
    <div className={`${styleModule.navBar}`}>

      <span className={`${styleModule.leftSpan}`}>
       <p>
       <button className={`${styleModule.button}`} onClick={signup_try}>
        Sign Up 
      </button>
      </p>
      <span className={`${styleModule.devider}`}></span>
        <p>
        <button className={`${styleModule.button}`} onClick={login_try}>Log In</button>
        </p>
       
      </span>
    </div>
    {signup && <SignUpModal onClose={signup_close}/>}
    {login && <LogInModal onClose={login_close}/>}
    </>
  );
}