import io
import json
from  VaseHead_admin import bot_settings

bot_token = 'Токен бота'
wellcome = 'Приветствие'
littleasking = 'Просьба'
ask_gender = 'Спросить пол'
ask_age = 'Спросить возраст'
how_u_know_about_us = 'Как узнали о нас'
who_are_u = 'Род деятельности'
last_question = 'Последний вопрос'
what_hobby = 'Какое хобби'
thanx = 'Спасибо'
admin_contact = 'Контакт администратора'
admin_name = 'Имя администратора'
about_us = 'О нас'

settings = [] 
with open('VaseHead_admin/settings.txt') as json_file:  
     settings = json.load(json_file)
"""settings = []
settings.append({bot_token:'578603304:AAE2vc2E4CoAF6YLIAZTrnUt11nULmAbCew',
                            wellcome:'добро пожаловать в Vase Head! Меня зовут Ari, я твой виртуальный ассистент.', 
                            littleasking:'Маленькая просьба, заполни пожалуйста  мини - анкету, это займет 30секунд.!!! Данная анкета научит меня правильно общаться с вами, людьми !!!\nЗаранее благодарим Вас за вклад!',
                            ask_gender:'Вы - люди, имеете возможность прожить жизнь в разных телах. Завидую вам))\nУкажи свой пол:',
                            ask_age:'Тебе ...:',
                            how_u_know_about_us:'Кто тебя к нам привел?',
                            who_are_u:'Ты...',
                            last_question:'Cпасибо! И последний вопрос !!!',
                            what_hobby:'Чем ты увлекаешься?',
                            thanx:'Благодарю за уделенное мне время !!!',
                            admin_name : 'Яна', 
                            admin_contact : '+380730904851',
                            about_us : '<b>VASE HEAD</b> - это молодой бренд, создающий функциональные скульптуры для вашего интерьера.\nКаждый образ наших скульптур тщательно проработан командойVH, чтобы стать неотъемлемой частью пространства современных людей.Вы сами  решаете как их использовать.\nНаши скульпторы вручную прорабатывают каждое изделие, с любовью к своему делу.А мы, в свою очередь, делимся их мастерством с остальным миром.\nМы гордимся тем, что в любой точке нашей планеты, наши скульптуры вызывают яркие и положительные эмоции.И на этомVH не останавливается, мы ежемесячно пополняем наши коллекции новыми образами.\nА как ты используешь свою скульптуру <b>Vase Head</b>? Напиши об этом в Instagram или Facebook, используя хэштег#my_vasehead и мы обязательно расскажем о тебе всему миру и подарим скидку к твоему следующему заказу.'}) 
 """
def UpdateSettings():
    with open('VaseHead_admin/settings.txt') as json_file:  
         bot_settings.settings = json.load(json_file)


def GetSettingsValue(setting):
    return settings[0][setting]

def SetSettingValue(setting, newValue):
    settings[0][setting] = newValue
    SaveSettings()
    UpdateSettings()

def SaveSettings(new_settings):
    with open('VaseHead_admin/settings.txt', 'w') as outfile:
        if new_settings is not None:
            json.dump(new_settings, outfile)
        else:
            json.dump(settings, outfile)