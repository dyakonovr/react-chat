import classes from './SearchInput.module.scss'

function SearchInput() {
  return (
    <input className={classes.input} placeholder="Поиск"/>
  );
};

export default SearchInput;