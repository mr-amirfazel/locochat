import classes from './RequestItem.module.css';
import React, { useState, useContext } from 'react';
import CheckCircleSharpIcon from '@mui/icons-material/CheckCircleSharp';
import HighlightOffSharpIcon from '@mui/icons-material/HighlightOffSharp';
import AuthContext from '../../store/auth-context';


export default function RequestItem (props){
    const [status, setStatus] = useState(props.status)

    const ctx = useContext(AuthContext);

    const updateStatusFetch = (sit) => {
        fetch("http://localhost:5000/update_situation", {
            method: "POST",
            body: JSON.stringify({
                src_username: props.username,
                dst_username: ctx.username,
                situation: sit
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then(response => {
            if (response.status === 200){
                response.json().then(data => {
                    console.log('dade',data)
                    console.log('msgs:',data.message)
                    setStatus(data.status)
                })
            }
            
        })
    }

    const acceptHandler = ()=> {
        updateStatusFetch('accepted');

    }

    const rejectHandler = ()=> {
        updateStatusFetch('rejected');

    }


    return (
        <li>
           <div className={`${classes.RequestItem}`}>
            <span>{props.username}</span>
            <span  className={`${classes.status}`}>{status}</span>
            {props.type === 'REC' && status === 'pending' &&
                <div className={`${classes.actions}`}>
                    <CheckCircleSharpIcon  onClick={acceptHandler}/>
                    <HighlightOffSharpIcon onClick={rejectHandler}/>
                </div>
            }
           </div>
        </li>
    );
}