from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import AddCarForm
from .models import Car, Mark

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить машину', 'url_name': 'addcar'},
    {'title': 'Технологии', 'url_name': 'tech'},
    ]


class CarHome(ListView):
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'cars'
    extra_context = {
        'title_low': '5 случайных автомобилей',
        'title_up': 'Мои автомобили'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        '''Создание динамического контекста'''
        context = super().get_context_data(**kwargs)
        marks = Mark.objects.all()
        context['menu'] = menu
        context['marks'] = marks
        context['mark_selected'] = 0
        return context

    def get_queryset(self):
        return Car.objects.order_by('?')[:5]


class MarkList(ListView):
    model = Car
    template_name = 'cars/index.html'
    context_object_name = 'cars'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        '''Создание динамического контекста'''
        context = super().get_context_data(**kwargs)
        marks = Mark.objects.all()
        current_mark = get_object_or_404(
            Mark, slug=self.kwargs["mark_slug"]).name
        context['title_up'] = f'Автомобили марки {current_mark}'
        context['title_low'] = f'Автомобили марки {current_mark}'
        context['menu'] = menu
        context['marks'] = marks
        context['mark_selected'] = self.kwargs['mark_slug']
        return context

    def get_queryset(self):
        return Car.objects.filter(mark__slug=self.kwargs['mark_slug'])


class ShowCar(DetailView):
    model = Car
    template_name = 'cars/car.html'
    slug_url_kwarg = 'car_slug'
    context_object_name = 'car'

    def get_context_data(self, *, object_list=None, **kwargs):
        '''Создание динамического контекста'''
        context = super().get_context_data(**kwargs)
        current_car = get_object_or_404(Car, slug=self.kwargs['car_slug'])
        context['title_up'] = f'{str(current_car.mark)} {str(current_car.model)}'
        context['title_low'] = f'{str(current_car.mark)} {str(current_car.model)}'
        context['menu'] = menu
        context['marks'] = Mark.objects.all()
        context['mark_selected'] = current_car.mark.slug
        return context


class AddCar(CreateView):
    form_class = AddCarForm
    template_name = 'cars/addcar.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        '''Создание динамического контекста'''
        context = super().get_context_data(**kwargs)
        context['title_up'] = 'Добавление автомобиля'
        context['title_low'] = 'На чем катался?'
        context['menu'] = menu
        context['marks'] = Mark.objects.all()
        return context


def about(request):
    context = {
            'title': 'Об авторе',
            'menu': menu}
    return render(request, 'about/author.html', context)


def tech(request):
    context = {
            'menu': menu}
    return render(request, 'about/tech.html', context)


def login(request):
    return HttpResponse('<h1>Авторизация</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Нет нихуя!')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'cars/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        '''Создание динамического контекста'''
        context = super().get_context_data(**kwargs)
        context['title_up'] = 'Регистрация'
        context['title_low'] = 'Давайте знакомиться'
        marks = Mark.objects.all()
        context['menu'] = menu
        context['marks'] = marks
        return context


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'cars/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        '''Создание динамического контекста'''
        context = super().get_context_data(**kwargs)
        context['title_up'] = 'Вход'
        context['title_low'] = 'Авторизация'
        marks = Mark.objects.all()
        context['menu'] = menu
        context['marks'] = marks
        return context

    def get_success_url(self) -> str:
        return reverse_lazy('home')
