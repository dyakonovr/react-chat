import classes from './DialogMessages.module.scss'
import DialogMessage from './DialogMessage/DialogMessage';

import SimpleBar from 'simplebar-react';
import 'simplebar-react/dist/simplebar.min.css';
import { useEffect } from 'react';
import { useRef } from 'react';
import { useState } from 'react';

function DialogMessages() {
  const [messages, setMessages] = useState([
    {id: "1", UserName : "Vasya", msg : "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "False"},
    {id: "2", UserName : "Vasya", msg : "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "True"},
    {id: "3", UserName : "Vasya", msg : "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "False"},
    {id: "4", UserName : "Vasya", msg : "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "True"},
    {id: "5", UserName : "Vasya", msg : "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "False"},
    {id: "6", UserName : "Vasya", msg : "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "False"},
    {id: "7", UserName : "Vasya", msg : "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "False"},
    {id: "8", UserName : "Vasya", msg : "Далеко-далеко, за словесными горами в стране гласных и согласных живут рыбные тексты. Коварный своих всеми lorem по всей проектах страна предложения эта рыбного грустный заманивший. Ему своего необходимыми рыбного осталось но, все коварный!", myMsg: "True"},

  ]);
  const ScrollRef = useRef();
  useEffect(() => {
    //ScrollRef.current.axis.y.scrollbar.el.classList.add("scrollBottom")
    //ScrollRef.current.axis.y.scrollbar.el.style = "height: 172px; transform: translate3d(0px, 0px, 0px); display: block;";
    // Пытался исправить скрол...

  }, []);
  
  return (
    <SimpleBar id="scroll" ref={ScrollRef} className={classes.scroll} style={{ maxHeight: 650 - 51 - 50}} forceVisible="y">
      <div  className={classes.wrapper}>
      {messages.map(message =>
            <DialogMessage key={message.id} UserName={message.UserName} msg={message.msg}myMsg={message.myMsg} />
            )}
      </div>
    </SimpleBar>
  );
};

export default DialogMessages;