"""
Definition of models.
"""

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class Good(models.Model):
    name=models.CharField(max_length = 128)
    description = models.TextField()
    price = models.FloatField()
    #image = models.ImageField(upload_to = "app/static/app/images/", default = "", )
    other_images = models.TextField(default = "")
    def __str__(self):
        return self.name
    def image_list(self):
        return self.other_images.split(',')

class Client(models.Model):
    username = models.CharField(max_length = 256, default = '', blank = True)
    name = models.CharField(max_length = 256)
    phone = models.CharField(max_length = 13)
    gender = models.CharField(max_length = 1)
    age = models.CharField(max_length = 6)
    who_invired = models.CharField(max_length = 13)
    profession = models.CharField(max_length = 30)
    hobby = models.CharField(max_length = 30)
    clientid = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class DailyMessaging(models.Model):
    user_name = models.CharField(max_length = 256, blank = False)
    user_id = models.CharField(max_length = 100)
    messages_count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{} {}'.format(self.user_name, self.date)

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length = 100)
    user_name = models.CharField(max_length = 256)
    user_phone = models.CharField(max_length = 13)
    good_id = models.IntegerField()
    good_name = models.CharField(max_length = 100)
    good_color = models.CharField(max_length = 100)
    is_done = models.BooleanField(default = False)
    def __str__(self):
        return '{} {}'.format(self.user_name, self.date)

class Coworking(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length = 100)
    user_name = models.CharField(max_length = 256)
    realise_method = models.CharField(max_length = 13)
    country_city = models.CharField(max_length = 120)
    sales_count = models.CharField(max_length = 120)
    have_realise_square = models.CharField(max_length = 100)
    link = models.CharField(max_length = 200)
    social_network = models.CharField(max_length = 200)
    contact_phone = models.CharField(max_length = 13)
    email = models.CharField(max_length = 100)
    is_done = models.BooleanField(default = False)
    def __str__(self):
        return '{} {}'.format(self.user_name, self.date)

class OverwriteStorage(FileSystemStorage):
    '''
    Muda o comportamento padrão do Django e o faz sobrescrever arquivos de
    mesmo nome que foram carregados pelo usuário ao invés de renomeá-los.
    '''
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/',storage=OverwriteStorage())
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MassSendingReport(models.Model):
    description = models.TextField(max_length=255, blank=False, default = '')
    text = models.TextField(max_length=255, blank=False)
    filter = models.TextField(max_length=255, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default = 0)
    def __str__(self):
        return self.description


# Create your models here.
