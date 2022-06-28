import  classes from './ActionModal.module.css';
import Button from '@mui/material/Button';

export default function ActionModal(props){

    const addFriendHandler = () => {}

    const BlockUserHandler = () => {}
    
    return( 
<div>
      <div className={classes.backdrop} onClick={props.onClose}/>
      <div className={classes.modal}>
        <div className="card">
       <header className="card-header">
        <h3 className="text-center">What do you wish to do with {props.username}?</h3>
       </header>
       <div className="d-flex flex-row justify-content-space-around card-body">
       <Button variant="contained" color="success" className="w-50 mx-1">Add as friend</Button>
       <Button variant="outlined" color="error"className="w-50 mx-1">Block</Button>
       </div>
       </div>
      </div>
</div>
);

}