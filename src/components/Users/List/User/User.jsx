import classes from './User.module.scss'
import { fetchChatData, chatIsChanged, resetPreloaderClasses } from '../../../../store/reducers/ActionCreators';
import { store } from '../../../../store/store';
import generateSocialIcon from '../../../../functions/generateSocialIcon';

function User({ user }) {
  // Функции
  function handleClick(target) {
    const itemActiveClass = classes.item_active;
    const activeItem = document.querySelector(`.${itemActiveClass}`);

    if (activeItem) activeItem.classList.remove(itemActiveClass);
    target.classList.toggle(itemActiveClass);


    // Создаю URL для json-файла
    const userID = target.getAttribute("data-id");
    const userSocial = target.getAttribute("data-from");
    const userUrl = `${userID}_${userSocial}`;

    store.dispatch(resetPreloaderClasses());
    store.dispatch(fetchChatData(userUrl));
    store.dispatch(chatIsChanged());
  }
  // Функции END

  return (
    <li className={[classes.item, `${classes.item}--${user.from}`].join(' ')} data-from={user.from}
      data-id={user.id} key={user.id} onClick={(e) => { handleClick(e.target) }}
    >
      <div className={classes.image}>
        <img src={`data:image/jpeg;base64,${user.avatar}`} alt={user.name} />
      </div>
      <div className={classes.wrapper}>
        <div className={classes.title}>
          <strong className={classes.name}>{user.name}</strong>
          <span className={classes.icon} style={{ 'backgroundImage': `url("${generateSocialIcon(user.from)}")` }}></span>
        </div>
        {/* <p className={classes.message}>{props.lastMsg}</p> */}
      </div>
    </li>
  );
};

export default User;