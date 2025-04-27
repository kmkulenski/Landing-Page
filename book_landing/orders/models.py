import uuid
from django.db import models

class Order(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Име и фамилия")
    email = models.EmailField(verbose_name="Имейл")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес за доставка")
    consent_to_privacy_policy = models.BooleanField(default=False, verbose_name="Съгласие с политиката за поверителност")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата на поръчката")
    
    # Поле за статус на поръчката
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'В очакване'), ('completed', 'Завършена')], 
        default='pending',
        verbose_name="Статус на поръчката"
    )

    # Генериране на уникален код чрез UUID
    order_code = models.CharField(
        max_length=36, 
        unique=True, 
        default=uuid.uuid4, 
        editable=False, 
        verbose_name="Код на поръчката"
    )

    def __str__(self):
        return f"Поръчка от {self.full_name} на {self.created_at.strftime('%d.%m.%Y %H:%M')}"
