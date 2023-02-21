import classes from './DialogMessages.module.scss'
import DialogMessage from './DialogMessage/DialogMessage';
import SimpleBar from 'simplebar-react';
import 'simplebar-react/dist/simplebar.min.css';
import { useEffect, useRef, useState } from 'react';

function DialogMessages() {
  const [messages, setMessages] = useState([
    { id: "1", userName: "Vasya", msg: "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "False" },
    { id: "2", userName: "Vasya", msg: "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "True" },
    { id: "3", userName: "Vasya", msg: "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "False" },
    { id: "4", userName: "Vasya", msg: "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "True" },
    { id: "5", userName: "Vasya", msg: "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "False" },
    { id: "6", userName: "Vasya", msg: "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "False" },
    { id: "7", userName: "Vasya", msg: "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "False" },
    { id: "8", userName: "Vasya", msg: "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "True" },

  ]);


  const scrollRef = useRef();
  useEffect(() => {
    const chatWidth = scrollRef.current.el.clientHeight;
    const chatBlock = scrollRef.current.el.querySelector('.simplebar-content-wrapper');
    chatBlock.scrollTo(0, chatWidth + 500);
  }, []);

  return (
    <SimpleBar id="scroll" className={classes.scroll} style={{ maxHeight: 610 - 51 - 50 }} forceVisible="y" ref={scrollRef}>
      <div className={classes.wrapper}>
        {messages.map(message =>
          <DialogMessage key={message.id} UserName={message.userName} msg={message.msg} myMsg={message.myMsg} />
        )}
      </div>
    </SimpleBar>
  );
};

export default DialogMessages;