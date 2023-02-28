from scripts import vk
from scripts import wa
#from scripts import telegram
import threading
import asyncio


# def tg_main():
#     loop = asyncio.new_event_loop()
#     loop.run_until_complete(telegram.main())


def vk_main():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(vk.main())


def wa_main():
    loop = asyncio.new_event_loop()
    loop.run_until_complete(wa.main())


vk_thread = threading.Thread(target=vk_main)
#tg_thread = threading.Thread(target=tg_main)
wa_thread = threading.Thread(target=wa_main)


def main():
    vk_thread.start()
    wa_thread.start()
#    tg_thread.start()
