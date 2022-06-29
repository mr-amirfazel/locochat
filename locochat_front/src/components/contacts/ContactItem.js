import classes from './ContactItem.module.css';
import React, {useState} from 'react';
import ChatModal from '../chatmodal/ChatModal';



export default function ContactItem (props) {
    
    const [showModal, setShowModal] = useState(false);

    const showModalHandler = () => {
        setShowModal(prev => !prev)
    }


    return (
        <>
        {showModal && <ChatModal title="Contact" onClose={showModalHandler}/>}
        <li>
        <div className={classes.contact_item} onClick={showModalHandler}>
            <p>{props.username}</p>
        </div>
        </li>
        </>
    );
}