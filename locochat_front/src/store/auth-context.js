import React, { useState, useEffect } from 'react';

const AuthContext = React.createContext({
    username: '',
    isLoggedIn: false,
  onLogout: () => {},
  onLogin: (username) => {},
  onDeleteAccount: () => {}
});

export const AuthContextProvider = (props) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState('')

  useEffect(() => {
    const storedUserLoggedInInformation = localStorage.getItem('isLoggedIn');
    check_login();
    if (storedUserLoggedInInformation === '1') {
      setIsLoggedIn(true);
    }
  }, []);

  const check_login = () => {
    fetch("http://localhost:5000/logged_user")
    .then(response => {
       console.log(response)
       if (response.status === 200){
          response.json().then(data => {
            console.log(data.username)
             setIsLoggedIn(true);
             setUsername(data.username)
          })
       }
       else if (response.status === 400){
        response.json().then(data => {
            console.log(data.message)
          setIsLoggedIn(false);
        })
     }
      
    })

  }

  const logOutFetch = () => {
    fetch("http://localhost:5000/logout", {
     
        method: "POST",
        body: JSON.stringify({
          username: username,
        }),
         
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    .then(response => {
       console.log(response)
       if (response.status === 200){
          response.json().then(data => {
             console.log(data.message)
          })
       }
      
    })

  }
  const deleteAccountFetch = (tmp) => {
    fetch("http://localhost:5000/delete_account", {
     
        method: "POST",
        body: JSON.stringify({
          username: tmp,
        }),
         
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    .then(response => {
       console.log(response)
       if (response.status === 200){
          response.json().then(data => {
             console.log(data.message)
          })
       }
      
    })

  }

  const logoutHandler = () => {
    localStorage.removeItem('isLoggedIn');
    setIsLoggedIn(false);
    logOutFetch();
  };

  const loginHandler = (ID) => {
    localStorage.setItem('isLoggedIn', '1');
    setIsLoggedIn(true);
    setUsername(ID);
  };

  const deleteAccountHandler = () => {
    const temp_username = username;
    localStorage.removeItem('isLoggedIn');
    setIsLoggedIn(false);
    setUsername('');
    logOutFetch();
    deleteAccountFetch(temp_username);
  }

  return (
    <AuthContext.Provider
      value={{
        username: username,
        isLoggedIn: isLoggedIn,
        onLogout: logoutHandler,
        onLogin: loginHandler,
        onDeleteAccount: deleteAccountHandler,
      }}
    >
      {props.children}
    </AuthContext.Provider>
  );
};

export default AuthContext;