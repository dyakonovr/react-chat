import classes from './DialogMessages.module.scss'
import DialogMessage from './DialogMessage/DialogMessage';

import SimpleBar from 'simplebar-react';
import 'simplebar-react/dist/simplebar.min.css';

function DialogMessages() {
  return (
    <SimpleBar style={{ maxHeight: 650 - 51 - 50 }} forceVisible="y">
      <div className={classes.wrapper}>
        <DialogMessage myMsg={false} />
        <DialogMessage myMsg={true} />
        <DialogMessage myMsg={false} />
        <DialogMessage myMsg={true} />
        <DialogMessage myMsg={false} />
        <DialogMessage myMsg={true} />
        <DialogMessage myMsg={false} />
        <DialogMessage myMsg={true} />
        <DialogMessage myMsg={false} />
        <DialogMessage myMsg={true} />
        <DialogMessage myMsg={false} />
        <DialogMessage myMsg={true} />
        <DialogMessage myMsg={false} />
        <DialogMessage myMsg={true} />
      </div>
    </SimpleBar>
  );
};

export default DialogMessages;