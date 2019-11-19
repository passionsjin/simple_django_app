import socket

from django.shortcuts import render

# Create your views here.


def hello(request):
    print(request)
    info = {'hostname': socket.gethostname(),
            'ip': socket.gethostbyname(socket.getfqdn())
            }
    return render(request, 'hello.html', {'title': 'hello', 'body': info})

