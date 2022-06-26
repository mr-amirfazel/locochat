import classes from './LogInModal.module.css';
import React, { useState, useContext } from 'react';
import AuthContext from '../../store/auth-context';



export default function SignUpModal(props){

  const ctx = useContext(AuthContext)

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const usernameChangeHandler = (event) => {
    setUsername(event.target.value);
 } 
 const passwordChangeHandler = event => {
  setPassword(event.target.value);
} 


const non_empty_entries = () =>{
  console.log(username, password);
  console.log(username.trim() !== '' && password.trim() !== '')
    if(username.trim() !== '' && password.trim() !== ''){
       return true;
    }
    else{
    return false;
  }
 }


const submitHandler = (event) => {
  event.preventDefault();

  if (non_empty_entries()){ 
    fetch("http://localhost:5000/login", {
     
    method: "POST",
    body: JSON.stringify({
      username: username,
      password: password,
    }),
     
    headers: {
        "Content-type": "application/json; charset=UTF-8"
    }
})
.then(response => {
   console.log(response)
   if (response.status === 200){
      response.json().then(data => {
         alert(data.message)
         props.onClose();
         ctx.onLogin(username, password);
      })
   }
   else if (response.status === 400){
      response.json().then(data => {
         alert(data.error)
      })
   }
  
})
}
else
  {
    alert('Please fill all the entries');
  }
    
  }
 



return (
<>
<div className={classes.backdrop} onClick={props.onClose} />
<div className={`card text-center ${classes.modal}`}>
<div className="card-header">
   <h2>Log In</h2>
  </div>
  <div className={`card-body ${classes.content}` }>
    <label className="">Username</label>
    <input type="text" className="" placeholder="Username" onChange={usernameChangeHandler}></input>


    <label className="">Password</label>
    <input type="password" className="" placeholder="password" onChange={passwordChangeHandler}></input>

  </div>
  <div className="card-footer">
    <button className="btn btn-primary w-100" onClick={submitHandler}>Log In</button>
    </div>
</div>
</>
);

}