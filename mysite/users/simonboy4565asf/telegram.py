from telethon import TelegramClient, events
import json
import configparser
import base64
import os
import asyncio

config = configparser.ConfigParser()
config.read("scripts/config.ini")

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

client = TelegramClient('telegram', api_id, api_hash)

users = dict({'users': []})
old_user = dict({"user_id": 1231, 'user_avatar': "asda",
                'username': 'sadas', 'from': 'tg'})
new_user = dict({"user_id": 1231, 'user_avatar': "asda",
                'username': 'sadas', 'from': 'tg', "messages": []})
messageToGo = dict({'from': 'user', 'message': 'str', 'id': 'str',
                   'date': 'date', 'photoflag': 'true', 'photo': 123})


async def temp_to_send(user_id: int, text):
    client = TelegramClient('telegramMessage', api_id, api_hash)
    await client.connect()
    await client.send_message(user_id, text)
    me = await client.get_me()
    me = me.id
    temp_msg = await client.get_messages(me, limit=1)
    temp_msg = temp_msg[0].to_dict()
    messageToGo['message'] = text
    messageToGo['id'] = temp_msg['id']
    messageToGo['date'] = str(temp_msg['date'])
    messageToGo['from'] = 'me'
    messageToGo['photoflag'] = "False"
    messageToGo['photo'] = 'None'
    with open('jsons/' + str(user_id)+'_tl.json', 'r') as outfile:
        user = json.load(outfile)
    user['messages'].append(messageToGo)
    with open('jsons/' + str(user_id)+'_tl.json', 'w') as outfile:
        json.dump(user, outfile)
    await client.disconnect()


def send_text_message(user_id: int, text):
    asyncio.run(temp_to_send(user_id, text))


async def send_media_message(phone_number, file):
    await client.send_file(phone_number, file)


async def main():
    print("TG NOW PARSING\n")

    @client.on(events.NewMessage)  # ждём новое сообщение
    async def parse_message(event):
        me = await client.get_me()
        me = me.id
        id = event.chat_id
        sender_id = ''
        try:
            sender_id = (await event.get_input_sender()).user_id
        except:
            pass
        if (sender_id != me and sender_id != ''):
            try:
                f = open('jsons/users.json', 'x')
                f.close()
                with open('jsons/users.json', 'w') as json_out:
                    json.dump(users, json_out)
            except:
                pass
            msg = (await client.get_messages(id, limit=1))
            await client.download_media(msg[0].media, str(msg[0].id)+'.png')
            try:
                with open(str(msg[0].id)+'.png', "rb") as image_file:
                    photostr = base64.b64encode(image_file.read())
                messageToGo['photo'] = str(photostr.decode('ascii'))
                messageToGo['photoflag'] = True
                os.remove(str(msg[0].id)+'.png')
            except:
                messageToGo['photoflag'] = False
                messageToGo['photo'] = 'None'

            temp_msg = msg[0].to_dict()
            messageToGo['message'] = temp_msg['message']
            messageToGo['id'] = temp_msg['id']
            messageToGo['date'] = str(temp_msg['date'])
            messageToGo['from'] = 'user'
            try:
                with open('jsons/' + str(sender_id)+'_tl.json', 'x') as outfile:
                    new_user['user_id'] = sender_id
                    old_user['user_id'] = sender_id
                    try:
                        new_user['username'] = str(((await client.get_entity(sender_id)).to_dict())['username'])
                        old_user['username'] = str(((await client.get_entity(sender_id)).to_dict())['username'])
                    except:
                        new_user['username'] = "Пользователь телеграм"
                        old_user['username'] = "Пользователь телеграм"
                    try:
                        await client.download_profile_photo(sender_id, str(msg[0].id)+'.png')
                        with open(str(msg[0].id)+'.png', "rb") as image_file:
                            photostr = base64.b64encode(image_file.read())
                        new_user['user_avatar'] = str(photostr.decode('ascii'))
                        old_user['user_avatar'] = str(photostr.decode('ascii'))
                        os.remove(str(msg[0].id)+'.png')
                    except:
                        new_user['user_avatar'] = "none"
                        old_user['user_avatar'] = "none"
                    json.dump(new_user, outfile)
                    with open('jsons/users.json', 'r') as outjson:
                        users2 = json.load(outjson)
                        users2['users'].append(old_user)
                    with open('jsons/users.json', 'w') as outjson:
                        json.dump(users2, outjson)
            except:
                pass
            with open('jsons/' + str(sender_id)+'_tl.json', 'r') as outfile:
                user = json.load(outfile)
                user['messages'].append(messageToGo)
            with open('jsons/' + str(sender_id)+'_tl.json', 'w') as outfile:
                json.dump(user, outfile)

    await client.start()
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
