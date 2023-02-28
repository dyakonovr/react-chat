import os
import time
import asyncio
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

number = config['INST']['number']
password = config['INST']['password']


async def parse_massages(client):
    thread2 = client.direct_threads(1)[0]
    thread2.pk
    temp_msg = thread2.messages[0].id
    while True:
        print(1)
        thread = client.direct_threads(1)[0]
        thread.pk
        if(temp_msg!=thread.messages[0].id):
            print(thread.messages[0])
            temp_msg = thread.messages[0].id
        time.sleep(1)


async def main():
    client = Client()
    client.login(number, password)
    print("INST NOW PARSING ")
    await parse_massages(client)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        pass



