import classes from './UsersList.module.scss'
import UserItem from './UserItem/UserItem';

import SimpleBar from 'simplebar-react';
import 'simplebar-react/dist/simplebar.min.css';

function UsersList() {
  return (
    <>
      <SimpleBar style={{ maxHeight: 650 - 51 }} forceVisible="y">
        <ul className={classes.list}>
          <UserItem />
          <UserItem />
          <UserItem />
          <UserItem />
          <UserItem />
          <UserItem />
          <UserItem />
          <UserItem />
          <UserItem />
          <UserItem />
          <UserItem />
          <UserItem />
          <UserItem />
          <UserItem />
          <UserItem />
        </ul>
      </SimpleBar>
    </>
  );
};

export default UsersList;