import classes from './Contacts.module.css';
import React, { useState, useEffect, useContext } from 'react';
import AuthContext from '../../store/auth-context';
import ContactsList from './ContactsList';

export default function Contacts (){
    const ctx = useContext(AuthContext)
    const [contacts, setContacts] = useState([])
    const [error, setError] = useState('')

    useEffect(() => {
        fetch("http://localhost:5000/contacts", {
     
            method: "POST",
            body: JSON.stringify({
              username: ctx.username
            }),
             
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then(response => {
           console.log(response)
           if (response.status === 200){
              response.json().then(data => {
                console.log(data.contacts)
                 setContacts(data.contacts)
                 setError('')
              })
           }
           else if (response.status === 400){
              response.json().then(data => {
                setError(data.message)
              })
           }
          
        })
    },[])


    return (
        <div className={classes.Contacts}>
            <div className={classes.inner}>
                <h2 className={classes.title}>Contacts</h2>
                <div className={classes.results}>
                    {error.trim() !== '' && <p className={`${classes.error}`}>{error}</p>}
                    {error.trim() === '' && <ContactsList contacts={contacts} />}
                </div>
            </div>
        </div>
    );
}