import classes from './LogInModal.module.css';
export default function SignUpModal(props){
return (
<>
<div className={classes.backdrop} onClick={props.onClose} />
<div className={`card text-center ${classes.modal}`}>
<div class="card-header">
   <h2>Log In</h2>
  </div>
  <div class={`card-body ${classes.content}` }>
    <label className="">Username</label>
    <input type="text" className="" placeholder="Username"></input>


    <label className="">Password</label>
    <input type="password" className="" placeholder="password"></input>

  </div>
  <div class="card-footer">
    <button className="btn btn-primary">Log In</button>
    </div>
</div>
</>
);

}