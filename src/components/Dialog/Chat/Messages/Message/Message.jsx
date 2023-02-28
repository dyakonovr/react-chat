import classes from './Message.module.scss'
import generateDate from '../../../../../functions/generateDate';

function Message({ messageObject }) {
  console.log(messageObject);
  const { from, message, id, date, media_type, media_urls, name, avatar, userLink } = messageObject;

  // Функции
  function generateMessage(media_type, media_urls, message) {
    console.log(media_type, media_urls, message);
  }
  // Функции END

  return (
    <div
      className={from == "me" ? [classes.message, classes.message_right].join(' ') : [classes.message, classes.message_left].join(' ')}
      data-id={id}>
      <div className={classes.image}>
        <img src={`data:image/jpeg;base64,${avatar}`} alt="sanya-petrov" />
      </div>
      <div className={classes.wrapper}>
        <div className={classes.header}>
          <a target="_blank" href={userLink} className={classes.nickname}>{name}</a>
          <span className={classes.date}>{generateDate(date)}</span>
        </div>
        {generateMessage(media_type, media_urls, message)}
      </div>
    </div>
  );
};

export default Message;