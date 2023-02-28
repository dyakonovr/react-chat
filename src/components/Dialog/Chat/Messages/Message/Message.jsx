import classes from './Message.module.scss'
import generateDate from '../../../../../functions/generateDate';
import iconDoc from "../../../../../assets/icon-doc.svg";

function Message({ messageObject }) {
  console.log(messageObject);
  const { from, message, id, date, media_type, media_urls, name, avatar, userLink } = messageObject;

  // Функции
  function generateMessage(media_type, media_urls, message) {
    let additionalBlock = '';

    console.log(media_type, media_urls, message);
    if (media_type == "None") additionalBlock = '';

    else if (media_type == "Photo") {
      additionalBlock = media_urls.map((url, i) => {
        return <div key={i} className={classes.userImg}><img src={url} alt="PHOTO" /></div>
      });
    }

    else if (media_type == "Stiker") {
      additionalBlock = <div className={classes.stiker}><img src={media_urls[0]} alt="STIKER" /></div>
    }

    else if (media_type == "Doc") {
      additionalBlock = media_urls.map((url, i) => {
        return <div key={i} href={url} className={classes.document_wrapper}>
          
          <div className={classes.document_icon} ><img src={iconDoc} alt="Icon"/></div>
          <strong className={classes.document_name}>Doc. name</strong>
        </div>
      });
    }

    return (
      <>
        <div>{media_type == "None" && message.length === 0 ? <span className={classes.empty}>Пустое сообщение...</span> : message}</div>
        {additionalBlock}
      </>
    )
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