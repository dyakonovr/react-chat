import classes from './UserItem.module.css'

function UserItem() {
  return (
    <li className={[classes.item].join(' ')}>
      <div className={classes.image}>
        <img src="https://reqres.in/img/faces/1-image.jpg" alt="sanya-petrov" />
      </div>
      <div className={classes.wrapper}>
        <strong className={classes.name}>sanya-petrov</strong>
        <p className={classes.message}>ava70347</p>
      </div>
    </li>
  );
};

export default UserItem;