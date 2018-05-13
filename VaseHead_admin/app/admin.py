from django.contrib import admin
from app.models import Good, Client, MassSendingReport, Order, DailyMessaging, Coworking


admin.site.register(Client)
admin.site.register(Good)
admin.site.register(MassSendingReport)
admin.site.register(Order)
admin.site.register(DailyMessaging)
admin.site.register(Coworking)



