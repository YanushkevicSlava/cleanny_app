from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Worker
from .services import send_email


@receiver(post_save, sender=Order)
def check_new_order_in_orders(sender, instance, created, **kwargs):
    """
    Функция сигнал, которая проверяет наличие нового заказа, при его наличии отправляет письмо работникам.
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    """
    if created:
        workers_emails = Worker.objects.all()
        send_email(workers_emails=workers_emails)
