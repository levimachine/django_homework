import random
from django.core.mail import send_mail
from django.core.management.utils import get_random_secret_key
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from config.settings import DEFAULT_FROM_EMAIL
from users.forms import RegisterForm
from users.models import User
from django.shortcuts import redirect


class UserCreateView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:user_login')

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            secret_key = get_random_secret_key()[0:6]
            user.secret_key = secret_key
            send_mail(
                subject='Подтверждение регистрации Бобр.com',
                message=f'Код подтверждения {secret_key}',
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False
            )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    fields = ('user_input_secret_key',)
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user_form = form.save()
        if self.object.secret_key == user_form.user_input_secret_key:
            self.object.is_verify = True
        return super().form_valid(form)


def reset_password(request):
    if request.user.is_authenticated:
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        send_mail(
            subject='Смена пароля Бобр.com',
            message=f'Новый пароль - {new_password}',
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[request.user.email],
            fail_silently=False
        )
        request.user.set_password(new_password)
        request.user.save()

    return redirect(to=reverse('catalog:home'))

