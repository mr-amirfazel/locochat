import classes from './SearchItem.module.css';
import React,{useState} from "react";

export default function SearchItem(props){

    return(
        <li>
            <div  className={`${classes.search_item}`}>
            <h2>{props.user}</h2>
            </div>
        </ li>
    );
}