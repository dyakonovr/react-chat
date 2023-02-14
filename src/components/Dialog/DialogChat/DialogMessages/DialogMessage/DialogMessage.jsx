import classes from './DialogMessage.module.scss'

function DialogMessage(props) {
  return (
    <div
      className={props.myMsg == "True"? [classes.message, classes.message_right].join(' ') : [classes.message, classes.message_left].join(' ')}
    >
      <div className={classes.image}>
        <img src="https://reqres.in/img/faces/1-image.jpg" alt="sanya-petrov" />
      </div>
      <div className={classes.wrapper}>
        <strong className={classes.nickname}>{props.UserName}</strong>
        <p className={classes.content}>{props.msg}</p>
      </div>
    </div>
  );
};

export default DialogMessage;