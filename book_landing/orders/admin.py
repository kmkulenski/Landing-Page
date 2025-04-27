
from django.contrib import admin
from .models import Order

# Админ клас за поръчките
class OrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'address', 'status', 'created_at', 'order_code')
    list_filter = ('status',)
    search_fields = ('full_name', 'email', 'order_code')
    ordering = ('-created_at',)
     # Това ще добави възможност за редактиране на статуса директно в админ панела
    list_editable = ('status',)  # Това ще позволи на администраторите да променят статуса
    # Това ще добави възможност за редактиране на полетата в администрацията
    fields = ('full_name', 'email', 'phone_number', 'address', 'status', 'payment_method', 'order_code')

# Регистриране на модела в админ панела
admin.site.register(Order, OrderAdmin)
