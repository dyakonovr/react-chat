import UsersHeader from '../UI/UsersHeader/UsersHeader';
import classes from './Users.module.css'
import UsersList from './../UI/UsersList/UsersList';

function Users() {
  return (
    <div className={classes.wrapper}>
      <UsersHeader />
      <UsersList />
    </div>
  );
};

export default Users;