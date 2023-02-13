import classes from './Dialog.module.css';
import DialogHeader from './../UI/DialogHeader/DialogHeader';

function Dialog() {
  return (
    <div className={classes.wrapper}>
      <DialogHeader />
    </div>
  );
};

export default Dialog;