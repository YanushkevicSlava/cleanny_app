from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import FormCreateOrder
from .models import Worker, Order


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

    else:
        calculate = 70
        worker = Worker.objects.get(id=1)

        context = {
            "calculate": calculate,
            "worker": worker
        }
        return render(request, template_name='service/index.html', context=context)


# def order_create(request):
#     if request.method == 'POST':
#         form = FormCreateOrder(request.POST or None)
#         if form.is_valid():
#             first_name = form.cleaned_data.get("first_name")
#             last_name = form.cleaned_data.get("last_name")
#             surname = form.cleaned_data.get("surname")
#             email = form.cleaned_data.get("email")
#             tel = form.cleaned_data.get("tel")
#             street = form.cleaned_data.get("street")
#             housing = form.cleaned_data.get("housing")
#             home = form.cleaned_data.get("home")
#             flat = form.cleaned_data.get("flat")
#             discount = form.cleaned_data.get("discount")
#             cleaning_time = form.cleaned_data.get("cleaning_time")
#             services = form.cleaned_data.get("services")
#             obj = Order.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 surname=surname,
#                 email=email,
#                 tel=tel,
#                 street=street,
#                 housing=housing,
#                 home=home,
#                 flat=flat,
#                 discount=discount,
#                 cleaning_time=cleaning_time,
#                 services=services
#             )
#             obj.save()
#             return render(request, "HTML/join.html",{})
#     else:
#         form = FormCreateOrder()
#         context = {"form": form}
#         return render(request, "service/order-create.html", context=context)

def order_create(request):

    context = {}

    form = FormCreateOrder(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'service/order-create.html', context)
