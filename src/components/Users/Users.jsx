import UsersHeader from './UsersHeader/UsersHeader';
import UsersList from './UsersList/UsersList';
import classes from './Users.module.scss'

function Users() {
  return (
    <div className={classes.wrapper}>
      <UsersHeader />
      <UsersList />
    </div>
  );
};

export default Users;