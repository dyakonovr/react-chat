import json
from datetime import datetime
from whatsapp_api_client_python import API
import requests
import base64
import os
import configparser

config = configparser.ConfigParser()
config.read("scripts/config.ini")


id = str(config['WA']['id'])
token = str(config['WA']['token'])

users = dict({'users': []})
old_user = dict({"user_id": 1231,'user_avatar': "asda", 'username' : 'sadas', 'from': 'tg'})
new_user = dict({"user_id": 1231, 'user_avatar': "asda",'username': 'sadas', 'from': 'wa', "messages": []})
messageToGo = dict({'message': 'str', 'from': 'me', 'id': 'str','date': 'date', 'photoflag': 'true', 'photo': '123'})

urlp = "https://api.green-api.com/waInstance" + id + "/getAvatar/" + token

logg = API.GreenApi(id, token)


headers = {
    'Content-Type': 'application/json'
}


async def main():
   logg.webhooks.startReceivingNotifications(onEvent)


def onEvent(typeWebhook, body):
   if typeWebhook == 'incomingMessageReceived':
      onIncomingMessageReceived(body)


def writejsUser(data, filename):
   with open(str(filename) + '_wa.json', "w") as f:
      json.dump(data, f)


def chek(filename, body):
   try:
      f = open('jsons/users.json', 'x')
      f.close()
      with open('jsons/users.json', 'w') as json_out:
         json.dump(users, json_out)
   except:
      pass
   new_user['user_id'] = body['senderData']['sender']
   new_user['username'] = body['senderData']['senderName']
   new_user['from'] = 'wa'
   new_user['messages'].append(messageToGo)
   old_user['user_id'] = body['senderData']['sender']
   old_user['username'] = body['senderData']['senderName']
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
         new_user['user_avatar'] = strPhoto.decode('ascii')
         old_user['user_avatar'] = strPhoto.decode('ascii')
         os.remove('img.jpeg')
      except:
         new_user['user_avatar'] = 'None'
         old_user['user_avatar'] = 'None'

      with open('jsons/' + str(filename) + '_wa.json', 'x') as jsonFile:
         json.dump(new_user, jsonFile)
      with open('jsons/users.json', 'r') as outjson:
         users2 = json.load(outjson)
         users2['users'].append(old_user)
      with open('jsons/users.json', 'w') as outjson:
         json.dump(users2, outjson)
      
   except:
        with open('jsons/' + str(filename) + '_wa.json', 'r') as jsonFile:
            user = json.load(jsonFile)
        user['messages'].append(messageToGo)
        with open('jsons/' + str(filename) + '_wa.json', 'w') as jsonFile:
            json.dump(user, jsonFile)



def send_text_message(text, user_id):
   logg.sending.sendMessage(user_id, text)
   body = logg.sending.greenApi
   body = body.journals.getChatHistory(user_id, '1')
   body = body.data[0]
   messageToGo['id'] = body['idMessage']
   messageToGo['date'] = str(datetime.fromtimestamp(body['timestamp']))
   messageToGo['message'] = text
   messageToGo['photoflag'] = 'false'
   messageToGo['photo'] = 'none'
   messageToGo['from'] = 'me'
   with open('jsons/' + str(user_id) + '_wa.json', 'r') as jsonFile:
      user = json.load(jsonFile)
   user['messages'].append(messageToGo)
   with open('jsons/' + str(user_id) + '_wa.json', 'w') as jsonFile:
      json.dump(user, jsonFile)




def onIncomingMessageReceived(body):
   eventDate = datetime.fromtimestamp(body['timestamp'])

   messageToGo['id'] = body['idMessage']
   messageToGo['date'] = str(eventDate)
   try:
      if (body['messageData']['typeMessage'] == 'imageMessage'):

         url = body['messageData']['fileMessageData']['downloadUrl']
         response = requests.get(url, stream=True)
         with open('img.jpeg', 'wb') as out_file:
            out_file.write(response.content)
         with open("img.jpeg", "rb") as img_file:
            strPhoto = base64.b64encode(img_file.read())
         del response
         messageToGo['photo'] = strPhoto.decode('ascii')
         os.remove('img.jpeg')

         messageToGo['message'] = body['messageData']['fileMessageData']['caption']
         messageToGo['photoflag'] = 'true'
      else:
         messageToGo['message'] = body['messageData']['textMessageData']['textMessage']
         messageToGo['photoflag'] = 'false'
         messageToGo['photo'] = 'none'
   except:
      messageToGo['message'] = "Неподдерживаемое сообщение, обратитесь в поддержку"
      messageToGo['photoflag'] = 'false'
      messageToGo['photo'] = 'None'
   messageToGo['from'] = 'user'

   chek(body['senderData']['sender'], body)


if __name__ == '__main__':
   send_text_message('text', '79626348420@c.us')
