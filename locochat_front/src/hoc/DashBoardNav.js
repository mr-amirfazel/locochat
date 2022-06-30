import styleModule from './navBar/NavBar.module.css';
import { Link } from "react-router-dom";
import React, { useState, useContext } from 'react';
import AuthContext from '../store/auth-context';

export default function DashBoardNav () {
    const ctx = useContext(AuthContext)

    const close = () => {
        console.log('arrrrrrrrrr')
        ctx.onLogout()
        console.log(ctx.isLoggedIn)
      }

    const deleteAccount = () => {
        console.log('arrrrrrrrrr')
        ctx.onDeleteAccount()
        // console.log(ctx.isLoggedIn)
      }
    

    return(
        <div className={`${styleModule.navBar}`}>

  <span className={`${styleModule.leftSpan}`}>
  <Link to='/chats'>
 <p>
 <button className={`${styleModule.button}`}>
  Chats 
</button>
</p>
</Link>
<span className={`${styleModule.devider}`}></span>
  <Link to={'/friends'}>
  <p>
  <button className={`${styleModule.button}`}>Friends</button>
  </p>
  </Link>
  <span className={`${styleModule.devider}`}></span>
  <Link to={'/search'}>
  <p>
  <button className={`${styleModule.button}`}>Search</button>
  </p>
  </Link>
  <span className={`${styleModule.devider}`}></span>
  <Link to={'/requests'}>
  <p>
  <button className={`${styleModule.button}`}>Friend requests</button>
  </p>
  </Link>
  <span className={`${styleModule.devider}`}></span>
  <Link to={'/blocks'}>
  <p>
  <button className={`${styleModule.button}`}>Blocked Users</button>
  </p>
  </Link>
  <span className={`${styleModule.devider}`}></span>
  <p>
  <button className={`${styleModule.button}`} onClick={close}>LogOut</button>
  </p>
  <span className={`${styleModule.devider}`}></span>
  <p>
  <button className={`${styleModule.button}`} onClick={deleteAccount}>Delete Account</button>
  </p>

</span>
<p className={`${styleModule.username}`}>
  <Link to={'/'}>
    <button className={`${styleModule.button} text-warning`}>
    {ctx.username}
    </button>
  </Link>
  </p>
</div>
);
}