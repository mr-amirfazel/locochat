import classes from './SignUpModal.module.css';
import React, { useState } from 'react';


export default function SignUpModal(props){

 const [username, setUsername] = useState('');
 const [firstname , setFirstname] = useState('');
 const [lastname , setLastname] = useState('');
 const [phonenumber , setPhonenumber] = useState('');
 const [favcolor , setFavcolor] = useState('');
 const [password, setPassword] = useState('');
 const [email, setEmail] = useState('');


 const usernameChangeHandler = (event) => {
    setUsername(event.target.value);
 } 
 const firstnameChangeHandler = (event) => {
    setFirstname(event.target.value);
 } 
 const lastnameChangeHandler = (event) => {
    setLastname(event.target.value);
 } 
 const phonenumberChangeHandler = event => {
    setPhonenumber(event.target.value);
 } 
 const emailChangeHandler = event => {
    setEmail(event.target.value);
 } 
 const passwordChangeHandler = event => {
    setPassword(event.target.value);
 } 
 const favcolorChangeHandler = event => {
    setFavcolor(event.target.value);
 } 

 const non_empty_entries = () =>{
  console.log(username, firstname, lastname, phonenumber, email, password, favcolor);
  console.log(username.trim() !== '' && firstname.trim() !== '' && lastname.trim() !== '' 
  && phonenumber.trim() !== '' && email.trim() !== '' && password.trim() !== '' && favcolor.trim() !== '')
    if(username.trim() !== '' && firstname.trim() !== '' && lastname.trim() !== '' 
    && phonenumber.trim() !== '' && email.trim() !== '' && password.trim() !== '' && favcolor.trim() !== ''){
       return true;
    }
    else{
    return false;
  }
 }

 const submitHandler = (event) => {
  event.preventDefault();

  if (non_empty_entries()){ 
    fetch("http://localhost:5000/signup", {
     
    method: "POST",
    body: JSON.stringify({
      username: username,
      first_name: firstname,
      last_name: lastname,
      phone_number: phonenumber,
      email: email,
      password: password,
      security_question_answer: favcolor
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
      })
   }
   else if (response.status === 400){
      response.json().then(data => {
         alert(data.error)
      })
   }
  
})
// props.onClose();
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
   <h2>Sign Up</h2>
  </div>
  <div className={`card-body ${classes.content}` }>
    <form>
    <label className="">Username</label>
    <input type="text" className="" placeholder="Username" onChange={usernameChangeHandler}></input>

    <label className="">firstname</label>
    <input type="text" className="" placeholder="first name" onChange= {firstnameChangeHandler}></input>

    <label className="">last name</label>
    <input type="text" className="" placeholder="lastname" onChange={lastnameChangeHandler}></input>

    <label className="">phone number</label>
    <input type="number" className="" placeholder="phone number" onChange={phonenumberChangeHandler}></input>

    <label className="">Email</label>
    <input type="email" className="" placeholder="Email" onChange={emailChangeHandler}></input>

    <label className="">Password</label>
    <input type="password" className="" placeholder="password" onChange={passwordChangeHandler}></input>

    <p>what is your favorite color?</p>
    <label className="">Favorite color</label>
    <input type="text" className="" placeholder="Favorite color" onChange={favcolorChangeHandler}></input>
    </form>
  </div>
  <div className="card-footer">
    <input type="submit" className="btn btn-primary w-100" value="Sign Up" onClick={submitHandler}/>
    </div>
</div>
</>
);

}