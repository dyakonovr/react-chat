import classes from './Messages.module.scss'
import Message from './Message/Message';
import SimpleBar from 'simplebar-react';
import 'simplebar-react/dist/simplebar.min.css';
import { useEffect, useRef } from 'react';
import Preloader from '../../../Preloader/Preloader';
import { store } from '../../../../store/store';
import { useSelector } from 'react-redux';
import { preloaderIsDone } from './../../../../store/reducers/ActionCreators';

function Messages({ chatObject }) {
  const { messages, avatar, name, userLink } = chatObject;
  const { preloaderIsVisible } = useSelector(state => state.preloaderReducer);

  // Делаю скролл "снизу вверх"
  const scrollRef = useRef(null);
  useEffect(() => {
    // console.log(document?.querySelector("#preloader").classList);

    setTimeout(() => {
      const scrollBlock = document.querySelector("#scroll");
      const chatScroll = scrollBlock.querySelector('.simplebar-content-wrapper');
      const chatHeight = chatScroll.scrollHeight;
      chatScroll.scrollTo(0, chatHeight);
      // console.log(chatHeight);
    }, 100);

    setTimeout(() => {
      // document?.querySelector("#preloader").classList.add("done");

      store.dispatch(preloaderIsDone());
    }, 1000);

  }, [name]);
  // Делаю скролл "снизу вверх" END

  return (
    <>
      <Preloader />
      {messages.length !== 0
        ?
        <SimpleBar id="scroll" className={classes.scroll} style={{ maxHeight: 610 - 51 - 50 }} forceVisible="y" ref={scrollRef}>
          <div className={!preloaderIsVisible ? [classes.wrapper, classes.wrapper_visible].join(' ') : classes.wrapper}>
            {messages.map((message, idx) => {
              const messageObject = { ...message, avatar, name, userLink };
              return <Message messageObject={messageObject} key={idx} />
            })}
          </div>
        </SimpleBar>
        :
        false
      }
    </>
  );

};

export default Messages;