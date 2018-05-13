from telegram.parsemode import ParseMode
import json
from telegram.keyboardbutton import KeyboardButton
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from VaseHead_admin import states
from VaseHead_admin import bot_settings
from VaseHead_admin.bot_settings import GetSettingsValue
from app.models import Client, MassSendingReport
from django.db.models import Q
from django.conf import settings

bot_instance = "BOT"

def GiveBot(bot):
    global bot_instance
    bot_instance = bot.bot

def SayHello(bot, update, self):
            bot.send_photo(chat_id=update.message.chat_id, photo=open('VaseHead_admin/header.jpg', 'rb'), caption =  update.message.from_user.first_name + ', ' + GetSettingsValue(bot_settings.wellcome))
            self.SetMyState(states.Share_contact);
            contact_keyboard = KeyboardButton(text="Поделиться контактом", request_contact=True, )
            custom_keyboard = [[contact_keyboard ]]
            reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard = True)
            bot.send_message(chat_id=update.message.chat_id, 
                             text = GetSettingsValue(bot_settings.littleasking),
                             parse_mode=ParseMode.HTML,
                             reply_markup=reply_markup);
def AskContact(bot, update, self):
            contact_keyboard = KeyboardButton(text="Поделиться контактом", request_contact=True, )
            custom_keyboard = [[contact_keyboard ]]
            reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard = True)
            bot.send_message(chat_id=update.message.chat_id, 
                             parse_mode=ParseMode.HTML,
                             reply_markup=reply_markup);
def AskAboutGender(bot, update, self):
            bot.send_message(chat_id=update.message.chat_id, 
                             text = "👍",
                             parse_mode=ParseMode.HTML,
                             reply_markup=ReplyKeyboardRemove());
            button_list = [
                           [ InlineKeyboardButton("М", callback_data="Gender-М"),
                            InlineKeyboardButton("Ж", callback_data="Gender-Ж")]
                          ]
            reply_markup = InlineKeyboardMarkup(button_list)
            bot.send_message(chat_id=update.message.chat_id, 
                             text = GetSettingsValue(bot_settings.ask_gender),
                             parse_mode=ParseMode.HTML,
                             reply_markup=reply_markup)
def AskAboutAge(bot, update, self):
            button_list = [[
                            InlineKeyboardButton("14–24  Эх..Лучшее время", callback_data="Age-14–24"),
                          ],[
                            InlineKeyboardButton("25–34  Постоянно в делах", callback_data="Age-25–34"),
                          ],[
                            InlineKeyboardButton("35–100 Мудрость пришла", callback_data="Age-35–100"),
                          ],
                          ]
            reply_markup = InlineKeyboardMarkup(button_list)
            bot.send_message(chat_id=update.callback_query.message.chat_id, 
                             text = GetSettingsValue(bot_settings.ask_age),
                             parse_mode=ParseMode.HTML,
                             reply_markup=reply_markup);
def AskAboutInvitation(bot, update, self):
            button_list = [[
                            InlineKeyboardButton("Instagram", callback_data="WhoInvited-Instagram"),
                            InlineKeyboardButton("Facebook", callback_data="WhoInvited-Facebook"),
                            InlineKeyboardButton("Google", callback_data="WhoInvited-Google")
                          ],[
                            InlineKeyboardButton("Друзья", callback_data = "WhoInvited-Друзья"),
                            InlineKeyboardButton("Выставка", callback_data="WhoInvited-Выставка")
                          ]
                          ]
            reply_markup = InlineKeyboardMarkup(button_list)
            bot.send_message(chat_id=update.callback_query.message.chat_id, 
                             text = GetSettingsValue(bot_settings.how_u_know_about_us),
                             parse_mode=ParseMode.HTML,
                             reply_markup=reply_markup);
def AskWhoAreU(bot, update, self):
            button_list = [[
                            InlineKeyboardButton("Студент(ка)", callback_data="WhoAreU-Студент(ка)"),
                          ],[
                            InlineKeyboardButton("Работаешь в компании", callback_data="WhoAreU-Работаешь в компании"),
                          ],[
                            InlineKeyboardButton("Предприниматель", callback_data="WhoAreU-Предприниматель"),
                          ],
                          ]
            reply_markup = InlineKeyboardMarkup(button_list)
            bot.send_message(chat_id=update.callback_query.message.chat_id, 
                             text = GetSettingsValue(bot_settings.who_are_u),
                             parse_mode=ParseMode.HTML,
                             reply_markup=reply_markup);
def LastQuestion(bot, update, self):
            bot.send_message(chat_id=update.callback_query.message.chat_id, 
                             text = GetSettingsValue(bot_settings.last_question),
                             parse_mode=ParseMode.HTML);
def AskAboutHobby(bot, update, self):
            button_list = [[
                            InlineKeyboardButton("Искусство", callback_data="YourHobby-Искусство"),
                            InlineKeyboardButton("Бизнес", callback_data="YourHobby-Бизнес"),
                            InlineKeyboardButton("Спорт", callback_data="YourHobby-Спорт")
                          ],[
                            InlineKeyboardButton("Путешествия", callback_data = "YourHobby-Путешествия"),
                            InlineKeyboardButton("Книги", callback_data = "YourHobby-Книги"),
                            InlineKeyboardButton("IT", callback_data="YourHobby-IT")
                          ]
                          ]
            reply_markup = InlineKeyboardMarkup(button_list)
            bot.send_message(chat_id=update.callback_query.message.chat_id, 
                             text = GetSettingsValue(bot_settings.what_hobby),
                             parse_mode=ParseMode.HTML,
                             reply_markup=reply_markup);
def SayThankU(bot, update, self):
            bot.send_message(chat_id=update.callback_query.message.chat_id, 
                             text = GetSettingsValue(bot_settings.thanx),
                             parse_mode=ParseMode.HTML);
def ShowMainMenu(bot, update, self):
            button_list = [[
                            KeyboardButton("🏪 Магазин"),
                            KeyboardButton("🛒 Корзина"),
                            KeyboardButton("📖 О нас")
                          ],[
                            KeyboardButton("🤝 Сотрудничество"),
                            KeyboardButton("🔍 Как нас найти")
                          ]
                          ]
            reply_markup = ReplyKeyboardMarkup(button_list, resize_keyboard = True)
            chat_id = ''
            try:
                chat_id = update.callback_query.message.chat_id
            except:
                chat_id = update.message.chat_id
            bot.send_message(chat_id=chat_id, 
                             text = '<b>Выбирай:</b>\nМагазин - тут наши скульптуры\nКорзина - активна после покупки\nО нас - тут все понятно\nАкции / События - держим вас в курсе\nПартнерство - если хочешь продавать нас Как нас найти ? -без комментариев',
                             parse_mode=ParseMode.HTML,
                             reply_markup=reply_markup);
def SendYanasContact(bot, update, self):
    bot.send_contact(chat_id=update.callback_query.message.chat_id, 
                     phone_number=GetSettingsValue(bot_settings.admin_contact), 
                     first_name=GetSettingsValue(bot_settings.admin_name));
def ShowCoworking(bot, update):
            bot.send_photo(chat_id=update.message.chat_id, photo=open('VaseHead_admin/header2.jpg', 'rb'), caption =  'Хочешь стать партнером Vase Head?\nРост продаж за квартал 2018, на 38% больше по сравнению с 2017.')
            button_list = [
                           [ InlineKeyboardButton("Подробнее...", callback_data="PartnershipDetails")],
                            [InlineKeyboardButton("Назад", callback_data="MainMenu")],
                          ]
            reply_markup = InlineKeyboardMarkup(button_list)
            bot.send_message(chat_id=update.message.chat_id, 
                             text = 'На данный момент мы продаемся в странах СНГ и Европы.\nКаждый месяц у нас новый релиз скульптуры, значит к концу 2018 их будет аж 15 :)\nЧтобы подать заявку на партнерство, кликай и пройди регистрацию.',
                             parse_mode=ParseMode.HTML,
                             reply_markup=reply_markup);
def AskHowUWillRealiseProducts(bot, update, self):
            self.newcoworking.user_id = update.callback_query.message.chat_id
            self.newcoworking.user_name = '{} {}'.format(update.callback_query.message.chat.first_name, update.callback_query.message.chat.last_name)
            print(self.newcoworking.user_id)
            button_list = [
                           [ InlineKeyboardButton("Online...", callback_data="Partner-Online")],
                            [InlineKeyboardButton("Offline", callback_data="Partner-Offline")],
                          ]
            reply_markup = InlineKeyboardMarkup(button_list, resize_keyboard = True) 
            bot.send_message(chat_id=update.callback_query.message.chat_id, 
                             text = 'Как ты планируешь реализовывать продукцию Vase Head....?',
                             parse_mode=ParseMode.HTML,
                             reply_markup=reply_markup);
def AskCountry(bot, update, self):
            bot.send_message(chat_id=update.callback_query.message.chat_id, 
                             text = 'Укажи страну, в которой планируются продажи ....? \n(Пример: Страна, Город)',
                             parse_mode=ParseMode.HTML);
            self.SetMyState(states.AskCountry)
def SayErrorInput(bot, update, self):
            bot.send_message(chat_id=update.message.chat_id, 
                             text = 'Ошибка, попробуйте ещё...',
                             parse_mode=ParseMode.HTML);
def AskSalesCount(bot, update, self):
        bot.send_message(chat_id=update.message.chat_id, text = 'Ожидаемый кол-во/ объем продаж в месяц ....? \n(Пример: 10 - 15)',
                             parse_mode=ParseMode.HTML);
def AskName(bot, update, self):
    bot.send_message(chat_id=update.message.chat_id, 
                             text = 'Укажи свое имя и фамилию....?\n(Пример: Иван Торобосов)',
                             parse_mode=ParseMode.HTML)
    self.SetMyState(states.AskName);
def AskAboutRealeseSquare(bot, update, self):
    button_list = [[ InlineKeyboardButton("Да", callback_data="RealiseSquare-Yes"),
                            InlineKeyboardButton("Нет", callback_data="RealiseSquare-No")]]
    reply_markup = InlineKeyboardMarkup(button_list)
    bot.send_message(chat_id=update.message.chat_id, 
                             text = 'Есть ли у тебя действующий магазин/ площадка....?',
                             parse_mode=ParseMode.HTML,
                             reply_markup = reply_markup)
    self.SetMyState(states.AskRealeseSquare)
def AskLink(bot, update, self):
    bot.send_message(chat_id=update.callback_query.message.chat_id, 
                             text = 'Укажи ссылку...?\n(Пример: <b>https://www.vase-head.com</b>)',
                             parse_mode=ParseMode.HTML);
    self.SetMyState(states.AskUrl);
def AskSocialNetwork(bot, update, self):
    bot.send_message(chat_id=update.message.chat_id, 
                             text = 'Если есть еще соц. сети и др. введи повторно....',
                             parse_mode=ParseMode.HTML);
    self.SetMyState(states.AskSocialNetwork);
def AskPhoneNumber(bot, update, self):
    bot.send_message(chat_id=update.message.chat_id, 
                             text = 'Укажи свой контактный телефон...?\n(Пример: +380730904800)',
                             parse_mode=ParseMode.HTML);
    self.SetMyState(states.AskPnoneNumber);
def AskPhoneNumber(bot, update, self):
    bot.send_message(chat_id=update.message.chat_id, 
                             text = 'Укажи свой контактный телефон...?\n(Пример: +380730904800)',
                             parse_mode=ParseMode.HTML);
    self.SetMyState(states.AskPnoneNumber);
def AskEmail(bot, update, self):
    bot.send_message(chat_id=update.message.chat_id, 
                             text = 'Укажи свою  почту...?\n(Пример: info@info.com)',
                             parse_mode=ParseMode.HTML);
    self.SetMyState(states.AskEmail);
def SayHighFive(bot, update, self):
    bot.send_message(chat_id=update.message.chat_id, 
                             text = 'За уделенное время - (дай пять)\nСкоро кто - то выйдет на связь с тобой !!!',
                             parse_mode=ParseMode.HTML);
def SayHowToFindUs(bot, update, self):
    buttons = [[InlineKeyboardButton(text = '🌐 Сайт', url ="https://www.vase-head.com/"),
                InlineKeyboardButton("📱 Телефон", callback_data = "Phone"),
                InlineKeyboardButton("📧 Эл.почта", url = "info@vase-head.com")]]
    bot.send_message(chat_id=update.message.chat_id, 
                             text = 'Вы можете :\n📰 Познакомиться с нашим сайтом.\n📞 Связаться с менеджером.\n📬  Написать нам на почту.',
                             parse_mode=ParseMode.HTML,
                             reply_markup = InlineKeyboardMarkup(buttons));
    SayShowRoomList(bot, update, self);
def SayShowRoomList(bot, update, self):
    buttons = [[InlineKeyboardButton('Киев', callback_data ='Сity-Kiev'),
                InlineKeyboardButton("Одеса", callback_data = 'Сity-Odesa'),
                InlineKeyboardButton("Харьков", callback_data = 'Сity-Kharkov')],
               [InlineKeyboardButton('Запорожье', callback_data ='Сity-Zaporozhie'),
                InlineKeyboardButton('Черновцы', callback_data = 'Сity-Chernovtsi')]]
    bot.send_message(chat_id=update.message.chat_id, 
                             text = 'Также, в шоу-румах по всей Украине',
                             parse_mode=ParseMode.HTML,
                             reply_markup = InlineKeyboardMarkup(buttons));
def SayShowRoomsAddress(bot, update, self):
    city = update.callback_query.data.split('-')[1]
    address = ''
    if city == 'Kiev':
        address = 'HIS, ул. Ивана Федорова 1\nUa Made, ТРЦ Lavina Mall\nAnnies Corner, ул.О.Гончара 14\nNew Flora, ул.Г.Алмазова 4\nSanctum, ул.Дорогожицкая 1\nARKA Flowers, ул.Регенераторная 4 / 5\nFlorissima, ТЦ Атмосфера\nWhitebeard Blackbird, ул.Возвдвиженская 40\nVeg Couture, ул  Хорева 21'
    if city == 'Odesa':
        address = 'Marry Berry, ул. Польская 12\nUtopia 8, ул. Жуковского 32\nHolovoy , ул. Троицкая 45'
    if city == 'Kharkov':
        address = 'Utopia 8, ул. Пушкинская 72'
    if city == 'Zaporozhie':
        address = 'Stl.Katin, пр. Соборный 216'
    if city == 'Chernovtsi':
        address = 'Lol Showroom, ул. Заньковецкой 3'

    bot.send_message(chat_id=update.callback_query.message.chat_id, 
                             text = address,
                             parse_mode=ParseMode.HTML);
def SayAboutUs (bot, update, self):
    buttons = [[
                InlineKeyboardButton("К скульптурам", callback_data = 'Magazine'),
                InlineKeyboardButton("Назад", callback_data = 'MainMenu')
                ]]
    bot.send_message(chat_id=update.message.chat_id, 
                             text = GetSettingsValue(bot_settings.about_us),
                             parse_mode=ParseMode.HTML,
                             reply_markup = InlineKeyboardMarkup(buttons));
def ShowMagazine (bot, update, self):
    items = self.GetItems() 
    color_text = '{} ({}/{})'.format(items[self.item_counter].images[self.item_color].split('.')[0].replace('photos/',''), self.item_color + 1, len(items[self.item_counter].images))
    buttons = [
                 [InlineKeyboardButton("⬅️", callback_data = 'previous'), InlineKeyboardButton(str(self.item_counter + 1) + " из " + str(len(items)), callback_data = 'count'), InlineKeyboardButton("➡️", callback_data = 'next')],
                 [InlineKeyboardButton("⬅️", callback_data = 'previous_color'), InlineKeyboardButton(color_text, callback_data = 'count'), InlineKeyboardButton("➡️", callback_data = 'next_color')],
                 [InlineKeyboardButton(items[self.item_counter].description, callback_data = 'description')],
                 [InlineKeyboardButton('В корзину({} UAH)'.format(items[self.item_counter].price), callback_data = 'buy-{}-{}'.format(items[self.item_counter].id, color_text.split(' ')[0]))]
               ]
    self.magazine = bot.send_photo(chat_id=update.message.chat_id, photo=open(settings.BASE_DIR + '/media/' + str(items[self.item_counter].images[self.item_color]), 'rb'), caption =  items[self.item_counter].name, reply_markup = InlineKeyboardMarkup(buttons))
def SelectNextGood(bot, update, self):
    items = self.GetItems() 
    bot.delete_message(chat_id = self.magazine.chat_id, message_id = self.magazine.message_id)
    self.item_color = 0
    self.item_counter=self.item_counter+1
    if self.item_counter > len(items)-1:
        self.item_counter = 0
    ShowMagazine(bot, update.callback_query, self)
def SelectPreviousGood(bot, update, self):
    items = self.GetItems() 
    bot.delete_message(chat_id = self.magazine.chat_id, message_id = self.magazine.message_id)
    self.item_color = 0
    self.item_counter=self.item_counter-1
    if self.item_counter < 0:
        self.item_counter = (len(items)-1)
    ShowMagazine(bot, update.callback_query, self)
def SelectPreviousColor(bot, update, self):
    items = self.GetItems() 
    bot.delete_message(chat_id = self.magazine.chat_id, message_id = self.magazine.message_id)
    self.item_color=self.item_color-1
    if self.item_color < 0:
        self.item_color = (len(items[self.item_counter].images)-1)
    ShowMagazine(bot, update.callback_query, self)
def SelectNextColor(bot, update, self):
    items = self.GetItems() 
    bot.delete_message(chat_id = self.magazine.chat_id, message_id = self.magazine.message_id)
    self.item_color=self.item_color+1
    if self.item_color > (len(items[self.item_counter].images)-1):
        self.item_color = 0
    ShowMagazine(bot, update.callback_query, self)
def MakeMassSending(data):
    gender_filter =data.getlist('gender_select')
    age_filter = data.getlist('age_select')
    invite_filter = data.getlist('invite_select')
    class_filter = data.getlist('class_select')
    hobby_filter = data.getlist('hobby_select')
    clients = Client.objects.all()
    filters = 'Для всех'
    if gender_filter:
        clients = clients.filter(gender__in = gender_filter)
        filters = str(gender_filter) + ',\n'
    if age_filter:
        query = Q()
        for letter in age_filter:
            query = query | Q(age__startswith=letter)
        clients = clients.filter(query)
        filters = filters + str(age_filter) + ',\n'
    if invite_filter:
        clients = clients.filter(who_invired__in = invite_filter)
        filters = filters + str(invite_filter) + ',\n'
    if class_filter:
        clients = clients.filter(profession__in = class_filter)
        filters = filters + str(class_filter) + ',\n'
    if hobby_filter:
        clients = clients.filter(hobby__in = hobby_filter)
        filters = filters + str(hobby_filter)
    bot = bot_instance
    for c in clients:
        bot.send_message(chat_id = str(c.clientid), 
                             text = data.get('message_text'),
                             parse_mode=ParseMode.HTML);
    MassSendingReport(text = data.get('message_text'), description = data.get('description_input'),filter = filters.replace('[','').replace(']',''), count = len(clients)).save()
def ShowCart(bot, update, self):
    try:
        if self.cart_message:
            try:
                bot.delete_message(chat_id = self.cart_message.chat_id, message_id = self.cart_message.message_id)
            except:
                doNothing = 0;
        if not self.cart:
            bot.send_message(chat_id=update.message.chat_id, 
                                 text = 'Корзина пуста.',
                                 parse_mode=ParseMode.HTML);
        else:
            buttons = []
            total = 0
            for g in self.cart:
                buttons.append([InlineKeyboardButton(g, callback_data ='cartremove-{}'.format(g))])
                total = total + float(g.split(' ')[2])
        
            buttons.append([InlineKeyboardButton('Оплатить', callback_data ='pay')])
            self.cart_message = bot.send_message(chat_id=update.message.chat_id, 
                                     text = 'Сумма: {} UAH'.format(total),
                                     parse_mode=ParseMode.HTML,
                                     reply_markup = InlineKeyboardMarkup(buttons));
    except Exception as e:
        print(e)