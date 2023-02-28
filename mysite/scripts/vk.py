import configparser
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import json
import asyncio
import requests
import base64
import os

config = configparser.ConfigParser()
config.read("scripts/config.ini")

key_user_id = 'id'
key_user_avatar = 'avatar'
key_username = 'name'

users = dict({'users': []})
old_user = dict({key_user_id: 1231, key_user_avatar: "asda",
                key_username: 'sadas', 'from': 'vk', 'last_message': 'sdf'})
new_user = dict({key_user_id: 1231, key_user_avatar: "asda",
                key_username: 'sadas', 'from': 'vk', "messages": []})
messageToGo = dict({'message': 'str', 'from': 'me', 'id': 'str',
                   'date': 'date', 'media_type': 'str', 'media_urls': []})

access_token = config['VK']['access_token']
session = vk_api.VkApi(token=access_token)

vk = session.get_api()
longpoll = VkLongPoll(session, preload_messages=True, mode=2)


def check_media(message_id):
    message = session.method('messages.getById', {"message_ids": message_id})
    # sticker
    try:
        messageToGo['media_urls'].clear()
        stik = message['items'][0]['attachments'][0]['sticker']['images'][-1]['url']
        messageToGo['media_type'] = 'Stiker'
        messageToGo['media_urls'].append(stik)
        old_user['last_message'] = 'Стикер'
        return
    except:
        pass
    # Multy
    messageToGo['media_urls'].clear()
    int_counter = [0, 0, 0]
    for i in range(0, len(message['items'][0]['attachments'])):
        tmp = message['items'][0]['attachments'][i]
        if (tmp['type'] == 'doc'):
            doc = message['items'][0]['attachments'][i]['doc']['url']
            messageToGo['media_urls'].append(doc)
            int_counter[0] += 1
        if (tmp['type'] == 'photo'):
            doc = message['items'][0]['attachments'][i]['photo']['sizes'][-1]['url']
            messageToGo['media_urls'].append(doc)
            int_counter[1] += 1
        if (tmp['type'] == 'video'):
            int_counter[2] += 1
            messageToGo['media_urls'].append('Неподдерживаемое вложение')
    if (int_counter[0] == 0 and int_counter[0] == 0 and int_counter[0] == 0):
        messageToGo['media_type'] = 'None'
        messageToGo['media_urls'] = ['None']
        old_user['last_message'] = messageToGo['message']
        return
    elif ((int_counter[0] != 0 and int_counter[1] != 0 and int_counter[2] == 0) or
          (int_counter[0] == 0 and int_counter[1] != 0 and int_counter[2] != 0) or
          (int_counter[0] != 0 and int_counter[1] == 0 and int_counter[2] != 0) or
          (int_counter[0] != 0 and int_counter[1] != 0 and int_counter[2] != 0)):
        messageToGo['media_type'] = 'Multy'
        old_user['last_message'] = 'Вложения'
        return
    elif (int_counter[0] != 0 and int_counter[1] == 0 and int_counter[2] == 0):
        messageToGo['media_type'] = 'Doc'
        old_user['last_message'] = 'Документ'
        return
    elif (int_counter[0] == 0 and int_counter[1] != 0 and int_counter[2] == 0):
        messageToGo['media_type'] = 'Photo'
        old_user['last_message'] = 'Фотография'
        return
    elif (int_counter[0] == 0 and int_counter[1] == 0 and int_counter[2] != 0):
        messageToGo['media_type'] = 'None'
        messageToGo['media_urls'] = [
            'Неподдерживаемое сообщение, обратитесь в техническую поддержку']
        old_user['last_message'] = messageToGo['message']
        return


def json_pars(*, json_array: json, result_list: list = None, key: str) -> list:
    if result_list is None:
        result_list = []
    if isinstance(json_array, list):
        for i in json_array:
            json_pars(json_array=i, result_list=result_list, key=key)
    if isinstance(json_array, dict):
        for i in json_array.keys():
            array = json_array[i]
            if i == key:
                result_list.append(array)
            else:
                json_pars(json_array=array, result_list=result_list, key=key)
    return result_list


def onOutgoingmessageRecieved(event: VkEventType.MESSAGE_NEW):
    try:
        f = open('jsons/users.json', 'x')
        f.close()
        with open('jsons/users.json', 'w') as json_out:
            json.dump(users, json_out)
    except:
        pass
    check_media(event.message_id)
    messageToGo['message'] = event.text
    messageToGo['id'] = event.message_id
    messageToGo['date'] = str(event.datetime)
    messageToGo['from'] = 'me'
    try:
        new_user[key_user_id] = event.peer_id
        old_user[key_user_id] = event.peer_id
        user2 = session.method(
            "users.get", {"user_ids": event.peer_id, "fields": ["photo_max_orig"]})
        user2 = user2[0]['photo_max_orig']
        photo = requests.get(user2)
        with open(str(event.message_id)+'.png', 'wb') as outfile:
            outfile.write(photo.content)
        with open(str(event.message_id)+'.png', "rb") as image_file:
            photostr = base64.b64encode(image_file.read())
        new_user[key_user_avatar] = photostr.decode('ascii')
        old_user[key_user_avatar] = photostr.decode('ascii')
        user2 = session.method("users.get", {"user_ids": event.peer_id})
        new_user[key_username] = user2[0]['first_name'] + \
            " " + user2[0]['last_name']
        old_user[key_username] = user2[0]['first_name'] + \
            " " + user2[0]['last_name']
        os.remove(str(event.message_id)+'.png')
        with open('jsons/' + str(event.peer_id)+'_vk.json', 'x') as outfile:
            json.dump(new_user, outfile)
        with open('jsons/users.json', 'r') as outjson:
            users2 = json.load(outjson)
            users2['users'].append(old_user)
        with open('jsons/users.json', 'w') as outjson:
            json.dump(users2, outjson)
    except:
        pass
    with open('jsons/users.json', 'r') as outjson:
        users2 = json.load(outjson)
    users_ids = json_pars(json_array=users2, key="id")
    index_user2 = users_ids.index(event.peer_id)
    users2['users'][index_user2]['last_message'] = old_user['last_message']
    with open('jsons/users.json', 'w') as outjson:
        json.dump(users2, outjson)
    with open('jsons/' + str(event.peer_id)+'_vk.json', 'r') as outfile:
        user = json.load(outfile)
    user['messages'].append(messageToGo)
    with open('jsons/' + str(event.peer_id)+'_vk.json', 'w') as outfile:
        json.dump(user, outfile)


def onIncomingMessageRecevied(event: VkEventType.MESSAGE_NEW):
    try:
        f = open('jsons/users.json', 'x')
        f.close()
        with open('jsons/users.json', 'w') as json_out:
            json.dump(users, json_out)
    except:
        pass
    message_id = event.message_id
    check_media(message_id)
    messageToGo['message'] = event.text
    messageToGo['id'] = event.message_id
    messageToGo['date'] = str(event.datetime)
    messageToGo['from'] = 'user'
    try:
        new_user[key_user_id] = event.user_id
        old_user[key_user_id] = event.user_id
        user2 = session.method(
            "users.get", {"user_ids": event.user_id, "fields": ["photo_max_orig"]})
        user2 = user2[0]['photo_max_orig']
        photo = requests.get(user2)
        with open(str(event.message_id)+'.png', 'wb') as outfile:
            outfile.write(photo.content)
        with open(str(event.message_id)+'.png', "rb") as image_file:
            photostr = base64.b64encode(image_file.read())
        new_user[key_user_avatar] = photostr.decode('ascii')
        old_user[key_user_avatar] = photostr.decode('ascii')
        user2 = session.method("users.get", {"user_ids": event.user_id})
        new_user[key_username] = user2[0]['first_name'] + \
            " " + user2[0]['last_name']
        old_user[key_username] = user2[0]['first_name'] + \
            " " + user2[0]['last_name']
        os.remove(str(event.message_id)+'.png')
        with open('jsons/' + str(event.user_id)+'_vk.json', 'x') as outfile:
            json.dump(new_user, outfile)
        with open('jsons/users.json', 'r') as outjson:
            users2 = json.load(outjson)
            users2['users'].append(old_user)
        with open('jsons/users.json', 'w') as outjson:
            json.dump(users2, outjson)
    except:
        pass
    with open('jsons/users.json', 'r') as outjson:
        users2 = json.load(outjson)
    users_ids = json_pars(json_array=users2, key="id")
    index_user2 = users_ids.index(event.user_id)
    users2['users'][index_user2]['last_message'] = old_user['last_message']
    with open('jsons/users.json', 'w') as outjson:
        json.dump(users2, outjson)
    with open('jsons/' + str(event.user_id)+'_vk.json', 'r') as outfile:
        user = json.load(outfile)
    user['messages'].append(messageToGo)
    with open('jsons/' + str(event.user_id)+'_vk.json', 'w') as outfile:
        json.dump(user, outfile)


async def parse_messages():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.from_me:
                onOutgoingmessageRecieved(event)
            if event.to_me and event.from_user:
                onIncomingMessageRecevied(event)


async def temp_to_send(user_id_to, message):
    vk.messages.send(user_id=user_id_to, message=message, random_id=0)


def send_message(user_id_to, message):
    asyncio.run(temp_to_send(user_id_to, message))


async def main():
    print("VK NOW PARSING\n")
    await parse_messages()


if __name__ == "__main__":
    asyncio.run(main())
