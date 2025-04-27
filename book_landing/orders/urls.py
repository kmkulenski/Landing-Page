from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Начална страница
    path('success/', views.order_success, name='order_success'),  # Потвърждение
    path('thank-you/', views.thank_you, name='thank_you'),  # Страница за благодарност
    # други пътища...
]
