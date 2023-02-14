import classes from './UsersList.module.scss'
import UserItem from './UserItem/UserItem';

import SimpleBar from 'simplebar-react';
import 'simplebar-react/dist/simplebar.min.css';
import { useState } from 'react';

function UsersList() {
const [users, setUsers] = useState([
    {id: "1", UserName : "Vasya", lastMsg : "123"},
    {id : "2", UserName : "Petya", lastMsg : "123"},
    {id : "3", UserName : "Kolya", lastMsg : "123"},
    {id : "4", UserName : "Vasya", lastMsg : "123"},
    {id : "5", UserName : "Petya", lastMsg : "123"},
    {id : "7", UserName : "Kolya", lastMsg : "123"},
    {id : "8", UserName : "Kolya", lastMsg : "123"},
    {id : "9", UserName : "Kolya", lastMsg : "123"},
    {id : "10", UserName : "Kolya", lastMsg : "123"},

]);
  return (
    <>
      <SimpleBar style={{ maxHeight: 650 - 51 }} forceVisible="y">
        <ul className={classes.list}>
          {users.map(user =>
            <UserItem key={user.id} userName={user.UserName} lastMsg={user.lastMsg}/>
            )}
        </ul>
      </SimpleBar>
    </>
  );
};

export default UsersList;