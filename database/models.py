from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=150, verbose_name="ФИО")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")

    def __str__(self):
        return self.username
    

class Record(models.Model):
    
    CHOICE_SERVICE = (
        ('main', 'общий клининг'),
        ('general', 'генеральная уборка'),
        ('post-build', 'послестроительная уборка'),
        ('carpent', 'химчистка ковров и мебели'),
        ('other', 'иная услуга'),
    )
    CHOICE_PAYMENT = (
        ('cash', 'наличные'),
        ('card', 'банковская карта'),
    )
    CHOICE_STATUS = (
        ('in-work', 'в работе'),
        ('completed', 'выполнено'),
        ('canceled', 'отменено'),
    )
    
    user = models.ForeignKey(CustomUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    address = models.TextField(verbose_name='Адрес')
    date = models.DateTimeField(verbose_name='Желаемая дата получения')
    service = models.CharField(max_length=50, choices=CHOICE_SERVICE, default='main', verbose_name='Услуга')
    other_service = models.TextField(blank=True, null=True, verbose_name='Описание иной услуги')
    status = models.CharField(max_length=50, choices=CHOICE_STATUS, default='in-work', verbose_name='Статус')
    cancel_reason = models.TextField(verbose_name='Причина отмены', blank=True, null=True)

    class Meta:
        #managed = False
        verbose_name = ("Запись")
        verbose_name_plural = ("Записи")

    def __str__(self):
        return f"Запись #{self.id}"