print('Loading...')

import vk_api
import requests
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload 

session = requests.Session()
vk_session = vk_api.VkApi(token='vk1.a.B4gUSY5DPzLNsdFZ1BYFpT8CRDYIKq0UG6filFyHdj_5qqsseuqgUTKiJorydIB-yaeI8eQ3zFEqDljejrU-RGMFPtLu-MpnZwpfJWRCuYHYmvcUPwO7c2xG5_qzUrGCmrrePO7XK5sXGo6C4zdFcuvl_RNvoK0GznOiLmuRpsbLDmOm2rqHT64J2u0H_aS6ia3cYVENUVbQBFTSB8gUbA')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

attachments = []
upload = VkUpload(vk_session)
image_url = 'https://i.pinimg.com/originals/c9/ea/65/c9ea654eb3a7398b1f702c758c1c4206.jpg'
image = session.get(image_url, stream=True)
photo = upload.photo_messages(photos=image.raw)[0]
attachments.append(
    'photo{}_{}'.format(photo['owner_id'], photo['id'])
)

print('Loading complete!')

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text: 
        if event.from_user:
            print('Message received:', event.text)
            if event.message == 'здохни':
                print('Turning off...')
                break
            else:
                vk.messages.send(
                    user_id=event.user_id,
                    message='...',
                    #attachment=','.join(attachments),
                    random_id=random.randint(-2147483648, 2147483648)
        )
    #     elif event.from_chat:
    #         vk.messages.send(
    #             chat_id=event.chat_id,
    #             message='',
    #             random_id=random.randint(-2147483648, 2147483648)
    # )