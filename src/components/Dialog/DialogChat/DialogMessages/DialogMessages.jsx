import classes from './DialogMessages.module.css'
import DialogMessage from './DialogMessage/DialogMessage';

function DialogMessages() {
  return (
    <div className={classes.wrapper}>
      <DialogMessage />
      <DialogMessage/>
      <DialogMessage/>
      <DialogMessage/>
      <DialogMessage/>
    </div>
  );
};

export default DialogMessages;