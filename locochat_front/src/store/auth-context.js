import React, { useState, useEffect } from 'react';

const AuthContext = React.createContext({
    username: '',
    isLoggedIn: false,
  onLogout: () => {},
  onLogin: (username) => {}
});

export const AuthContextProvider = (props) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState(null)

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
             alert(data.message)
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

  return (
    <AuthContext.Provider
      value={{
        isLoggedIn: isLoggedIn,
        onLogout: logoutHandler,
        onLogin: loginHandler,
      }}
    >
      {props.children}
    </AuthContext.Provider>
  );
};

export default AuthContext;