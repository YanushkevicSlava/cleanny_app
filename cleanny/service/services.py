from django.conf import settings
from django.core.mail import send_mass_mail


def send_email(workers_emails):
    """
    Функция отправляет сообщение на электронную почту покупателя.

    """
    # Текст письма
    html_content = 'Добрый день!\n'
    html_content += f'В списке заказов появился новый заказ!'
    # Получение почты сервиса и отправка письма покупателю
    email_from = settings.EMAIL_HOST_USER
    send_mass_mail(html_content, from_email=email_from, recipient_list=workers_emails)
