import classes from './ContactsList.module.css';
import React, { useState, useEffect, useContext } from 'react';
import AuthContext from '../../store/auth-context';
import ContactItem from './ContactItem';


export default function ContactsList(props) {
    return(
        <ul className={classes.ContactsList}>
           {props.contacts.map(contact =>
           <ContactItem key={contact.token} username={contact.username} token={contact.token} />)}
        </ul>
    );

}