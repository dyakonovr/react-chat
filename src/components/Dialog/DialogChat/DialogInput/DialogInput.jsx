import { useState } from 'react';
import classes from './DialogInput.module.scss'

function DialogInput() {
  const [inputValue, setInputValue] = useState("")
  const inputChange = (event) =>
  {
    setInputValue(event.target.value)
  }
  return (
    <div className={classes.wrapper}>
      <input
      value={inputValue}
      onChange={inputChange}
      placeholder='Введите сообщение...'
      className={classes.input}
      />
      <button className={classes.btn}>
        <img className={classes.img} src="src/assets/send.svg" alt="" />
      </button>
    </div>
  );
};

export default DialogInput;