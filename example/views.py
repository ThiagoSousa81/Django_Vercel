# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''    
    <!DOCTYPE html>
    <html>
        <head>
            <title>Meu primeiro site em Django</title>
        </head>
        <body>
            <h1>{ print('Minha aplicação Django') }</h1>
            <p>A data de hoje é { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)
