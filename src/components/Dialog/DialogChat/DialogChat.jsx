import classes from './DialogChat.module.scss'
import DialogInput from './DialogInput/DialogInput';
import DialogMessages from './DialogMessages/DialogMessages'

function DialogChat() {
  return (
    <div className={classes.wrapper}>
      <DialogMessages/>
      <DialogInput />
    </div>
  );
};

export default DialogChat;