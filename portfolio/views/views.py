# Create your views here.
from django.http import HttpResponse
from django.template import loader

import datetime

def index(request):
    template = loader.get_template('index.html')
    context = {
        'datetime_now': datetime.datetime.now()
    }
    return HttpResponse(template.render(context, request))