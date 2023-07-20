from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    html = """
    <html>
    <head>
        <style>
            body {
                display: flex;
                height: 100vh;
                margin: 0;
                align-items: center;
                justify-content: center;
                font-size: 100px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div>Hello World</div>
    </body>
    </html>
    """
    return HttpResponse(html)
