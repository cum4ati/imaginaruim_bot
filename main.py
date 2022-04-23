import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

bot = vk_api.VkApi(token = '27218a84b2bfdd925be41222ba7387bd5c4953c6a9e05d485433bccbd65483b15d0c071595f8c11f2fb36')


def send_message(user_id, message):
    bot.method('messages.send', {
        "user_id": user_id,
        "message": message,
        "random_id": get_random_id()
    })


for event in VkLongPoll(bot).listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id
        send_message(user_id,text)