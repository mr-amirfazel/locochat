import React from 'react';
import classes from './FriendList.module.css';
import FriendItem from '../friendItem/FriendItem';


export default function FriendList(props) {

    return (
<div className={`${classes.list_container}`}>
    <ul className={`${classes.list}`}>
    {props.friends.map(friend => (<FriendItem key={friend.username} username={friend.username}/>))}
    </ul>
</div>
    );
}