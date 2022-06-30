import classes from './SearchList.module.css';
import React, {useContext} from "react";
import SearchItem from './SearchItem';
import AuthContext from '../../store/auth-context';


export default function SearchList(props) {

    const ctx = useContext(AuthContext);
    const username = ctx.username;

    return (
        <ul className={`${classes.search_list}`}>
            {
            props.users.map(user => (
                ctx.username !== user.username && <SearchItem key={user.username} user={user.username} />
                )
            )}

        </ul>
    )
}