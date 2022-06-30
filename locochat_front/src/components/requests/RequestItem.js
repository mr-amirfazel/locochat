import classes from './RequestItem.module.css';
import React, { useState, useContext } from 'react';
import CheckCircleSharpIcon from '@mui/icons-material/CheckCircleSharp';
import HighlightOffSharpIcon from '@mui/icons-material/HighlightOffSharp';


export default function RequestItem (props){

    return (
        <li>
           <div className={`${classes.RequestItem}`}>
            <span>{props.username}</span>
            <span  className={`${classes.status}`}>{props.status}</span>
            {props.type === 'REC' && props.status === 'PENDING' &&
                <div className={`${classes.actions}`}>
                    <CheckCircleSharpIcon />
                    <HighlightOffSharpIcon />
                </div>
            }
           </div>
        </li>
    );
}