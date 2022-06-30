import  classes from './ActionModal.module.css';
import Button from '@mui/material/Button';
import AuthContext from '../../../store/auth-context';
import React, {useContext} from 'react';

export default function ActionModal(props){

    const ctx = useContext(AuthContext);

    const addFriendHandler = () => {
        fetch("http://localhost:5000/add_friend", {
     
            method: "POST",
            body: JSON.stringify({
              username: ctx.username,
              dst_username: props.username
            }),
             
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then(response => {
           console.log(response)
           response.json().then(data => {
            alert(data.message)
            props.onClose()
           })
          
        })
    }

    const BlockUserHandler = () => {
        fetch("http://localhost:5000/block", {
     
            method: "POST",
            body: JSON.stringify({
              username: ctx.username,
              dst_username: props.username
            }),
             
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then(response => {
            console.log(response)
            response.json().then(data => {
             alert(data.message)
             props.onClose()
            })
           
         })
    }

    return( 
<div>
      <div className={classes.backdrop} onClick={props.onClose}/>
      <div className={classes.modal}>
        <div className="card">
       <header className="card-header">
        <h3 className="text-center">What do you wish to do with {props.username}?</h3>
       </header>
       <div className="d-flex flex-row justify-content-space-around card-body">
       <Button variant="contained" color="success" className="w-50 mx-1" onClick={addFriendHandler}>Add as friend</Button>
       <Button variant="outlined" color="error"className="w-50 mx-1" onClick={BlockUserHandler}>Block</Button>
       </div>
       </div>
      </div>
</div>
);

}