import classes from './Blocks.module.css';
import React, { useState, useEffect, useContext } from 'react';
import AuthContext from '../../store/auth-context';
import BlockList from './BlockList';


export default function Blocks(){
    const [blocks, setBlocks] = useState([]);
    const [error, setError] = useState('');

    const ctx = useContext(AuthContext);

    useEffect(() => {
        fetch("http://localhost:5000/blocks", {
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
            console.log('dade',data)
            console.log('blcks:',data.blocks)
             setBlocks(data.blocks)
             
          })
       }
       else if (response.status === 400){
          response.json().then(data => {
            setError(data.message)
          })
       }
      
    })
    }
    
    , []);

    const deleteHandler = (username) => {
        console.log('delete',username)
        const users = blocks.filter(block => block.username !== username);
        setBlocks(users);
    }
    

    return(
        <div className={classes.Blocks}>
            <header>
                <h2 className="text-center">Blocks List</h2>
            </header>
            <div className={classes.inner}>
            {error.trim() !== '' && <div className={`${classes.error}`}>{error}</div>}
            {error.trim() === '' && <BlockList blocks={blocks} onDelete={deleteHandler} />}
            </div>
        </div>
    );
}