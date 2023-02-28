import Header from './Header/Header';
import List from './List/List';
import classes from './Users.module.scss';

function Users() {
  return (
    <div className={classes.wrapper}>
      <Header />
      <List />
    </div>
  );
};

export default Users;