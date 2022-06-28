import classes from './SearchList.module.css';
import React,{useState} from "react";
import SearchItem from './SearchItem';


export default function SearchList(props) {
    return (
        <ul className={`${classes.search_list}`}>
            {
            props.users.map(user => (
                <SearchItem key={user.username} user={user.username} />)
            )}

        </ul>
    )
}