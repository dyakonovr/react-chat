import json
from datetime import datetime
from whatsapp_api_client_python import API
import requests
import base64
import os
import configparser
import asyncio
import pytz


config = configparser.ConfigParser()
config.read("scripts/config.ini")


id = str(config['WA']['id'])
token = str(config['WA']['token'])
none = config['None']['none']

key_user_id = 'id'
key_user_avatar = 'avatar'
key_username = 'name'

users = dict({'users': []})
old_user = dict({key_user_id: 1231, key_user_avatar: "asda", key_username : 'sadas', 'from': 'wa', 'last_message': 'sdf'})
new_user = dict({key_user_id: 1231, key_user_avatar: "asda", key_username : 'sadas', 'from': 'wa', "messages": []})
messageToGo = dict({'message': 'str', 'from': 'me', 'id': 'str','date': 'date', 'media_type': 'str', 'media_urls': []})

urlp = "https://api.green-api.com/waInstance" + id + "/getAvatar/" + token
urls = "https://api.green-api.com/waInstance" + id + "/readChat/" + token
urln = "https://api.green-api.com/waInstance" + id + "/getContactInfo/" + token
format = "%Y-%m-%d %H:%M:%S"

logg = API.GreenApi(id, token)


headers = {
    'Content-Type': 'application/json'
}


def check_media(body):
   try:
      if (body['messageData']['typeMessage'] == 'imageMessage'):
         messageToGo['message'] = body['messageData']['fileMessageData']['caption']
         messageToGo['media_type'] = 'Photo'
         messageToGo['media_urls'] = [(body['messageData']['fileMessageData']['downloadUrl'])]
      elif (body['messageData']['typeMessage'] == 'textMessage'):
         messageToGo['message'] = body['messageData']['textMessageData']['textMessage']
         messageToGo['media_type'] = 'None'
         messageToGo['media_urls'] = ['None']
      elif (body['messageData']['typeMessage'] == 'videoMessage'):
         messageToGo['message'] = body['messageData']['fileMessageData']['caption']
         messageToGo['media_type'] = 'Video'
         messageToGo['media_urls'] = [(body['messageData']['fileMessageData']['downloadUrl'])]
      elif (body['messageData']['typeMessage'] == 'documentMessage'):
         messageToGo['message'] = body['messageData']['fileMessageData']['caption']
         messageToGo['media_type'] = 'Doc'
         messageToGo['media_urls'] = [(body['messageData']['fileMessageData']['downloadUrl'])]
      elif (body['messageData']['typeMessage'] == 'audioMessage'):
         messageToGo['message'] = body['messageData']['fileMessageData']['caption']
         messageToGo['media_type'] = 'Audio'
         messageToGo['media_urls'] = [(body['messageData']['fileMessageData']['downloadUrl'])]
   except:
      messageToGo['message'] = "Неподдерживаемое сообщение, обратитесь в поддержку"
      messageToGo['media_type'] = 'None'
      messageToGo['media_urls'] = ['None']

def readMes(body):
   payload = "{\r\n\t\"chatId\": \"" + body['senderData']['sender'] + "\",\r\n\t\"idMessage\": \""+ body['idMessage'] +"\"\r\n}\r\n"
   response = requests.request("POST", urls, headers=headers, data = payload)


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


async def main():
   logg.webhooks.startReceivingNotifications(onEvent)
   


def onEvent(typeWebhook, body):
   if typeWebhook == 'incomingMessageReceived':
      onIncomingMessageReceived(body)
   if typeWebhook == 'outgoingMessageReceived' or typeWebhook == 'outgoingAPIMessageReceived':
      onOutgoingMessageReceived(body)



def chek_out(filename, body):
   try:
      f = open('jsons/users.json', 'x')
      f.close()
      with open('jsons/users.json', 'w') as json_out:
         json.dump(users, json_out)
   except:
      pass
   payload = "{\r\n    \"chatId\": \"" + \
         body['chatId'] + "\"\r\n}"
   response = requests.request("POST", urln, headers=headers, data = payload)
   name = json.loads(response.text.encode('utf-8'))['name']
   new_user[key_user_id] = body['chatId']
   new_user[key_username] = name
   new_user['from'] = 'wa'
   new_user['messages'].append(messageToGo)
   old_user[key_user_id] = body['chatId']
   old_user[key_username] = name
   old_user['from'] = 'wa'
   try:
      payload = "{\r\n    \"chatId\": \"" + \
         body['chatId'] + "\"\r\n}"
      responseS = requests.request(
         "POST", urlp, headers=headers, data=payload)
      responseS = json.loads(responseS.text)
      try:
         response = requests.get(responseS['urlAvatar'], stream=True)
         with open('img.jpeg', 'wb') as out_file:
            out_file.write(response.content)
         with open("img.jpeg", "rb") as img_file:
            strPhoto = base64.b64encode(img_file.read())
         del response
         new_user[key_user_avatar] = strPhoto.decode('ascii')
         old_user[key_user_avatar] = strPhoto.decode('ascii')
         os.remove('img.jpeg')
      except:
         new_user[key_user_avatar] = none
         old_user[key_user_avatar] = none
      if(messageToGo['media_type'] == 'None'):
         old_user['last_message'] = messageToGo['message']
      elif (messageToGo['media_type'] == 'Photo'):
         old_user['last_message'] = 'Фото'
      elif (messageToGo['media_type'] == 'Audio'):
         old_user['last_message'] = 'Аудио'
      elif (messageToGo['media_type'] == 'Video'):
         old_user['last_message'] = 'Видео'
      elif (messageToGo['media_type'] == 'Doc'):
         old_user['last_message'] = 'Документ'
      with open('jsons/' + str(filename) + '_wa.json', 'x') as jsonFile:
         json.dump(new_user, jsonFile)
      with open('jsons/users.json', 'r') as outjson:
         users2 = json.load(outjson)
         users2['users'].append(old_user)
      with open('jsons/users.json', 'w') as outjson:
         json.dump(users2, outjson)
   except:
      with open('jsons/users.json', 'r') as outjson:
         users2 = json.load(outjson)
      users_ids = json_pars(json_array=users2, key="id")
      index_user2 = users_ids.index(filename)
      if(messageToGo['media_type'] == 'None'):
         users2['users'][index_user2]['last_message'] = messageToGo['message']
      elif (messageToGo['media_type'] == 'Photo'):
         users2['users'][index_user2]['last_message'] = 'Фото'
      elif (messageToGo['media_type'] == 'Audio'):
         users2['users'][index_user2]['last_message'] = 'Аудио'   
      elif (messageToGo['media_type'] == 'Video'):
         users2['users'][index_user2]['last_message'] = 'Видео'
      elif (messageToGo['media_type'] == 'Doc'):
         users2['users'][index_user2]['last_message'] = 'Документ'
      with open('jsons/users.json', 'w') as outjson:
         json.dump(users2, outjson)
      with open('jsons/' + str(filename) + '_wa.json', 'r') as jsonFile:
         user = json.load(jsonFile)
      user['messages'].append(messageToGo)
      with open('jsons/' + str(filename) + '_wa.json', 'w') as jsonFile:
         json.dump(user, jsonFile)

def chek_in(filename, body):
   try:
      f = open('jsons/users.json', 'x')
      f.close()
      with open('jsons/users.json', 'w') as json_out:
         json.dump(users, json_out)
   except:
      pass
   new_user[key_user_id] = body['senderData']['sender']
   new_user[key_username] = body['senderData']['senderName']
   new_user['from'] = 'wa'
   new_user['messages'].append(messageToGo)
   old_user[key_user_id] = body['senderData']['sender']
   old_user[key_username] = body['senderData']['senderName']
   old_user['from'] = 'wa'
   try:
      payload = "{\r\n    \"chatId\": \"" + \
         body['senderData']['sender'] + "\"\r\n}"
      responseS = requests.request(
         "POST", urlp, headers=headers, data=payload)
      responseS = json.loads(responseS.text)
      try:
         response = requests.get(responseS['urlAvatar'], stream=True)
         with open('img.jpeg', 'wb') as out_file:
            out_file.write(response.content)
         with open("img.jpeg", "rb") as img_file:
            strPhoto = base64.b64encode(img_file.read())
         del response
         new_user[key_user_avatar] = strPhoto.decode('ascii')
         old_user[key_user_avatar] = strPhoto.decode('ascii')
         os.remove('img.jpeg')
      except:
         new_user[key_user_avatar] = none
         old_user[key_user_avatar] = none
      if(messageToGo['media_type'] == 'None'):
         old_user['last_message'] = messageToGo['message']
      elif (messageToGo['media_type'] == 'Photo'):
         old_user['last_message'] = 'Фото'
      elif (messageToGo['media_type'] == 'Audio'):
         old_user['last_message'] = 'Аудио'
      elif (messageToGo['media_type'] == 'Video'):
         old_user['last_message'] = 'Видео'
      elif (messageToGo['media_type'] == 'Doc'):
         old_user['last_message'] = 'Документ'
      with open('jsons/' + str(filename) + '_wa.json', 'x') as jsonFile:
         json.dump(new_user, jsonFile)
      with open('jsons/users.json', 'r') as outjson:
         users2 = json.load(outjson)
         users2['users'].append(old_user)
      with open('jsons/users.json', 'w') as outjson:
         json.dump(users2, outjson)
   except:
      with open('jsons/users.json', 'r') as outjson:
         users2 = json.load(outjson)
      users_ids = json_pars(json_array=users2, key="id")
      index_user2 = users_ids.index(filename)
      if(messageToGo['media_type'] == 'None'):
         users2['users'][index_user2]['last_message'] = messageToGo['message']
      elif (messageToGo['media_type'] == 'Photo'):
         users2['users'][index_user2]['last_message'] = 'Фото'
      elif (messageToGo['media_type'] == 'Audio'):
         users2['users'][index_user2]['last_message'] = 'Аудио'   
      elif (messageToGo['media_type'] == 'Video'):
         users2['users'][index_user2]['last_message'] = 'Видео'
      elif (messageToGo['media_type'] == 'Doc'):
         users2['users'][index_user2]['last_message'] = 'Документ'
      with open('jsons/users.json', 'w') as outjson:
         json.dump(users2, outjson)
      with open('jsons/' + str(filename) + '_wa.json', 'r') as jsonFile:
         user = json.load(jsonFile)
      user['messages'].append(messageToGo)
      with open('jsons/' + str(filename) + '_wa.json', 'w') as jsonFile:
         json.dump(user, jsonFile)
      



def send_text_message(text, user_id):
   logg.sending.sendMessage(user_id, text)


def onOutgoingMessageReceived(body):
   messageToGo['media_urls'].clear()
   eventDate = datetime.fromtimestamp(body['timestamp'])
   dt_str = str(eventDate)
   local_dt = datetime.strptime(dt_str, format)
   dt_utc = local_dt.astimezone(pytz.UTC)
   messageToGo['date'] = str(dt_utc)
   messageToGo['id'] = body['idMessage']
   check_media(body)
   messageToGo['from'] = 'me'
   try:
      filename = body['senderData']['chatId']
      body2 = body['senderData']
   except:
      filename = body['chatId']
      body2 = body

   chek_out(filename, body2)


def onIncomingMessageReceived(body):
   messageToGo['media_urls'].clear
   eventDate = datetime.fromtimestamp(body['timestamp'])
   dt_str = str(eventDate)
   local_dt = datetime.strptime(dt_str, format)
   dt_utc = local_dt.astimezone(pytz.UTC)
   messageToGo['date'] = str(dt_utc)
   messageToGo['id'] = body['idMessage']
   check_media(body)
   messageToGo['from'] = 'user'
   readMes(body)
   chek_in(body['senderData']['sender'], body)


if __name__ == '__main__':
   asyncio.run(main())
