from django.http import HttpResponse


def hello(request):
    html = """
    <html>
    <head>
        <style>
            body {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                font-size: 70px;
                font-weight: bold;
                background-color: #343148;
                color: #D7C49E;
                height: 100vh;
                margin: 0;
                gap: 20px;
            }
            .message {
                letter-spacing: 4px;
                line-height: 2;
            }
        </style>
    </head>
    <body>
        <div class="message">안녕하세요</div>
    </body>
    </html>
    """
    return HttpResponse(html)
