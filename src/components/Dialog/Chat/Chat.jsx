import classes from './Chat.module.scss'
import Input from './Input/Input';
import Messages from './Messages/Messages'

function Chat({ chatObject }) {
  return (
    <div className={classes.wrapper}>
      <Messages chatObject={chatObject} />
      <Input />
    </div>
  );
};

export default Chat;