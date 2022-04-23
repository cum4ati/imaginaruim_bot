import vk as vk
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import os
import sys

token = '46f982e5a44658d8a8bfa52a7230f339d23eebcb1c9132bd0f072fed0af619bf7aca30e3c79c7399fa620'
session = vk_api.VkApi(token=token)
api = session.get_api()
longpoll = VkLongPoll(session)

upload = vk_api.VkUpload(session)


def response(id, text):
    session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


used = []

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            user_id = event.user_id
            if message == 'старт' or message == 'начать':
                attchs = []
                for i in range(5):
                    files = os.listdir('imaginaruim_cards')
                    file = random.choice(files)
                    if file in used:
                        while file in used:
                            file = random.choice(files)

                    used.append(file)
                    attachment = f'imaginaruim_cards/{file}'
                    photo = upload.photo_messages(attachment)
                    owner_id = photo[0]['owner_id']
                    photo_id = photo[0]['id']
                    access_key = photo[0]['access_key']
                    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
                    attchs.append(attachment)
                api.messages.send(peer_id=user_id, random_id=0, attachment=','.join(attchs))

            else:
                response(user_id, 'На этом функционал закончен :(')
