import classes from './Message.module.css';
import React, { useState, useEffect, useContext } from 'react';
import AuthContext from '../../store/auth-context';
import DoneSharpIcon from '@mui/icons-material/DoneSharp';
import DoneAllSharpIcon from '@mui/icons-material/DoneAllSharp';

export default function Message (props){

    const ctx = useContext(AuthContext);
    return (
        <div className={`d-flex ${props.sender === ctx.username ? 'flex-row-reverse' : 'flex-row'}`}>
            <div className={classes.Message_box}>
                <p className={classes.Message_text}>{props.message_content}</p>
                <div className="row d-flex flex-row">
                    <div className="col-8">{props.time}</div>
                    <div className="col-4">
                        {props.seen && <DoneAllSharpIcon />}
                        {!props.seen && <DoneSharpIcon />}
                    </div>
                </div>
            </div>
        </div>
    );
}