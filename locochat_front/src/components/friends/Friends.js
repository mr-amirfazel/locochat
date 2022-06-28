import React,{ useState, useEffect, useContext} from 'react';
import classes from './Friends.module.css';
import AuthContext from '../../store/auth-context';
import FriendList from '../friendlist/FriendList';



export default function Friends () {
    const ctx = useContext(AuthContext);
    const [friends, setFriends] = useState([]);
    const [noFriends, setNoFriends] = useState(false);


    useEffect(() => {
        get_friends();
        
      }, []);

      const get_friends = () => {
        fetch("http://localhost:5000/friends", {
     
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
                console.log(data)
                 setFriends(data.friends)
              })
           }
           else if (response.status === 400){
              response.json().then(data => {
                setNoFriends(true)
              })
           }
          
        })
      }


    return(
        <div className={`${classes.friends}`}>
        <div className={`card my-auto w-100 ${classes.banner}`}>
            <div className={`${classes.header}`}>
            Friends
            </div>
  <div className="card-body">
    {noFriends && <p className="text-danger text-center">No Friends found</p>}
    {!noFriends && <FriendList friends={friends}/>}


  </div>
  <div className="card-footer text-muted h-25  d-flex justify-content-center align-content-center">
    {ctx.username}'s friends
  </div>
        </div>
        </div>
    );
}