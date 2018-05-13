"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Good, Client, MassSendingReport, DailyMessaging, Order, Coworking
import json
from VaseHead_admin.bot_settings import SaveSettings, UpdateSettings
from VaseHead_admin.response_maker import MakeMassSending
from django.core.files.storage import FileSystemStorage
from django.views import View
from app.forms import PhotoForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core import serializers

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'goods_count': len(Good.objects.all()),
            'clients_count': len(Client.objects.all()),
        }
    )

def analytics(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/analytics.html',
        {
            'title':'Analitycs',
            'goods_count': len(Good.objects.all()),
            'clients_count': len(Client.objects.all()), 
        }
    )

def sendmass(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.POST:
        MakeMassSending(request.POST)
        return HttpResponseRedirect(reverse('sendmass'))
    return render(
        request,
        'app/sendingmass.html',
        {
            'title':'Mass Message Sending',
            'reports': MassSendingReport.objects.all(),
            'goods_count': len(Good.objects.all()),
            'clients_count': len(Client.objects.all()),
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
            'goods_count': len(Good.objects.all()),
            'clients_count': len(Client.objects.all()),
        }
    )

def clients(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/clients.html',
        {
            'title':'Clients',
            'clients': Client.objects.all(),
            'goods_count': len(Good.objects.all()),
            'clients_count': len(Client.objects.all()),
        }
    )

def coworking(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/coworking.html',
        {
            'title':'Coworking',
            'coworkers': Coworking.objects.all(),
            'goods_count': len(Good.objects.all()),
            'clients_count': len(Client.objects.all()),
        }
    )

def orders(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/orders.html',
        {
            'title':'Orders',
            'orders': Order.objects.all(),
            'goods_count': len(Good.objects.all()),
            'clients_count': len(Client.objects.all()),
        }
    )

def goods(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/goods.html',
        {
            'title':'Goods',
            'goods': Good.objects.all(),
            'goods_count': len(Good.objects.all()),
            'clients_count': len(Client.objects.all()),
        }
    )

def good(request, pk):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
    return render(
        request,
        'app/good_item.html',
        {
            'title':'Goods',
            'good': Good.objects.filter(id = pk),
            'goods_count': len(Good.objects.all()),
            'clients_count': len(Client.objects.all()),
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'goods_count': len(Good.objects.all()),
            'clients_count': len(Client.objects.all()),
        }
    )

def settings(request):
    """Renders the about page."""
    settings_items = ''
    with open('VaseHead_admin/settings.txt') as json_file:  
         settings_items = json.load(json_file)
    if request.method == 'POST':
        settings_to_save = settings_items
        for k in settings_items[0]:
            settings_to_save[0][k] = request.POST[k.replace(" ", "")]
        SaveSettings(new_settings=settings_to_save)
        UpdateSettings()
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/settings.html',
        {
            'settings_items': settings_items[0],
            'goods_count': len(Good.objects.all()),
        }
    )

from app.models import Photo
from django.http import JsonResponse

class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

def add_good(request):
    assert isinstance(request, HttpRequest)
    result = str(request.POST)
    if request.POST.get('images') != None:
         new_item = request.POST.get('new_good').split('&')
         Good(name = decoder(new_item[0].split("=")[1]), description = decoder(new_item[1].split("=")[1]), price = float(new_item[2].split("=")[1]), other_images = decoder(request.POST.get('images'))).save()
    else:
        data = {}
        data['result'] = 'Success'
        return HttpResponse(json.dumps(data), content_type="application/json")
    return JsonResponse({})

def analitycs_json(request):
    assert isinstance(request, HttpRequest)
    try:
        d = datetime.strptime(request.POST.get('date'), "%d.%m.%Y").date()
        obj = DailyMessaging.objects.filter(date__year = d.year, date__day = d.day, date__month = d.month)
        serialized = serializers.serialize('json', list(obj), fields=('user_name', 'messages_count'))
        
        serialized1 = []
        obj = Order.objects.filter(date__year = d.year, date__day = d.day, date__month = d.month)
        for g in Good.objects.all():
            serialized1.append({'name':g.name, 'count':obj.filter(good_name__contains=g.name).count()})

        obj = Client.objects.filter(date__year = d.year, date__day = d.day, date__month = d.month)
        serialized2 = serializers.serialize('json', list(obj), fields=('user_name'))
        return JsonResponse(serialized+"#"+str(json.dumps(serialized1))+"#"+str(serialized2), safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'pisdec':True}, safe = False)

def delete_good(request):
    assert isinstance(request, HttpRequest)
    result = request.POST.get('delete')
    if result != None:
        Good.objects.filter(id=result).delete()
    return JsonResponse({})

def decoder(result:str):
    decodod_line = ""
    i=0
    while i<len(result):
             if result[i] == '%':
                 if result[i+1] == '2' and result[i+2] == '0':
                    decodod_line = decodod_line + " "
                    i=i+3
                 else:
                     try:
                        decodod_line = decodod_line + bytearray.fromhex(result[i+1]+result[i+2] + ' ' + result[i+4]+result[i+5]).decode()
                        i=i+6
                     except:
                        i=i+1
             else:
                decodod_line = decodod_line + result[i]
                i=i+1
    return decodod_line