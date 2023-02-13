import classes from './UsersList.module.css'
import UserItem from './../UserItem/UserItem';

function UsersList() {
  return (
    <ul className={classes.list}>
      <UserItem />
      <UserItem />
      <UserItem />
      <UserItem />
      <UserItem />
    </ul>
  );
};

export default UsersList;