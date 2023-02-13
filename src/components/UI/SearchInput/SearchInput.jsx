import classes from './SearchInput.module.css'

function SearchInput() {
  return (
    <input className={classes.input} placeholder="Поиск"/>
  );
};

export default SearchInput;