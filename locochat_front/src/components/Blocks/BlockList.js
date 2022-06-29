import classes from './BlockList.module.css';
import React, {useState} from 'react'
import BlockItem from './BlockItem';


export default function BlockList(props) {

    return (
        <ul className={classes.BlockList}>
            {props.blocks.map(block => (
                <BlockItem key={block.username} username={block.username} time={block.time} onDelete={props.onDelete}/>
            ))}
        </ul>
    )
}