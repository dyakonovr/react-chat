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

users = dict({'users': []})
old_user = dict({"user_id": 1231,'user_avatar': "asda", 'username' : 'sadas', 'from': 'tg'})
new_user = dict({"user_id": 1231,'user_avatar': "asda", 'username' : 'sadas', 'from' : 'vk', "messages": []})
messageToGo = dict({'message' : 'str', 'from' : 'me', 'id' : 'str', 'date': 'date', 'photoflag' : 'true', 'photo': '123'})

access_token = config['VK']['access_token']
session = vk_api.VkApi(token=access_token)

vk = session.get_api()
longpoll = VkLongPoll(session, preload_messages=True, mode = 2)


async def parse_messages():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me and event.from_user:
                try:
                    f = open('jsons/users.json', 'x')
                    f.close()
                    with open('jsons/users.json', 'w') as json_out:
                        json.dump(users, json_out)
                except:
                    pass
                try:
                    message_id = event.message_id
                    message = session.method('messages.getById', {"message_ids": message_id})
                    photo = requests.get(message['items'][0]['attachments'][0]['photo']['sizes'][-1]['url'])
                    with open(str(event.message_id)+'.png', 'wb') as outfile:
                        outfile.write(photo.content)
                    messageToGo['photoflag'] = True
                    with open(str(event.message_id)+'.png', "rb") as image_file:
                        photostr = base64.b64encode(image_file.read())
                    messageToGo['photo'] = str(photostr.decode('ascii'))
                    os.remove(str(event.message_id)+'.png')
                except:
                    messageToGo['photoflag'] = False
                    messageToGo['photo'] = 'None'
                
                messageToGo['message'] = event.text
                messageToGo ['id'] = event.message_id
                messageToGo ['date'] = str(event.datetime)
                messageToGo ['from'] = 'user'
                try:                    
                    new_user['user_id'] = event.user_id
                    old_user['user_id'] = event.user_id
                    user2 = session.method("users.get", {"user_ids": event.user_id, "fields":["photo_max_orig"]})
                    user2 = user2[0]['photo_max_orig']
                    photo = requests.get(user2)
                    with open(str(event.message_id)+'.png', 'wb') as outfile:
                        outfile.write(photo.content)
                    with open(str(event.message_id)+'.png', "rb") as image_file:
                        photostr = base64.b64encode(image_file.read())
                    new_user['user_avatar'] = photostr.decode('ascii')
                    old_user['user_avatar'] = photostr.decode('ascii')
                    user2 = session.method("users.get", {"user_ids": event.user_id})
                    new_user['username'] = user2[0]['first_name']+ " " + user2[0]['last_name']
                    old_user['username'] = user2[0]['first_name']+ " " + user2[0]['last_name']
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
                with open('jsons/' + str(event.user_id)+'_vk.json', 'r') as outfile:
                    user = json.load(outfile)
                user['messages'].append(messageToGo)
                with open('jsons/' + str(event.user_id)+'_vk.json', 'w') as outfile:
                    json.dump(user, outfile)
                    


async def temp_to_send(user_id_to, message):
    vk.messages.send(user_id = user_id_to, message = message, random_id = 0)
    msg = session.method("messages.getHistory", {'user_id': user_id_to, 'count': 1})
    messageToGo['message'] = message
    messageToGo ['id'] = msg['items'][0]['id']
    messageToGo ['date'] = str(msg['items'][0]['date'])
    messageToGo ['from'] = 'me'
    messageToGo['photoflag'] = "False"
    messageToGo['photo'] = 'none'
    with open('jsons/' + str(user_id_to)+'_vk.json', 'r') as outfile:
        user = json.load(outfile)
    user['messages'].append(messageToGo)
    with open('jsons/' + str(user_id_to)+'_vk.json', 'w') as outfile:
        json.dump(user, outfile)

def send_message(user_id_to, message):
    asyncio.run(temp_to_send(user_id_to, message))



async def main():
    print("VK NOW PARSING\n")
    await parse_messages()



if __name__ == "__main__":
    asyncio.run(main())
    

