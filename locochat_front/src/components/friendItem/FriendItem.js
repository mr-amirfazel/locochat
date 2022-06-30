import classes from './FriendItem.module.css';
import DeleteIcon from '@mui/icons-material/Delete';
import AuthContext from '../../store/auth-context';
import React, {useContext, useState} from 'react';
import ChatModal from '../chatmodal/ChatModal';


export default function FriendItem (props){

    const [showModal, setShowModal] = useState(false);

    const ctx = useContext(AuthContext);

    const deleteHandler = () =>{
        fetch("http://localhost:5000/unfriend", {
     
            method: "POST",
            body: JSON.stringify({
              username: ctx.username,
              dst_username:props.username
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
                console.log('message:',data.message)
                 
              })
           }
          
        })
        props.onDelete(props.username)
    }

    const showModalHandler = (e) => {
        e.preventDefault();
        setShowModal(prev => !prev)
    }

    return (
        <>
        {showModal && <ChatModal token={props.token} title={props.username} onClose={showModalHandler}/>}
        <li>
            <div className={`${classes.friendItem}`} onClick={showModalHandler}>
            <p className="py-2 px-2 " >
                {props.username}
            </p>
            <div className={`${classes.delete}`} onClick={deleteHandler}>
            <DeleteIcon />
            </div>
            </div>
        </li>
        </>
    );
}