from VaseHead_admin import states
from VaseHead_admin.response_maker import *
import validators
import re
from app.models import Coworking

def ThitdPartyCommands(bot, update, self):
    if self.state == states.AskCountry:
        # country realese
        if len(update.message.text.split(','))<2:
            SayErrorInput(bot, update, self)
            return
        else:
            self.newcoworking.country_city = update.message.text
            self.SetMyState(states.AskSalesCount)
            AskSalesCount(bot, update, self)
            return
    if self.state == states.AskSalesCount:
        # sales count realese
        self.newcoworking.sales_count = update.message.text
        self.SetMyState(states.AskName)
        AskName(bot, update, self)
        return
    if self.state == states.AskName:
        # name
        if len(update.message.text.split(' '))<2:
            SayErrorInput(bot, update, self)
            return
        else:
            self.newcoworking.user_name = update.message.text
            self.SetMyState(states.AskRealeseSquare)
            AskAboutRealeseSquare(bot, update, self)
        return
    if self.state == states.AskUrl:
        if validators.url(update.message.text):
        # url
            self.newcoworking.link = update.message.text
            self.SetMyState(states.AskSocialNetwork)
            AskSocialNetwork(bot, update, self)
            return
        else: 
            SayErrorInput(bot, update, self)
            return
    if self.state == states.AskSocialNetwork:
        #social networks
            self.newcoworking.social_network = update.message.text
            self.SetMyState(states.AskPnoneNumber)
            AskPhoneNumber(bot, update, self)
            return
    if self.state == states.AskPnoneNumber:
        if re.match(r'[\+][3][8][0][456789][043678][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', update.message.text):
            self.newcoworking.contact_phone = update.message.text
            self.SetMyState(states.AskEmail)
            AskEmail(bot, update, self)
            return
        else: 
            SayErrorInput(bot, update, self)
            return
    if self.state == states.AskEmail:
         if re.match(r'[^@]+@[^@]+\.[^@]+', update.message.text):
            #save email and this object
            self.newcoworking.email = update.message.text
            print(self.newcoworking.user_name)
            print(self.newcoworking.contact_phone)
            print(self.newcoworking.email)
            print(self.newcoworking.sales_count)
            print(self.newcoworking.user_id)
            print(self.newcoworking.country_city)
            print(self.newcoworking.realise_method )
            print(self.newcoworking.have_realise_square )
            print(self.newcoworking.link )
            print(self.newcoworking.social_network )
            Coworking(user_id= self.newcoworking.user_id, 
                             user_name = self.newcoworking.user_name, 
                             realise_method = self.newcoworking.realise_method , 
                             country_city = self.newcoworking.country_city,  
                             have_realise_square = self.newcoworking.have_realise_square,
                             sales_count = self.newcoworking.sales_count, 
                             link = self.newcoworking.link,
                             social_network = self.newcoworking.social_network, 
                             contact_phone = self.newcoworking.contact_phone , 
                             email = self.newcoworking.email 
                             ).save()
            self.SetMyState(states.MainMenu)
            SayHighFive(bot, update, self)
            ShowMainMenu(bot, update, self)
            return
         else: 
            SayErrorInput(bot, update, self)
            return
    ShowMainMenu(bot, update, self)

