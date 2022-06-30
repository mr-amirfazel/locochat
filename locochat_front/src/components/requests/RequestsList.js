import classes from './RequestsList.module.css';
import React, { useState, useContext, useEffect } from 'react';
import RequestItem from './RequestItem';
import AuthContext from '../../store/auth-context';


export default function RequestsList (props) {
    
    const [requests, setRequests] = useState([]);
    const [error, setError] = useState('');

    const ctx = useContext(AuthContext)

    let url = '';
    if(props.type === 'SNT'){
        url = "http://localhost:5000/sent_requests"
    }
    else if(props.type === 'REC'){
        url = "http://localhost:5000/received_requests"
    }

    useEffect(() => {
        fetch(url, {
            method: "POST",
            body: JSON.stringify({
              username: ctx.username
            }),
             
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then(response => {
           console.log(response)
           if (response.status === 200){
              response.json().then(data => {
                console.log('dade', data)
                console.log('reqs:', data.requests)
                 setRequests(data.requests)
                 
              })
           }
           else if (response.status === 400){
              response.json().then(data => {
                setError(data.message)
              })
           }
          
        })
    }
    , [])



    return(
        <div className={`${classes.column}`}>
           <div className={`${classes.header}`}>
             <h2>{props.header}</h2>
           </div>
           {error.trim() !== '' && <div className={`${classes.error}`}>{error}</div>}
            {error.trim() === '' &&  <ul className={`${classes.list}`}>
                {requests.map(req => <RequestItem type={props.type} key={req.username} username={req.username} status={req.situation}/>)}
            </ul>}
        </div>
    );
}