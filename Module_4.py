import vk_api
import traceback

try:
    while True:
        txt = input("Введите текст поста не более 140 символов: ")
        if len(txt) <= 140:
            vk_session = vk_api.VkApi('login', 'password')
            vk_session.auth()
            vk = vk_session.get_api()
            print(vk.wall.post(message = txt))
            input("Ваш пост успешно опубликован! =)\nНажмите Enter для выхода")
            break
        else:
            print("Вы превысили количество символов, вы ввели: ",len(txt), "символов, попробуйте ещё раз")
except Exception as e:
    print('Что-то пошло не так =(')
    input("Нажмите Enter для выхода")
              





