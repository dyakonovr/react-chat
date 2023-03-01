import { useState } from 'react';
import classes from './Input.module.scss';
import iconSend from "../../../../assets/icon-send.svg";

function Input() {
  const [inputValue, setInputValue] = useState("")
  const inputChange = (event) => setInputValue(event.target.value);
  return (
    <div className={classes.wrapper}>
      <input
        value={inputValue}
        onChange={inputChange}
        placeholder='Введите сообщение...'
        className={classes.input}
      />
      <button className={classes.btn}>
        <img className={classes.img} src={iconSend} alt="" />
      </button>
    </div>
  );
};

export default Input;