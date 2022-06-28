import React from 'react';
import TextField from "@mui/material/TextField";

export default function SearchBar(props){
    return( 
        <TextField
          id="outlined-basic"
          variant="outlined"
          fullWidth
          label="Search"
          onChange={props.onChange}
        />
        )
     
}

