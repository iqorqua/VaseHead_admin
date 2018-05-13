from app.models import Client, DailyMessaging
from datetime import date, datetime

def IsNewMember(bot, update, self):
    Update_messages_count(bot, update, self)
    try:
       return not Client.objects.filter(clientid=update.message.chat_id).exists()
    except:
         return not Client.objects.filter(clientid=update.callback_query.message.chat_id).exists()
  
def Update_messages_count(bot, update, self):
   try:
       today = date.today()
       try:
         temp = DailyMessaging.objects.filter(date__year=today.year, date__month = today.month, date__day = today.day).filter(user_id = update.message.chat_id)
       except Exception as e:
           print(e)
           temp = DailyMessaging(user_name = (update.callback_query.message.from_user.first_name + update.callback_query.message.from_user.last_name), user_id = update.callback_query.message.chat_id, messages_count = 0).save()
       if not temp:
           DailyMessaging(user_name = (update.message.from_user.first_name + update.message.from_user.last_name), user_id = update.message.chat_id, messages_count = 0).save();
           temp = DailyMessaging.objects.filter(date__year=today.year, date__month = today.month, date__day = today.day).filter(user_id = update.message.chat_id)
       temp.update(messages_count=int(temp[0].messages_count)+1)
   except:
        return