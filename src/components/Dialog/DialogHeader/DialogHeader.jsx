import classes from './DialogHeader.module.scss'

function DialogHeader() {
  return (
    <div className={classes.wrapper}>
      <div className={classes.image}>
        <img src="https://reqres.in/img/faces/1-image.jpg" alt="sanya-petrov" />
      </div>
      <strong className={classes.name}>sanya-petrov</strong>
    </div>
  );
};

export default DialogHeader;