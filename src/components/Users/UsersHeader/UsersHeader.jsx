import SearchInput from '../../UI/SearchInput/SearchInput';
import classes from './UsersHeader.module.css'

function UsersHeader() {
  return (
    <div className={classes.wrapper}>
      <SearchInput />
    </div>
  );
};

export default UsersHeader;