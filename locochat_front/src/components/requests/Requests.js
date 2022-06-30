import classes from './Requests.module.css';
import RequestsList from './RequestsList';
import React, { useState, useContext } from 'react';


export default function Requests (){
    return (
        <div className={`${classes.requests_container}`}>

        <div className={`${classes.requests_inner}`}>
        <div className={`col-5 h-100`}>
            <RequestsList header = "Sent Requests" type ="SNT" />
        </div>
        <div className={`col-5 h-100`}>
            <RequestsList header = "Received Requests" type ="REC"/>
            </div>
        </div>

        </div>

    );
}