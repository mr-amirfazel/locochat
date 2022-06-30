import classes from './ChatModal.module.css';
import Message from './Message';
import AuthContext from '../../store/auth-context';
import React, {useState, useContext, useEffect} from 'react';
import TextField from '@mui/material/TextField';
import SendIcon from '@mui/icons-material/Send';


export default function ChatModal(props){
    const [messages, setMessages] = useState([]);
    const [error, setError] =useState('');
    const [content, setContent] = useState('');
    const [fetchReady, setFetchReady] = useState(false);


    const ctx = useContext(AuthContext);

    const fetchMessages = () => {
        fetch("http://localhost:5000/chatroom", {
     
            method: "POST",
            body: JSON.stringify({
              src_username: ctx.username,
              dst_token: props.token
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
                console.log('msgs:',data.messages)
                setMessages(data.messages)
                 
              })
           }
           else if (response.status === 400){
              response.json().then(data => {
                setError(data.message)
              })
           }
          
        })
    }

    const seenMessages = () =>{
        fetch("http://localhost:5000/seen", {
            method: "POST",
            body: JSON.stringify({
               src_username: ctx.username,
               dst_token: props.token
               
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then(response => {
            if (response.status === 200){
                response.json().then(data => {
                    console.log(data.message);
                    setFetchReady(true);
                })
            }   
        }
        )

    }


    useEffect(() => {
        seenMessages();
        // if (fetchReady){
            fetchMessages();
        // }
    }
    ,[])

    const textFieldChangeHandler = (e) => {
        e.preventDefault();
        setContent(e.target.value)
    }

    const sendHandler = (e) => {
        e.preventDefault();
        if (content.length > 0){
            fetch("http://localhost:5000/send_message", {
                method: "POST",
                body: JSON.stringify({
                    src_username: ctx.username,
                    dst_token: props.token,
                    content: content
                }),
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
            })
            .then(response => {
                if (response.status === 200){
                    response.json().then(data => {
                        console.log(data.message);
                        setMessages(prev => [...prev, data.message])
                        setContent('')
                    })
                }   
            }
            )
        }
    }


    return (
        <>
        <div className={classes.backdrop} onClick={props.onClose}/>
        <div className={classes.modal}>
            <div className='card'>
                <div className="card-header bg-info">
                    <h5 className="card-title text-center">{props.title}</h5>
                </div>
                <div className={`card-body`}>
                <div className={classes.inner}>
                    <div className={classes.results}>
                    {error.trim().length ==0 && messages.map(message =>
                        <ul className={classes.list}>
                        <Message key={message.id} id={message.id} sender={message.sender} receiver={message.receiver} message_content={message.message_content} time={message.time} seen={message.seen}
                        likes={message.likes}/>
                        </ul>)}
                    {error.trim().length > 0 && <p className={classes.error}>{error.trim()}</p>}
                    </div>
                </div>
            </div>

            <div class="card-footer">
                    <div className={classes.send_message}>
                        <TextField id="outlined-basic" label="type something..." variant="outlined" value={content} onChange={textFieldChangeHandler} className={`${classes.input}`} />
                        
                        <div className={`${classes.send_icon} text-right` }>
                        <SendIcon onClick={sendHandler}/>
                        </div>
                        
                    </div>
            </div>
            </div>
        </div>
        </>
    );
}