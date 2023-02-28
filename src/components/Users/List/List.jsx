import classes from './List.module.scss'
import User from './User/User';
import SimpleBar from 'simplebar-react';
import 'simplebar-react/dist/simplebar.min.css';
import { useSelector } from 'react-redux';

function List() {
  const { data, isLoading, error } = useSelector(state => state.usersReducer);

  if (isLoading) {
    const { users } = data;

    return (
      <SimpleBar style={{ maxHeight: 610 - 51 }} forceVisible="y">
        <ul className={classes.list}>
          {users.map(user => <User key={user.id} user={user} />)}
        </ul>
      </SimpleBar>
    );
  }
};

export default List;