import SearchBar from "../UI/searchbar/SearchBar";
import classes from './Search.module.css';
import React,{useState} from "react";
import SearchList from './SearchList';


export default function Search() {
    const [search, setSearch] = useState("");
    const [result, setResult] = useState([]);
    const [error, setError] = useState("");

   

    const inputHandler = (e) => {
        setSearch(e.target.value);
      };

      const fetch_search = () =>{
         fetch("http://localhost:5000/search", {
     
            method: "POST",
            body: JSON.stringify({
              username: search
            }),
             
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then(response => {
           console.log(response)
           if (response.status === 200){
              response.json().then(data => {
                console.log(data.users)
                 setResult(data.users)
                 setError('')
              })
           }
           else if (response.status === 400){
              response.json().then(data => {
                setError(data.message)
              })
           }
          
        })
        
      };

      return (
        <div className={`${classes.container}`}>
            <div className="inner">
            <div className={`${classes.search_bar}`} >
                <SearchBar onChange={inputHandler} />
                <button className={`btn btn-primary w-100`} onClick={fetch_search}>Search</button>
            </div>
            <div className={`${classes.results}`}>
            {error.trim() ==='' && <SearchList users={result}/>}
            {error.trim() !=='' && <p className="text-danger text-center">{error}</p>}
            </div>
            </div>
        </div>
      );

}