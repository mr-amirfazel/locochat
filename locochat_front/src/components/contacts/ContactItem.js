import classes from './ContactItem.module.css';
import React from 'react';



export default function ContactItem (props) {
    return (
        <li>
        <div className={classes.contact_item}>
            <p>{props.username}</p>
        </div>
        </li>
    );
}