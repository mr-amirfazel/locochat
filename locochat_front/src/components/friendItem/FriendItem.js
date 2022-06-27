import classes from './FriendItem.module.css';


export default function FriendItem (props){
    return (
        <li className={`${classes.friendItem}`}>
            <p className="py-2 px-2 ">
                {props.username}
            </p>
        </li>
    );
}