import classes from './Dialog.module.scss';
import Header from './Header/Header';
import Chat from './Chat/Chat';
import { useSelector } from 'react-redux';
import generateLink from '../../functions/generateLink';

function Dialog() {
  const { data, isLoading, error } = useSelector(store => store.chatReducer);

  if (isLoading) {
    const { id, avatar, name, from, messages } = data;
    const userLink = generateLink(id, from);
    const userObject = { name, avatar, id, from, userLink };
    const chatObject = { messages, name, avatar, userLink};

    return (
      <div className={classes.wrapper}>
        <Header userObject={userObject} />
        <Chat chatObject={chatObject} />
      </div>
    );
  }
};

export default Dialog;