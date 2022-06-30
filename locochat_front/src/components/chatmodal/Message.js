import classes from './Message.module.css';
import React, { useState, useEffect, useContext } from 'react';
import AuthContext from '../../store/auth-context';
import DoneSharpIcon from '@mui/icons-material/DoneSharp';
import DoneAllSharpIcon from '@mui/icons-material/DoneAllSharp';
import ThumbUpIcon from '@mui/icons-material/ThumbUp';

export default function Message (props){

    const ctx = useContext(AuthContext);
    const [likes, setLikes] = useState(props.likes);

    const likeMessageFetch = () =>{
        fetch("http://localhost:5000/like", {
            method: "POST",
            body: JSON.stringify({
               username: ctx.username,
               message_ID: props.id
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then(response => {
            if (response.status === 200){
                response.json().then(data => {
                    console.log(data.message);
                })
            }   
        }
        )
    }

    const likeHandler = () => {
        if (!likes.includes(ctx.username)){
            setLikes(prev => [...prev, ctx.username]);
            likeMessageFetch();
        }
       
    }

    
    const sender_is_user = ctx.username === props.sender;



    return (
        <li>
        <div className={`d-flex ${props.sender === ctx.username ? 'flex-row-reverse' : 'flex-row'}`}>
            <div className={classes.Message_box} onClick={likeHandler}>
                <p className={classes.Message_text}>{props.message_content}</p>
                <div className="row d-flex flex-row">
                    <div className="col-12">{props.time}</div>
                </div>
                <div className="row d-flex flex-row">
                    <div className="col-6">{likes.map(like => <ThumbUpIcon />)}</div>
                    <div className="col-6">
                        {sender_is_user && props.seen && <DoneAllSharpIcon />}
                        {sender_is_user && !props.seen && <DoneSharpIcon />}
                    </div>
                </div>
            </div>
        </div>
        </li>
    );
}