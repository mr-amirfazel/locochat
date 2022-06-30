import classes from './ContactItem.module.css';
import React, {useState, useContext, useEffect} from 'react';
import ChatModal from '../chatmodal/ChatModal';
import AuthContext from '../../store/auth-context';



export default function ContactItem (props) {
    
    const [showModal, setShowModal] = useState(false);

    const ctx = useContext(AuthContext);

    const showModalHandler = (e) => {
        setShowModal(prev => !prev)
    }

    


    return (
        <>
        {showModal && <ChatModal type="chat" token={props.token} title={props.username} onClose={showModalHandler}/>}
        <li>
        <div className={classes.contact_item} onClick={showModalHandler}>
            <p>{props.username}</p>
        </div>
        </li>
        </>
    );
}