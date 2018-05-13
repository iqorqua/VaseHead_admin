from app.models import Good
from VaseHead_admin.good import GoodItemInList
from VaseHead_admin.states import *
from VaseHead_admin.new_member_check import *
from VaseHead_admin.response_maker import *
from VaseHead_admin.thirdparty_command import ThitdPartyCommands
import datetime

class Conversation:  
    def __init__(self, id):
            self.id = id
            self.items = []
            self.item_counter = 0
            self.item_color = 0
            self.state = Start  
            self.newclient = NewClient()
            self.newcoworking = NewCoworking()
            self.magazine = None
            self.cart_message = None
            self.datetime = datetime.datetime.now()
            self.cart = []
    def SetMyState(self, state:int):
        self.state = state
    def GetItems(self):
        self.items.clear()
        for good in Good.objects.all():
            self.items.append(GoodItemInList(images = str(good.other_images), name = good.name, description = good.description, price = float(good.price), id = good.pk))
        return self.items

    def NewMemberCreate(self, bot, update):
       if self.state == Start:
          SayHello(bot, update, self)
          self.newclient.userid = update.message.from_user.id
          return
       if self.state == Share_contact:
          if update.message.contact == None:
               AskContact(bot, update, self)
          else:
              self.SetMyState(Gender)
              self.newclient.phone_number = update.message.contact.phone_number
              self.newclient.name = update.message.contact.first_name + ' ' + update.message.contact.last_name
              AskAboutGender(bot, update, self)
          return
       if self.state == Gender:
          AskAboutAge(bot, update, self)
          return
       if self.state == Age:
          AskAboutInvitation(bot, update, self)
          return
       if self.state == WhoInvite:
          AskWhoAreYou(bot, update, self)
          return
       if self.state == WhoAreU:
          AskAboutHobby(bot, update, self)
          return
       if self.state == YourHobby:
          SayThankU(bot, update, self)
          ShowMainMenu(bot, update, self)
          return 

    def ProcessInline(self, bot, update):
        self.datetime = datetime.datetime.now()
        Update_messages_count( bot, update.callback_query, self)
        callback = update.callback_query.data.split('-')
        if not IsNewMember(bot, update, self):
            if callback[0]=='cartremove':
                self.cart.remove(callback[1])
                ShowCart(bot, update.callback_query, self)
            if callback[0]=='buy':
                self.cart.append('{}, {}, {} UAH ❌'. format(Good.objects.all().filter(pk = callback[1]).get().name, callback[2], Good.objects.all().filter(pk = callback[1]).get().price))
                print(self.cart)
            if callback[0]=='next':
                SelectNextGood(bot, update, self)
            if callback[0]=='next_color':
                SelectNextColor(bot, update, self)
            if callback[0]=='previous_color':
                SelectPreviousColor(bot, update, self)
            if callback[0]=='previous':
                SelectPreviousGood(bot, update, self)
            if callback[0]=='Phone':
                SendYanasContact(bot, update, self)
            if callback[0]=='Сity':
                SayShowRoomsAddress(bot, update, self)
                SayShowRoomList(bot, update.callback_query, self)
            if callback[0]=='MainMenu':
                ShowMainMenu(bot, update, self)
            if callback[0]=='Magazine':
                ShowMagazine(bot, update, self)
            if callback[0]=='PartnershipDetails':
                AskHowUWillRealiseProducts(bot, update, self)
            if callback[0]=='Partner':
                self.newcoworking.realise_method = callback[1]
                AskCountry(bot, update, self)
            if callback[0]=='RealiseSquare':
                self.newcoworking.have_realise_square = callback[1]
                AskLink(bot, update, self)
        else:
            if callback[0] == "Gender":
                self.newclient.gender = update.callback_query.data.split('-')[1]
                self.SetMyState(Age)
                AskAboutAge(bot, update, self)
            
            if callback[0] == "Age":
                self.newclient.age = update.callback_query.data.split('-')[1]
                self.SetMyState(WhoInvite)
                AskAboutInvitation(bot, update, self)

            if callback[0] == "WhoInvited":
                self.newclient.who_invited = update.callback_query.data.split('-')[1]
                self.SetMyState(WhoInvite)
                AskWhoAreU(bot, update, self)

            if callback[0] == "WhoAreU":
                self.newclient.who_r_u = update.callback_query.data.split('-')[1]
                self.SetMyState(WhoInvite)
                LastQuestion(bot, update, self)
                AskAboutHobby(bot, update, self)

            if callback[0] == "YourHobby":
                self.newclient.hobby = update.callback_query.data.split('-')[1]
                #make registration
                try:
                    username = ''
                    try:
                        username = self.newclient.username
                        if username == None:
                            username = ''
                    except BaseException:
                        username = ''
                    Client(username = username, name = self.newclient.name, phone = self.newclient.phone_number, gender = self.newclient.gender,  age = self.newclient.age, who_invired = self.newclient.who_invited, profession = self.newclient.who_r_u, hobby = self.newclient.hobby, clientid = self.newclient.userid).save()
                except BaseException:
                    SayHello(bot, update, self)
                    SayErrorInput(bot, update, self)
                self.SetMyState(MainMenu)
                SayThankU(bot, update, self)
                ShowMainMenu(bot, update, self)


    def ExecuteCommand(self, bot, update):
       self.datetime = datetime.datetime.now()
       if "🏪 Магазин" == update.message.text:
          ShowMagazine(bot, update, self)
          return
       if "🔍 Как нас найти" == update.message.text:
          SayHowToFindUs(bot, update, self)
          return
       if "📖 О нас" == update.message.text:
          SayAboutUs(bot, update, self)
          return
       if "🤝 Сотрудничество" == update.message.text:
          ShowCoworking(bot, update)
          return
       if "🛒 Корзина" == update.message.text:
          ShowCart(bot, update, self)
          return
       ThitdPartyCommands(bot, update, self)


    def ProcessMessage(self, bot, update):
        if IsNewMember(bot, update, self):
            self.newclient.username = update.message.chat.username
            self.NewMemberCreate(bot, update)
        else:
            self.ExecuteCommand(bot, update)



   

    

                    