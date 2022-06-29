import classes from './BlockItem.module.css';
import React, { useState, useEffect, useContext } from 'react';
import HighlightOffSharpIcon from '@mui/icons-material/HighlightOffSharp';
import AuthContext from '../../store/auth-context';



export default function BlockItem(props) {

    const ctx = useContext(AuthContext);

    const deleteHandler = () => {
        fetch("http://localhost:5000/unblock", {
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
       if (response.status === 200){
          response.json().then(data => {
            console.log('dade',data)
            console.log('blcks:',data.blocks)
             alert(data.message)
             
          })
       }
      
    })
        props.onDelete(props.username);
    }


    return (
        <li>
            <div className={`${classes.BlockItem}`}>
                <h4>{props.username}</h4>
                <p className={`${classes.time}`}>{props.time}</p>
                <span className={classes.icon} onClick={deleteHandler}><HighlightOffSharpIcon /></span>
            </div> 
        </li>
    );
}