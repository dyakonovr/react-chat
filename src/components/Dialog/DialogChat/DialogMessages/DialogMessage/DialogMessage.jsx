import classes from './DialogMessage.module.scss'

function DialogMessage({ myMsg }) {
  return (
    <div
      className={myMsg ? [classes.message, classes.message_right].join(' ') : [classes.message, classes.message_left].join(' ')}
    >
      <div className={classes.image}>
        <img src="https://reqres.in/img/faces/1-image.jpg" alt="sanya-petrov" />
      </div>
      <div className={classes.wrapper}>
        <strong className={classes.nickname}>sanya-petrov</strong>
        <p className={classes.content}>Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!</p>
      </div>
    </div>
  );
};

export default DialogMessage;