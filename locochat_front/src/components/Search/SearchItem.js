import classes from './SearchItem.module.css';
import ActionModal from './actionmodal/ActionModal';
import React,{useState} from "react";

export default function SearchItem(props){
        const [showModal, setShowModal] =useState(false)

        const showModalHandler = () => {
            console.log("showModalHandler")
            setShowModal(prev => !prev)
        }
    return(
        <>
        {showModal && <ActionModal onClose= {showModalHandler} username = {props.user}/>}
        <li>
            <div  className={`${classes.search_item}`} onClick={showModalHandler}>
            <h2>{props.user}</h2> 
            </div>
        </ li>
        </>
    );
}