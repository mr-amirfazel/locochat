import classes from "./welcome.module.css";
export default function Welcome(){
    return (
    <div className={`${classes.welcome}`}>
        <h1 className={`${classes.text}`}>
            
            Welcome  To LOCOCHAT

        </h1>
    </div>

    );
}