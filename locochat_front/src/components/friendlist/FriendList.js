import React, {useState, useEffect} from 'react';
import classes from './FriendList.module.css';
import FriendItem from '../friendItem/FriendItem';


export default function FriendList(props) {

    const [friends, setFriends] = useState(props.friends);

   


    console.log('arrrrr',friends);

    return (
<div className={`${classes.list_container}`}>
    <ul className={`${classes.list}`}>
    {props.friends.map(friend => (<FriendItem key={friend.username} username={friend.username} onDelete={props.onDelete}/>))}
    </ul>
</div>
    );
}