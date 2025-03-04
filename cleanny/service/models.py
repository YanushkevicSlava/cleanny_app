from django.db import models


class Worker(models.Model):
    """Модель сотрудника"""
    first_name = models.CharField(max_length=100,
                                  help_text="Введите имя сотрудника",
                                  verbose_name="Имя сотрудника")
    last_name = models.CharField(max_length=100,
                                 help_text="Введите фамилию сотрудника",
                                 verbose_name="Фамилия сотрудника")
    email = models.CharField(max_length=100,
                             help_text="Введите email сотрудника",
                             verbose_name="Email сотрудника")
    photo = models.ImageField(upload_to="images",
                              help_text="Загрузите фото сотрудника",
                              verbose_name="Фото сотрудника")
    work_story = models.TextField(help_text="Введите историю о заказе",
                                  verbose_name="История о заказе",
                                  blank=True)
    experience = models.IntegerField(help_text="Введите стаж работы",
                                     verbose_name="Стаж работы",
                                     blank=True)


class Service(models.Model):
    """Модель предоставляемой услуги"""
    name = models.CharField(max_length=100,
                            help_text="Введите название услуги",
                            verbose_name="Название услуги")
    cost = models.IntegerField(help_text="Введите стоимость улуги",
                               verbose_name="Стоимость услуги")

    def __str__(self):
        return self.name


class Order(models.Model):
    """Модель заказа"""
    DISCOUNT = (
        (0, '1 раз или первый раз'),
        (7, 'раз в месяц 7%'),
        (10, 'раз в две недели 10%'),
        (15, 'раз в неделю 15%'),
    )
    cleaning_time = models.DateTimeField(help_text="Введите дату и время уборки",
                                         verbose_name="Дата и время уборки",
                                         )
    services = models.ForeignKey('Service',
                                 on_delete=models.CASCADE,
                                 help_text="Выберите услуги",
                                 verbose_name="Услуга")
    first_name = models.CharField(max_length=100,
                                  help_text="Введите имя",
                                  verbose_name="Имя клиента")
    last_name = models.CharField(max_length=100,
                                 help_text="Введите фамилию",
                                 verbose_name="Фамилия клиента")
    surname = models.CharField(max_length=100,
                               help_text="Введите Отчество",
                               verbose_name="Отчество клиента")
    email = models.EmailField(max_length=100,
                              help_text="Введите email",
                              verbose_name="Email клиента")
    tel = models.IntegerField(help_text="Введите номер телефона с кодом",
                              verbose_name="Номер клиента")
    street = models.CharField(max_length=100,
                              help_text="Введите улицу",
                              verbose_name="Улица клиента")
    housing = models.CharField(max_length=100,
                               help_text="Введите корпус",
                               verbose_name="Корпус клиента",
                               blank=True, null=True)
    home = models.CharField(max_length=100,
                            help_text="Введите номер дома",
                            verbose_name="Номер дома клиента")
    flat = models.CharField(max_length=100,
                            help_text="Введите номер квартиры",
                            verbose_name="Номер квартиры клиента")
    discount = models.IntegerField(help_text="Выберите переодичность уборки",
                                   verbose_name="Переодичность уборки со скидкой",
                                   blank=True, default=0,
                                   choices=DISCOUNT)

