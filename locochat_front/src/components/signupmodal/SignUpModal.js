import classes from './SignUpModal.module.css';
export default function SignUpModal(props){
return (
<>
<div className={classes.backdrop} onClick={props.onClose} />
<div className={`card text-center ${classes.modal}`}>
<div class="card-header">
   <h2>Sign Up</h2>
  </div>
  <div class={`card-body ${classes.content}` }>
    <label className="">Username</label>
    <input type="text" className="" placeholder="Username"></input>

    <label className="">firstname</label>
    <input type="text" className="" placeholder="first name"></input>

    <label className="">last name</label>
    <input type="text" className="" placeholder="lastname"></input>

    <label className="">phone number</label>
    <input type="number" className="" placeholder="phone number"></input>

    <label className="">Email</label>
    <input type="email" className="" placeholder="Email"></input>

    <label className="">Password</label>
    <input type="password" className="" placeholder="password"></input>

    <p>what is your favorite color?</p>
    <label className="">Favorite color</label>
    <input type="text" className="" placeholder="Favorite color"></input>
  </div>
  <div class="card-footer">
    <button className="btn btn-primary">SignUp</button>
    </div>
</div>
</>
);

}