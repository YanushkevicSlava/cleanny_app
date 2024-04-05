from django.shortcuts import render
from .models import Worker


def calculate_cost(request):
    if request.method == "POST":
        cost_room = 40
        cost_san_room = 30
        amount_rooms = int(request.POST.get('room'))
        amount_san_rooms = int(request.POST.get('san_room'))
        calculate = cost_room * amount_rooms + cost_san_room * amount_san_rooms

        worker = Worker.objects.get(id=1)

        context = {
            "calculate": calculate,
            "worker": worker
        }
        return render(request, template_name='service/index.html', context=context)

