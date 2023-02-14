import SearchInput from './SearchInput/SearchInput';
import classes from './UsersHeader.module.scss'

function UsersHeader() {
  return (
    <div className={classes.wrapper}>
      <SearchInput />
    </div>
  );
};

export default UsersHeader;