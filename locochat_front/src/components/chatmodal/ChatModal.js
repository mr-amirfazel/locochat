import classes from './ChatModal.module.css';
import Message from './Message';


export default function ChatModal(props){
    return (
        <>
        <div className={classes.backdrop} onClick={props.onClose}/>
        <div className={classes.modal}>
            <div className='card'>
                <div class="card-header bg-info">
                    <h5 class="card-title text-center">{props.title}</h5>
                </div>
                <div class="card-body">
                    {/* <Message /> */}
                    <p>arrrrrrrrr</p>
                </div>
            </div>
        </div>
        </>
    );
}