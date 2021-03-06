# locochat

*Locochat* is a non-realtime made on both cli & ui platfrom, chat app implemented in python as my database course final project
### UI
![to-go_edit1](https://user-images.githubusercontent.com/78591315/176680600-71bfb0c6-2a60-49b1-85f9-29f9bc347c6f.gif)
### cli
![image](https://user-images.githubusercontent.com/78591315/176684957-1fca46c9-3d3c-4b38-a54c-22a4389ce6e1.png)



## Naming  <br/>
  'LocoChat' is a fancy combination of 'Locomotive' & 'chat'
  <br />
  also if you alter the characters you get 'Chocolat' =))
  
  
## About this project
  this is a non-realtime chat app meaning there is no concept of client & server implemented <br/>
  also it is implemented in a way that only one user can use app with no matter how many tabs of app you open, it will only display one users dashboard
  <br />
  <br />
  this project is built with python and used mysql as database <br/>
  also there exists a User Interface made with React.js and an api using flask <br /> <br />
  *note that the UI doesnt have the user limitation ability (yet)* <br/>
  code duplication in react components is in the 'OOOOOF' level and it could have better design patterns so feel free to contribute :)
  
 
## ERD
the ERD table is shown below
![image](https://user-images.githubusercontent.com/78591315/175594899-fbd4c432-3053-49f5-a1dd-8eabf3021e19.png)

## How to use
 - clone this repo
 - add the sql file in db folder to your mysql app
 - change the mysql conncetion entries in `connect.py`
 - if you want to use the cli app, enter cmd and use command 
 ```
 python main.py
 ```
 ### to use the ui app
 - run the flask server <br/>
  ```
  python api.py
  ```
 - enter the locochat front folder <br/>
 ```
 npm install
 ``` 
 ```
 npm start
 ```
** be sure to install Flask and Flask_cors packages **
 
