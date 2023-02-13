import classes from './Dialog.module.css';
import DialogHeader from './DialogHeader/DialogHeader';
import DialogChat from './DialogChat/DialogChat';

function Dialog() {
  return (
    <div className={classes.wrapper}>
      <DialogHeader />
      <DialogChat />
    </div>
  );
};

export default Dialog;