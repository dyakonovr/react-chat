import classes from './DialogInput.module.scss'

function DialogInput() {
  return (
    <div className={classes.wrapper}>
      <input 
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