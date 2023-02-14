import classes from './UserItem.module.scss'

function UserItem(props) {
  return (
    <li className={[classes.item].join(' ')}>
      <div className={classes.image}>
        <img src="https://reqres.in/img/faces/1-image.jpg" alt="sanya-petrov" />
      </div>
      <div className={classes.wrapper}>
        <strong className={classes.name}>{props.userName}</strong>
        <p className={classes.message}>{props.lastMsg}</p>
      </div>
    </li>
  );
};

export default UserItem;