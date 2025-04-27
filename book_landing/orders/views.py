from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from django.core.mail import send_mail

def landing_page(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # Записване на поръчката в базата данни
            order = Order(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                consent_to_privacy_policy=form.cleaned_data['consent_to_privacy_policy']
            )
            order.save()

            # Изпращане на имейл потвърждение до клиента
            # send_mail(
            #     'Поръчката Ви е потвърдена',
            #     'Вашата поръчка е успешна. Благодарим Ви за поръчката! Възможно е да получите допълнителна информация по имейл.',
            #     'admin@bookstore.com',  # Администраторски имейл
            #     [form.cleaned_data['email']],
            #     fail_silently=False,
            # )

            # Изпращане на имейл уведомление до администратора
            # send_mail(
            #     'Нова поръчка',
            #     f"Нова поръчка от {form.cleaned_data['full_name']}:\n"
            #     f"Телефон: {form.cleaned_data['phone']}\n"
            #     f"Адрес: {form.cleaned_data['address']}\n"
            #     f"Съгласие с политиката за поверителност: {'Да' if form.cleaned_data['consent_to_privacy_policy'] else 'Не'}",
            #     'admin@bookstore.com',  # Администраторски имейл
            #     ['admin@bookstore.com'],
            #     fail_silently=False,
            # )

            # Пренасочване към страницата за благодарност
            return redirect('orders:thank_you')  # Актуализирахме URL-то

    else:
        form = OrderForm()

    return render(request, 'orders/landing_page.html', {'form': form})

def order_success(request):
    # Тази функция може да показва съобщение за успешна поръчка или нещо друго, ако е необходимо
    return render(request, 'orders/order_success.html')

def thank_you(request):
    # Страница за благодарност след успешна поръчка
    return render(request, 'orders/thank_you.html')
