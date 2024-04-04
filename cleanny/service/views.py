from django.shortcuts import render


def index(request):
    text = "На нашем сайте вы можете получить услуги клининга"
    context = {
        "text": text,
    }
    return render(request, "service/index.html", context=context)
