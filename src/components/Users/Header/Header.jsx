import SearchInput from './SearchInput/SearchInput';
import classes from './Header.module.scss'

function Header() {
  return (
    <div className={classes.wrapper}>
      <SearchInput />
    </div>
  );
};

export default Header;